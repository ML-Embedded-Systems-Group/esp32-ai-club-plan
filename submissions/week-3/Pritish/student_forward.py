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
    rms = np.sqrt(
        np.mean(
            x.astype(np.float64) ** 2,
            axis=-1,
            keepdims=True
        ) + EPS
    )
    return (w * x / rms).astype(np.float32)


def silu(x):
    return (
        x * (
            1.0 / (
                1.0 + np.exp(-x.astype(np.float64))
            )
        )
    ).astype(np.float32)


def gelu(x):
    cdf = 0.5 * (
        1.0
        + np.vectorize(math.erf)(
            x.astype(np.float64) / math.sqrt(2.0)
        )
    )
    return (x * cdf).astype(np.float32)


def softmax(x, axis=-1):
    e = np.exp(
        x.astype(np.float64)
        - x.max(axis=axis, keepdims=True)
    )
    return (
        e / e.sum(axis=axis, keepdims=True)
    ).astype(np.float32)


def mm(x, w):
    return x @ w.T


def build_rope(seq_len, head_dim, theta):
    dims = np.arange(
        0,
        head_dim,
        2,
        dtype=np.float64
    )

    freqs = np.outer(
        np.arange(seq_len, dtype=np.float64),
        1.0 / theta ** (dims / head_dim)
    )

    return (
        np.cos(freqs).astype(np.float32),
        np.sin(freqs).astype(np.float32)
    )


def apply_rope(x, cos, sin):
    x1 = x[..., :DH // 2]
    x2 = x[..., DH // 2:]

    cos = cos[None, None, :x.shape[2]]
    sin = sin[None, None, :x.shape[2]]

    return np.concatenate(
        [
            x1 * cos - x2 * sin,
            x2 * cos + x1 * sin
        ],
        axis=-1
    )


def attention(x, w_qkv, w_proj, cos, sin):
    B, T, C = x.shape

    q, k, v = np.split(
        mm(x, w_qkv),
        3,
        axis=-1
    )

    def to_heads(t):
        return t.reshape(
            B,
            T,
            N_HEADS,
            DH
        ).transpose(0, 2, 1, 3)

    q = to_heads(q)
    k = to_heads(k)
    v = to_heads(v)

    q = apply_rope(q, cos, sin)
    k = apply_rope(k, cos, sin)

    scores = (
        q.astype(np.float64)
        @ k.astype(np.float64).transpose(0, 1, 3, 2)
        * (DH ** -0.5)
    )

    scores = np.where(
        np.triu(
            np.ones((T, T), dtype=bool),
            1
        ),
        -1e9,
        scores
    )

    out = (
        softmax(scores) @ v
    ).transpose(
        0,
        2,
        1,
        3
    ).reshape(
        B,
        T,
        C
    )

    return mm(out, w_proj)


def swiglu(x, w_gate, w_up, w_down):
    return mm(
        silu(mm(x, w_gate)) * mm(x, w_up),
        w_down
    )


def forward(weights, idx):
    B, T = idx.shape

    x = weights["tok_emb"][idx]

    cos, sin = build_rope(
        SEQ,
        DH,
        THETA
    )

    cos = cos[:T]
    sin = sin[:T]

    ple = (
        mm(
            x,
            weights["ple_model_proj"]
        )
        * (D ** -0.5)
    )

    ple = rmsnorm(
        ple.reshape(
            B,
            T,
            N_LAYERS,
            PLE
        ),
        weights["ple_proj_norm"]
    )

    ple = (
        ple
        + weights["ple_table"][idx].reshape(
            B,
            T,
            N_LAYERS,
            PLE
        ) * (PLE ** 0.5)
    ) * (2 ** -0.5)

    for i in range(N_LAYERS):
        p = f"block{i}_"

        x = x + attention(
            rmsnorm(
                x,
                weights[p + "attn_norm"]
            ),
            weights[p + "qkv"],
            weights[p + "attn_proj"],
            cos,
            sin
        )

        x = x + swiglu(
            rmsnorm(
                x,
                weights[p + "ffn_norm"]
            ),
            weights[p + "gate"],
            weights[p + "up"],
            weights[p + "down"]
        )

        g = gelu(
            mm(
                x,
                weights[p + "ple_gate"]
            )
        )

        x = x + rmsnorm(
            mm(
                g * ple[:, :, i],
                weights[p + "ple_proj"]
            ),
            weights[p + "ple_norm"]
        )

    x = rmsnorm(
        x,
        weights["out_norm"]
    )

    return (
        x @ weights["tok_emb"].T
    ).astype(np.float32)