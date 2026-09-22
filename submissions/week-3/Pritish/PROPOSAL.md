## Topic
3. Keep ple, or try fatembed or bigcore, for one use case (src/model.py arms).

## Problem (in this repo)
The repository explores alternative structural embedding arms in `src/model.py`, specifically comparing Positional Lookup Embedding (`ple`) against broader or alternative lookup structures like `fatembed`. While `ple` efficiently factorizes position lookup through a shared table across layers, it introduces auxiliary block-wise projection gates and matrix multiplication overhead during forward execution. On a memory-constrained microcontroller architecture like the ESP32, these extra projection steps increase operational complexity and instruction counts per token generated.

## What I would change
I propose an experiment to switch the model architecture arm in `src/model.py` from the current `ple` implementation to the `fatembed` alternative for the TinyStories generation use case. This replaces the layer-wise factorized PLE projection gates with a wider, direct embedding strategy while keeping core transformer hyperparameters (such as `d_model=16` and `n_layers=2`) constant to maintain parity with the baseline memory envelope.

## How I would know it worked
I will evaluate success using two concrete metrics:
1. **Inference Latency:** Measure tokens per second on the ESP32 target to see if removing the auxiliary PLE gating layers reduces compute overhead.
2. **Perplexity / Generation Quality:** Calculate validation loss on the TinyStories test split to determine whether the simpler `fatembed` architecture preserves text generation quality compared to `ple`.

A successful experiment will show lower execution latency with a negligible change in text generation perplexity.

## Memory / size risk
- **SRAM / PSRAM:** Moving from `ple` to `fatembed` alters how embedding tensors are indexed and stored. While `ple` utilizes a factorized table (`32 x 16`), `fatembed` changes the parameter width distribution across the SRAM/PSRAM boundary.
- **Risk:** The primary risk is that widening the embedding table directly could increase static memory pressure or cache misses during token lookups on the ESP32-S3 chip, potentially negating any compute savings gained by removing the projection gates.

## Sources
1. Project File: `src/model.py` (Contains the structural definitions and arm implementations for `ple`, `fatembed`, and `bigcore`).
2. Project File: `RESULTS.md` (Tracks architectural performance and memory constraint thresholds).
3. Project File: `tasks/week-3/lab/00_TASK_INTRO.md` (Details the lab configuration and target microcontroller hardware limits).