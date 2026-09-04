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

import numpy as np


def forward(weights, idx):
    raise NotImplementedError("fill this function")
