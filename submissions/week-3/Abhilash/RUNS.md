## Token path
1. input token `id`
2. `tok_emb` lookup (embedding)
3. PLE table lookup and mixing with `ple_model_proj`
4. For each block:
   - Apply `rmsnorm`, `attn` (with `apply_rope`), and add residual
   - Apply `rmsnorm`, `swiglu` FFN, and add residual
   - Compute `gelu` gate on input and multiply with `ple` slice, then `ple_proj` and `rmsnorm`, add residual
5. Final `rmsnorm`
6. Tied `tok_emb` projection to `logits`

## Runs

- `python check.py`: `NotImplementedError("fill this function")` (Initial state)
- `python check.py`: `max abs diff = 2.456e-01` (Added basic embedding and linear, no layers)
- `python check.py`: `max abs diff = 1.321e-02` (Added blocks, attention and FFN, but without PLE mix)
- `python check.py`: `max abs diff = 2.98023224e-08` (Added complete PLE arm logic. PASS)

## Final max abs diff
`2.98023224e-08`

## What I still need to learn
- Deepen my understanding of the theoretical advantages of PLE (per-layer embeddings) versus conventional architectures in memory-constrained devices.
- Master mapping mathematical definitions like SwiGLU directly to optimized kernel operations.

