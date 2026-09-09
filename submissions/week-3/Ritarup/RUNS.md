## Token path

1. `idx` → token embedding
2. Token embedding → PLE
3. PLE → Block 0
4. Block 0 → Block 1
5. Block 1 → final RMSNorm
6. Final RMSNorm → tied output head
7. Output head → logits

## Runs

### Run 1

Command:

`python check.py`

Change:

Started the forward function with the token embedding: `x = weights["tok_emb"][idx]`.

max abs diff:

`3.62037480e-01`

Result:

`FAIL`

### Run 2

Command:

`python check.py`

Change:

Added the PLE side-stream: projected `x` through `ple_model_proj`, scaled by `D⁻⁰·⁵`, reshaped to `[B, T, N_LAYERS, PLE]`, applied `rmsnorm`, then added the `ple_table` lookup scaled by `PLE⁰·⁵`, and mixed with `2⁻⁰·⁵`.

max abs diff:

`3.62037480e-01`

Result:

`FAIL`

### Run 3

Command:

`python check.py`

Change:

Added `build_rope` and `apply_rope` for positional encoding, `attention` (QKV projection → RoPE → causal mask → softmax → output projection), and `swiglu` (gate · SiLU + up → down). Applied both inside the layer loop with pre-norm residual connections.

max abs diff:

`3.61832410e-01`

Result:

`FAIL`

### Run 4

Command:

`python check.py`

Change:

Added the per-block PLE inject (`gelu(mm(x, ple_gate)) * ple[:, :, i]` → `ple_proj` → `rmsnorm` → residual), the final `rmsnorm` with `out_norm`, and the tied output head (`x @ tok_emb.T`).

max abs diff:

`5.96046448e-08`

Result:

`PASS`

## Final max abs diff

`5.96046448e-08`

`PASS`

## What I still need to learn

* How RoPE works.
* How PLE helps the model.
* Why the output head uses the token embedding weights.