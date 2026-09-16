"""Tiny PLE decoder. Fill forward(weights, idx). NumPy only.

Config (fixed):
  arm=ple, vocab=32, d_model=16, n_layers=2, n_heads=2, head_dim=8,
  ffn_hidden=32, seq_len=8, ple_dim=8, rope_theta=10000
  tied head: logits use tok_emb as the output matrix

idx: int64 array, shape (1, T), T <= 8
return: float32 logits, shape (1, T, 32)

Weight keys in the npz (all float32):
  tok_emb                 (32, 16)
  ple_model_proj          (16, 16)   # d_model -> n_layers * ple_dim
  ple_proj_norm           (8,)
  ple_table               (32, 16)   # vocab x n_layers * ple_dim
  out_norm                (16,)
  block{i}_attn_norm      (16,)
  block{i}_qkv            (16, 48)
  block{i}_attn_proj      (16, 16)
  block{i}_ffn_norm       (16,)
  block{i}_gate           (16, 32)
  block{i}_up             (16, 32)
  block{i}_down           (32, 16)
  block{i}_ple_gate       (16, 8)
  block{i}_ple_proj       (8, 16)
  block{i}_ple_norm       (16,)
  for i in 0, 1

Match slvDev/esp32-ai src/model.py TinyLM.forward for arm=ple.
GELU is the erf form: 0.5 * x * (1 + erf(x / sqrt(2))). Linear layers use
PyTorch layout: weight shape (out, in), y = x @ W.T.
"""

import math
import numpy as np

def rmsnorm(x, w, eps=1e-6):
    ms = np.mean(x.astype(np.float64) ** 2, axis=-1, keepdims=True) + eps
    return (w * x * (1.0 / np.sqrt(ms))).astype(np.float32)

def linear(x, w):
    return x @ w.T

def silu(x):
    return x * (1.0 / (1.0 + np.exp(-x.astype(np.float64)))).astype(np.float32)

def gelu(x):
    z = x / math.sqrt(2.0)
    erf = np.frompyfunc(math.erf, 1, 1)(z).astype(np.float64)
    return (0.5 * x * (1.0 + erf)).astype(np.float32)

def build_rope(seq_len, head_dim, theta):
    inv = 1.0 / (theta ** (np.arange(0, head_dim, 2, dtype=np.float64) / head_dim))
    t = np.arange(seq_len, dtype=np.float64)
    freqs = np.outer(t, inv)
    return np.cos(freqs).astype(np.float32), np.sin(freqs).astype(np.float32)

def apply_rope(x, cos, sin):
    half = x.shape[-1] // 2
    x1, x2 = x[..., :half], x[..., half:]
    cos = cos[None, None, : x.shape[2], :]
    sin = sin[None, None, : x.shape[2], :]
    return np.concatenate([x1 * cos - x2 * sin, x2 * cos + x1 * sin], axis=-1)

def softmax(x, axis=-1):
    x = x.astype(np.float64)
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return (e / np.sum(e, axis=axis, keepdims=True)).astype(np.float32)

def attn(x, w_qkv, w_proj, cos, sin, n_heads, head_dim):
    B, T, C = x.shape
    qkv = linear(x, w_qkv)
    q, k, v = np.split(qkv, 3, axis=-1)
    
    q = q.reshape(B, T, n_heads, head_dim).transpose(0, 2, 1, 3)
    k = k.reshape(B, T, n_heads, head_dim).transpose(0, 2, 1, 3)
    v = v.reshape(B, T, n_heads, head_dim).transpose(0, 2, 1, 3)
    
    q, k = apply_rope(q, cos, sin), apply_rope(k, cos, sin)
    
    scale = head_dim ** -0.5
    scores = (q.astype(np.float64) @ k.astype(np.float64).transpose(0, 1, 3, 2)) * scale
    mask = np.triu(np.ones((T, T), dtype=np.bool_), 1)
    scores = np.where(mask, -1e9, scores)
    
    w = softmax(scores, axis=-1)
    o = w.astype(np.float32) @ v
    
    o = o.transpose(0, 2, 1, 3).reshape(B, T, C)
    return linear(o, w_proj)

def swiglu(x, w_gate, w_up, w_down):
    return linear(silu(linear(x, w_gate)) * linear(x, w_up), w_down)

def forward(weights, idx):
    B, T = idx.shape
    D = 16
    N_LAYERS = 2
    N_HEADS = 2
    DH = 8
    SEQ = 8
    PLE = 8
    THETA = 10000.0

    x = weights["tok_emb"][idx]
    
    cos, sin = build_rope(SEQ, DH, THETA)
    cos, sin = cos[:T], sin[:T]

    ple = linear(x, weights["ple_model_proj"]) * (D ** -0.5)
    ple = rmsnorm(ple.reshape(B, T, N_LAYERS, PLE), weights["ple_proj_norm"])
    table = weights["ple_table"][idx].reshape(B, T, N_LAYERS, PLE)
    ple = (ple + table * (PLE ** 0.5)) * (2 ** -0.5)

    for i in range(N_LAYERS):
        p = f"block{i}_"
        
        x_norm = rmsnorm(x, weights[p + "attn_norm"])
        x = x + attn(x_norm, weights[p + "qkv"], weights[p + "attn_proj"], cos, sin, N_HEADS, DH)
        
        x_norm = rmsnorm(x, weights[p + "ffn_norm"])
        x = x + swiglu(x_norm, weights[p + "gate"], weights[p + "up"], weights[p + "down"])
        
        g = gelu(linear(x, weights[p + "ple_gate"]))
        ple_out = rmsnorm(linear(g * ple[:, :, i], weights[p + "ple_proj"]), weights[p + "ple_norm"])
        x = x + ple_out

    x = rmsnorm(x, weights["out_norm"])
    logits = x @ weights["tok_emb"].T
    return logits.astype(np.float32)
