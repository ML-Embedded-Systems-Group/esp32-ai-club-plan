## Topic
4. A smaller or factorized output head

## Problem (in this repo)
The shipping runtime is PSRAM-bandwidth-bound in the output head. RESULTS.md's on-chip profile shows the head costing 57.6ms of the 102.9ms per-token step, because it reads about 2.43MB of int8 weights from PSRAM every single token at a measured 60.7MB/s, a roughly 40ms floor that dominates the step. Int8 activations already shipped and closed most of the compute-side gap; RESULTS.md itself names a smaller or factorized output head, not further SIMD work, as the next lever, since SIMD alone is capped near 15%. The head is the tied embedding, d_model (96) by vocab (32,768), about 3.1M parameters, the only large tensor read sequentially every token instead of through the PLE table's sparse per-token row lookups.

## What I would change
Factorize the output projection into two stages: d_model (96) to a bottleneck d_rank, then d_rank up to vocab (32,768). Starting point d_rank = 32. W_A is 96 x 32 = 3,072 parameters, small enough to live permanently in internal SRAM. W_B is 32 x 32,768 = 1,048,576 parameters, replacing the 3.1M-parameter head with roughly a third of the bytes read per token. I would train this jointly with the core on the host, using the existing TinyStories setup, keeping the transformer blocks and PLE arms unchanged. One open design question I would resolve early: the current head is weight-tied to `tok_emb`. A rank-32 projection cannot share that exact tie, so the experiment needs to either accept an untied head or find a partial-tying scheme, and that choice affects the real parameter budget.

## How I would know it worked
Two metrics on the host harness:
1. Validation perplexity should not regress by more than about 0.05 to 0.1 nats against the PLE headline of 11.41 ppl in RESULTS.md.
2. Head bytes read per token should drop by roughly two-thirds (about 3.1M to about 1.05M parameters), which at the measured 60.7MB/s PSRAM bandwidth should cut the head's ~40ms floor to roughly 13 to 14ms, the largest single lever RESULTS.md's own profiling points at.

## Memory / size risk
W_A is trivial and stays resident in SRAM with no bandwidth cost. W_B still lives in PSRAM or flash, just smaller. The real risk is that breaking the tok_emb tie could increase, not decrease, total resident parameters: if `tok_emb` must still exist separately for input lookups, the true footprint becomes tok_emb (3.1M) plus W_A and W_B (about 1.05M), which is worse than today unless a tying scheme is found. The second risk is capacity: a rank-32 bottleneck may not separate 32,768 tokens well enough, which would show up as repetitive or degenerate greedy generations even if perplexity looks acceptable on aggregate.

## Sources
- slvDev/esp32-ai `RESULTS.md`: the on-chip profile (head 57.6ms of 102.9ms/step), the 2.43MB/token PSRAM read figure, and the explicit note that a factorized/smaller head is the next lever over SIMD.
- slvDev/esp32-ai headline config in `RESULTS.md`: d_model=96, vocab=32,768, 6 layers, confirming the real head size (~3.1M params) used above.
- My own job 1 result: verified in `student_forward.py`/`_make_golden.py` that the head is implemented as `x @ tok_emb.T`, i.e. genuinely weight-tied, which is what motivates the tying risk above.
