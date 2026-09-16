# RUNS.md: Tiny PLE Forward Pass Verification

## Token path

The forward pass in `student_forward.py` follows this sequence from token IDs to final vocabulary logits:

1. **Token Lookup (`id` → `x`)**:
   - `idx` shape: `(batch_size, seq_len)` = `(1, 8)`
   - Token embeddings `tok_emb`: `(vocab_size, d_model)` = `(32, 16)`
   - Embedding lookup: `x = tok_emb[idx]` → shape `(1, 8, 16)`

2. **Base Per-Layer Embedding (`x` → `ple`)**:
   - Projection: `ple_base = x @ ple_model_proj.T` → shape `(1, 8, 8)`
   - Per-slice RMSNorm: `apply_rmsnorm(ple_base, ple_proj_norm)` → shape `(1, 8, 8)`
   - Table lookup & mixing: `ple_tab = ple_table[idx] * sqrt(ple_dim)` → shape `(1, 8, 8)`
   - Combine & scale: `ple = (ple_base + ple_tab) * (1 / sqrt(2))` → shape `(1, 8, 8)`

3. **Transformer Block 0 & Block 1 (`x`, `ple` → `x`)**:
   For each block `layer in [0, 1]`:
   - **Pre-Attention RMSNorm**: `x_norm = apply_rmsnorm(x, block{i}_attn_norm)` → `(1, 8, 16)`
   - **QKV Linear Projections**: `qkv = x_norm @ block{i}_qkv.T` → split into `q`, `k`, `v` each of shape `(1, 2, 8, 8)`
   - **Split-Half RoPE**: Apply sine/cosine position rotations to `q` and `k`
   - **Causal Scaled Dot-Product Attention**: `scores = (q @ k.T) / sqrt(head_dim)` + upper-triangular `-inf` causal mask, followed by softmax and value aggregation
   - **Attention Output Projection & Residual**: `x = x + (attn_out @ block{i}_attn_proj.T)` → `(1, 8, 16)`
   - **Per-Block PLE Gating & Residual**: `gated_ple = gelu(x @ block{i}_ple_gate.T) * ple` → `(1, 8, 8)`, project back `gated_ple @ block{i}_ple_proj.T` → `(1, 8, 16)`, apply `block{i}_ple_norm`, and add residual `x = x + norm_ple`
   - **Pre-FFN RMSNorm & SwiGLU FFN**: `x_ffn_norm = apply_rmsnorm(x, block{i}_ffn_norm)`, SwiGLU `(silu(x @ gate.T) * (x @ up.T)) @ down.T`, and add residual `x = x + ffn_out`

4. **Final Normalisation & Tied Head Projection (`x` → `logits`)**:
   - Final RMSNorm: `x = apply_rmsnorm(x, out_norm)` → shape `(1, 8, 16)`
   - Tied linear projection: `logits = x @ tok_emb.T` → shape `(1, 8, 32)`

---

## Runs

### Run 1: Parameter Key Mapping Alignment
* **Command**: `python check.py`
* **Output / Result**: `KeyError: 'tok_embeddings.weight'`
* **Code Changes**: Inspected `weights.npz` and mapped PyTorch state dictionary naming variations (`tok_embeddings.weight` → `tok_emb`, `attention.wq.weight` → `block{i}_qkv`, `feed_forward.w1` → `block{i}_gate`, etc.).

### Run 2: Per-Slice RMSNorm Dimensions
* **Command**: `python check.py`
* **Output / Result**: `ValueError: operands could not be broadcast together with shapes (1,8,16) (8,)`
* **Code Changes**: Updated `apply_rmsnorm` to handle per-slice normalization when the weight array dimension `(8,)` (`ple_dim`) is smaller than the tensor's hidden dimension `(16)` (`d_model`), reshaping into slices of size 8 before scaling.

### Run 3: Floating-Point Precision & GELU Formulation
* **Command**: `python check.py`
* **Output / Result**: `max abs diff = 4.17551398e-03` (`FAIL`)
* **Code Changes**: Replaced approximate GELU with exact `erf`-based PyTorch GELU (`0.5 * x * (1 + erf(x / sqrt(2)))`) and enforced explicit `np.float32` array casting across all matrix multiplications, activation functions, and RoPE tables to avoid 64-bit NumPy promotion drift.

### Run 4: Per-Block PLE Dimensional Alignment (Final Pass)
* **Command**: `python check.py`
* **Output / Result**: `max abs diff = 2.98023224e-08` (`PASS`)
* **Code Changes**: Standardized the per-block PLE branch so `ple` remains in `ple_dim = 8` space during `gelu(x @ ple_gate.T) * ple` before being projected back to `d_model = 16` via `ple_proj`.

---

## Final max abs diff

* **Final Max Absolute Difference**: `2.98023224e-08`
* **Status**: **`PASS`** (strictly below the `1e-5` threshold)

---

## What I still need to learn

1. **Hardware Acceleration Constraints**: How to map this pure-NumPy tensor execution logic into C/C++ or fixed-point integer arithmetic for resource-constrained ESP32 microcontrollers.
2. **KV Cache Management**: How to convert this batch sequence forward pass into an incremental key-value (KV) cache implementation for efficient step-by-step token generation.
3. **Quantization Precision Effects**: The impact of 8-bit (INT8) or 4-bit (INT4) weight quantization on numerical parity relative to full float32 inference.
