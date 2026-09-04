# Week 3 job 1: tiny PLE forward versus golden

Member: everyone
Time budget: most of the week (about 8 to 12 hours)

## Goal

Write a tiny copy of the project model on your laptop. Make the logits match a frozen golden file.

The project is [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai). The model code is `src/model.py`. That file has RMSNorm, RoPE, causal attention, SwiGLU, Per-Layer Embeddings, and a tied head.

Do not train 28.9 million parameters.
Do not use the board.

The job is complete when:

```text
max abs diff < 1e-5
```

You will fail many times. Run the check. Change one part. Run the check again. Repeat that loop.

## Lab files

Use the files in [`lab/`](lab/).

| File | Role |
|---|---|
| `student_forward.py` | You fill this file. Use NumPy only. |
| `check.py` | This script loads the weights and the golden file. It prints `max abs diff`. |
| `weights.npz`, `idx.npy`, `golden_logits.npy` | Frozen inputs and answers. Do not edit these files. |
| `_make_golden.py` | For the lead only. Do not copy this file into your submission. |

Copy the lab files you need into `submissions/week-3/<member>/`. Keep the `.npz` and `.npy` files unchanged. You can also point `check.py` at `tasks/week-3/lab/`.

## Config (fixed)

```text
arm = ple
vocab_size = 32
d_model = 16
n_layers = 2
n_heads = 2
head_dim = 8
ffn_hidden = 32
seq_len = 8
ple_dim = 8
rope_theta = 10000
```

The head is tied to the token embedding. The arm is `ple` (table plus per-layer mix). Match `TinyLM.forward` in `src/model.py`. Include all of these parts:

- RMSNorm
- RoPE as in `apply_rope` (split the last dim in half; do not interleave)
- causal attention
- SwiGLU (`silu(gate) * up`)
- PLE: `ple_model_proj`, RMSNorm per slice, table `* sqrt(ple_dim)`, mix `* 1/sqrt(2)`
- per-block PLE: `gelu(ple_gate(x)) * ple`, then `ple_proj`, `ple_norm`, then add
- final `out_norm` and tied head

Read `src/model.py` in the project repo. The golden file comes from that path.

## Phase 1: map the forward (1 to 2 hours)

Read these items:

1. The project README memory tiers (SRAM, PSRAM, flash)
2. `src/model.py`: `forward`, `Block.forward`, `param_budget`
3. The docstring in `student_forward.py`

Write a numbered token path in `RUNS.md`: id to embed to PLE to blocks to logits.

## Phase 2: write the code and run the check (6 to 10 hours)

```bash
cd submissions/week-3/<member>
python check.py
```

Fill `forward(weights, idx)` in `student_forward.py`. Use NumPy and the Python standard library only.

Do not import PyTorch in the student file.
Do not load `TinyLM` to make your logits.

Record each run in `RUNS.md`: the command, `max abs diff`, and what you changed. Change one part per run when you can.

## Phase 3: write `RUNS.md` (about 1 hour)

Use these headings:

```markdown
## Token path
## Runs
## Final max abs diff
## What I still need to learn
```

Under **Runs**, list at least four attempts with the printed diff. If the check prints `PASS` but `RUNS.md` has no history, job 1 is not complete.

## Evidence checklist

- [ ] `python check.py` prints `PASS` and `max abs diff` is less than `1e-5`.
- [ ] `student_forward.py` uses NumPy only (no PyTorch).
- [ ] `RUNS.md` has a token path and at least four runs.
- [ ] I did not edit `golden_logits.npy` or `weights.npz`.
- [ ] A pair reviewed the pull request.

## Out of scope

- Firmware flash
- The Hugging Face 28.9M model
- Training
- `_make_golden.py` as your answer
