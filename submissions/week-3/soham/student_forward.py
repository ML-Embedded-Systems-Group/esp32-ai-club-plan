"""Tiny PLE decoder matching _make_golden.py forward_ref."""

import math
import numpy as np

VOCAB = 32
D = 16
N_LAYERS = 2
N_HEADS = 2
DH = 8
FFN = 32
SEQ = 8
PLE = 8
THETA = 10000.0
EPS = 1e-6


def rmsnorm(x, w):
    ms = np.mean(x.astype(np.float64) ** 2, axis=-1, keepdims=True) + EPS
    return (w * x * (1.0 / np.sqrt(ms))).astype(np.float32)


def silu(x):
    return x * (1.0 / (1.0 + np.exp(-x.astype(np.float64)))).astype(np.float32)


def gelu(x):
    z = x / math.sqrt(2.0)
    erf = np.frompyfunc(math.erf, 1, 1)(z).astype(np.float64)
    return (0.5 * x * (1.0 + erf)).astype(np.float32)


def softmax(x, axis=-1):
    x = x.astype(np.float64)
    x = x - np.max(x, axis=axis, keepdims=True)
    e = np.exp(x)
    return (e / np.sum(e, axis=axis, keepdims=True)).astype(np.float32)


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


def linear(x, w):
    return x @ w.T


def attn(x, w_qkv, w_proj, cos, sin):
    B, T, C = x.shape
    qkv = linear(x, w_qkv)
    q, k, v = np.split(qkv, 3, axis=-1)
    q = q.reshape(B, T, N_HEADS, DH).transpose(0, 2, 1, 3)
    k = k.reshape(B, T, N_HEADS, DH).transpose(0, 2, 1, 3)
    v = v.reshape(B, T, N_HEADS, DH).transpose(0, 2, 1, 3)
    q, k = apply_rope(q, cos, sin), apply_rope(k, cos, sin)
    scale = DH ** -0.5
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
    x = weights["tok_emb"][idx]
    cos, sin = build_rope(SEQ, DH, THETA)
    cos, sin = cos[:T], sin[:T]

    ple = linear(x, weights["ple_model_proj"]) * (D ** -0.5)
    ple = rmsnorm(ple.reshape(B, T, N_LAYERS, PLE), weights["ple_proj_norm"])
    table = weights["ple_table"][idx].reshape(B, T, N_LAYERS, PLE)
    ple = (ple + table * (PLE ** 0.5)) * (2 ** -0.5)

    for i in range(N_LAYERS):
        p = f"block{i}_"
        x = x + attn(
            rmsnorm(x, weights[p + "attn_norm"]),
            weights[p + "qkv"],
            weights[p + "attn_proj"],
            cos,
            sin,
        )
        x = x + swiglu(
            rmsnorm(x, weights[p + "ffn_norm"]),
            weights[p + "gate"],
            weights[p + "up"],
            weights[p + "down"],
        )
        g = gelu(linear(x, weights[p + "ple_gate"]))
        x = x + rmsnorm(linear(g * ple[:, :, i], weights[p + "ple_proj"]), weights[p + "ple_norm"])

    x = rmsnorm(x, weights["out_norm"])
    logits = x @ weights["tok_emb"].T
    return logits.astype(np.float32)