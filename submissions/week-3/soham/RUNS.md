## Token path

1. **Token Input:** Receive token indices `idx` of shape `(1, T)`.
2. **Embedding:** Look up base representations `x = tok_emb[idx]` of shape `(1, T, 16)`.
3. **PLE Static Prep:**
   - Linear projection: `ple = (x @ ple_model_proj.T) * (1 / sqrt(16))`.
   - Per-slice RMSNorm using `ple_proj_norm` with `eps=1e-6`.
   - Table lookup: `table = ple_table[idx] * sqrt(8)`.
   - Combined PLE feature: `ple = (ple + table) * (1 / sqrt(2))`.
4. **Transformer Blocks (x2):**
   - **Pre-Attn RMSNorm:** Compute `rmsnorm(x, block_attn_norm)`.
   - **QKV Projection:** Compute `qkv = rmsnorm(x) @ block_qkv.T` split into `q, k, v`.
   - **RoPE:** Apply half-split rotary embeddings on `q` and `k` using base `theta=10000.0`.
   - **Causal Self-Attention:** Scaled dot-product attention `(q @ k.T) / sqrt(8)` with causal upper-triangular mask, `float64` stable softmax, multiplied by `v`, followed by `block_attn_proj`.
   - **Residual 1:** `x = x + attn_out`.
   - **SwiGLU FFN:** Compute `silu(rmsnorm(x) @ gate.T) * (rmsnorm(x) @ up.T) @ down.T`.
   - **Residual 2:** `x = x + ffn_out`.
   - **PLE Injection:** Compute gate `g = gelu(x @ block_ple_gate.T)`, project gated slice `(g * ple[:, :, i]) @ block_ple_proj.T`, normalize with `block_ple_norm`, and accumulate into `x`.
5. **Final Norm & Unembedding:** Pass through `rmsnorm(x, out_norm)` and project through tied weight `tok_emb.T` to produce output logits of shape `(1, T, 32)`.

## Runs

### Run 1
- **Command:** `python check.py`
- **max abs diff:** N/A (execution failed)
- **Changes made:** Executed starter stub containing `raise NotImplementedError("fill this function")` to confirm test harness behavior.

### Run 2
- **Command:** `python check.py`
- **max abs diff:** `1.42857143e-01`
- **Changes made:** Implemented initial NumPy forward pass with standard interleaved RoPE and default single-precision `float32` RMSNorm with `eps=1e-5`. Failed due to RoPE indexing differences and normalization accumulation precision.

### Run 3
- **Command:** `python check.py`
- **max abs diff:** `8.27189201e-04`
- **Changes made:** Switched RoPE implementation to match the repository's split-half structure (`half = head_dim // 2`) and updated the RMSNorm epsilon to `1e-6`. PLE gating formulation still used standard sigmoid instead of the repository's erf-based GELU.

### Run 4
- **Command:** `python check.py`
- **max abs diff:** `5.96046448e-08`
- **Status:** PASS
- **Changes made:** Aligned PLE gating to `gelu(linear(x, ple_gate))` and promoted intermediate accumulators in RMSNorm, Softmax, and RoPE frequencies to `float64` prior to final casting. Output matched frozen golden logits within the `1e-5` threshold.

## Final max abs diff

`5.96046448e-08` (PASS, threshold is `< 1e-5`)

## What I still need to learn

- How the per-slice scaling factor `PLE ** 0.5` affects activation dynamic range during integer quantization on hardware registers.
- How to efficiently implement split-half RoPE transformations inside an ESP32-S3 SIMD kernel without generating extra intermediate transposition overhead.
- Memory streaming strategies required when reading the large `ple_table` directly from external flash via SPI cache without stalling the core execution pipeline.
