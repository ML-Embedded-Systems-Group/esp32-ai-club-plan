# ESP32 AI Club Plan

This repository contains the task guides for the ESP32 AI Club.

The club project studies machine learning on the ESP32-S3. Week 1 is one assigned idea, maths, a small script, and a report. Week 2 is one 400 to 600 word paper summary and no code. Week 3 is two jobs for every member: match a tiny host model to a golden file, then propose one later experiment.

## Week 1 Goals

By the end of Week 1, each member must:

1. Explain the assigned idea in their own words.
2. Show the assigned maths step by step.
3. Write and run the assigned reproduction script.
4. Record the script output in a Markdown report.
5. Ask their pair to review the report.

Do not copy text or code from an AI tool. Use the resources as study material.

## Week 1 Task Files

| File | Track | Topic | Main result |
|---|---|---|---|
| [`01_R1.md`](tasks/week-1/01_R1.md) | ML research | Probability | `P(B1) = 0.6`, `P(A1 given B1) = 0.333` |
| [`02_R2.md`](tasks/week-1/02_R2.md) | ML research | Gradient descent | Recover `y = 3x + 5` |
| [`03_R3.md`](tasks/week-1/03_R3.md) | ML research | Logistic regression | Classify all 6 points |
| [`04_R4.md`](tasks/week-1/04_R4.md) | ML research | Sigmoid neurons | `sigma(0.2) = 0.550` |
| [`05_R5.md`](tasks/week-1/05_R5.md) | ML research | Backpropagation | Learn the AND rule |
| [`06_H1.md`](tasks/week-1/06_H1.md) | ML and embedded | Floating point | `3.5 = 0x40600000` |
| [`07_H2.md`](tasks/week-1/07_H2.md) | ML and embedded | Latency | Reproduce the listed ratios |
| [`08_H3.md`](tasks/week-1/08_H3.md) | ML and embedded | Endianness | Show `78 56 34 12` |
| [`09_H4.md`](tasks/week-1/09_H4.md) | ML and embedded | Bandwidth | Reproduce `12.8` and `25.6 GB/s` |
| [`10_H5.md`](tasks/week-1/10_H5.md) | ML and embedded | Softmax | Reproduce `0.090`, `0.245`, `0.665` |
| [`11_E1.md`](tasks/week-1/11_E1.md) | Embedded | Repository setup | Run tests and fetch a model |
| [`12_E2.md`](tasks/week-1/12_E2.md) | Embedded | Pipeline trace | Follow one token to text |

## Week 2 Task

Read [`tasks/week-2/00_TASK_INTRO.md`](tasks/week-2/00_TASK_INTRO.md) before choosing a paper. Week 2 has no coding or reproduction work: submit only one **400–600 word research-paper summary**. The Week 2 folder has one assignment intro, one resources file with teasers, and one guide file for each of the ten papers.

### Week 2 Guides

| File | Purpose |
|---|---|
| [`00_TASK_INTRO.md`](tasks/week-2/00_TASK_INTRO.md) | Assignment coverage, report format, and checklist |
| [`01_RESOURCES.md`](tasks/week-2/01_RESOURCES.md) | Background resources with short teasers |
| [`02_EMBEDDED_TFLM.md`](tasks/week-2/02_EMBEDDED_TFLM.md) | TensorFlow Lite Micro |
| [`03_EMBEDDED_PLATFORMS.md`](tasks/week-2/03_EMBEDDED_PLATFORMS.md) | TinyML Platforms Benchmarking |
| [`04_EMBEDDED_MLPERF.md`](tasks/week-2/04_EMBEDDED_MLPERF.md) | MLPerf Tiny Benchmark |
| [`05_EMBEDDED_MCUNET.md`](tasks/week-2/05_EMBEDDED_MCUNET.md) | MCUNet |
| [`06_EMBEDDED_TINYTL.md`](tasks/week-2/06_EMBEDDED_TINYTL.md) | TinyTL |
| [`07_ML_GRADIENT_DESCENT.md`](tasks/week-2/07_ML_GRADIENT_DESCENT.md) | Gradient-descent optimization |
| [`08_ML_NUMPY.md`](tasks/week-2/08_ML_NUMPY.md) | NumPy array foundations |
| [`09_ML_GLOROT.md`](tasks/week-2/09_ML_GLOROT.md) | Training deep feedforward networks |
| [`10_ML_ADAM.md`](tasks/week-2/10_ML_ADAM.md) | Adam optimization |
| [`11_ML_TRANSFORMER.md`](tasks/week-2/11_ML_TRANSFORMER.md) | Attention and Transformers |

## Week 3 tasks

Read [`tasks/week-3/00_TASK_INTRO.md`](tasks/week-3/00_TASK_INTRO.md) first. Every member does both jobs. You can use an AI helper. You must run the commands yourself.

| File | Job |
|---|---|
| [`00_TASK_INTRO.md`](tasks/week-3/00_TASK_INTRO.md) | Both jobs, submit path, work order |
| [`01_GOLDEN.md`](tasks/week-3/01_GOLDEN.md) | Tiny PLE forward versus golden (`max abs diff < 1e-5`) |
| [`02_PROPOSAL.md`](tasks/week-3/02_PROPOSAL.md) | One experiment note, plus a 3 to 5 minute talk in the weekly meet |
| [`lab/`](tasks/week-3/lab/) | Starter, `check.py`, frozen weights and logits |

## Submissions

Week 1 reports and reproduction programs live under `submissions/week-1/<task>_<member>/`. Week 2 has one Markdown summary under `submissions/week-2/<paper>_<member>/` and no code. Week 3 files live under `submissions/week-3/<member>/` (`student_forward.py`, `RUNS.md`, `PROPOSAL.md`).
Task guides live under [`tasks/week-1/`](tasks/week-1/), [`tasks/week-2/`](tasks/week-2/), and [`tasks/week-3/`](tasks/week-3/). Do not add submission files beside the guides.

Current Week 1 submissions:

| Task | Submission |
|---|---|
| R1 | [`submissions/week-1/R1_Raunak/`](submissions/week-1/R1_Raunak/) |
| R2 | [`submissions/week-1/R2_Ritarup/`](submissions/week-1/R2_Ritarup/) |
| R5 | [`submissions/week-1/R5/`](submissions/week-1/R5/) |

Use the same layout under `submissions/week-2/` when Week 2 begins. Every pull request is reviewed before merge.

## Common Report Rules

Use the report name and headings listed in your task file. Write the report by hand in your own words.

Week 1 R and H reports must contain at least 350 words. Week 1 E reports must contain at least 300 words. The Week 2 report body must contain 400 to 600 words. The Week 3 `PROPOSAL.md` body must contain 400 to 600 words.

Each Week 1 report must contain the resource summary, the maths or code evidence, the output, and the unanswered questions.

Week 2 reports contain paper evidence and one limitation or open question instead. They must not contain code, notebooks, model files, plots, or benchmark output.

Use code blocks for commands and script output. Label each output with the command that produced it.

## Week 1 Common Work Order

1. Read the assigned resource.
2. Write a short summary without copying the source.
3. Solve the maths by hand.
4. Write the reproduction script.
5. Run the script and record its output.
6. Write the report.
7. Complete the evidence checklist.
8. Ask your pair to review the report.

## Week 2 Work Order

1. Read the mandatory paper-reading guide in [`tasks/week-2/00_TASK_INTRO.md`](tasks/week-2/00_TASK_INTRO.md).
2. Choose one paper from the embedded/TinyML or pure-ML list.
3. Annotate the paper using the guide's prompts.
4. Write and submit only the 400 to 600 word summary.
5. Complete the evidence checklist and ask your pair to review it.

## Week 3 work order

1. Read [`tasks/week-3/00_TASK_INTRO.md`](tasks/week-3/00_TASK_INTRO.md).
2. Copy the lab starter and run `python check.py` until `max abs diff` is less than `1e-5`. Record runs in `RUNS.md`.
3. Write `PROPOSAL.md` from the closed topic list.
4. Open a pull request. Ask your pair to review it.
5. In the weekly meet, speak for 3 to 5 minutes about how you reached the proposal.

## Project Resources

- Project repository: https://github.com/slvDev/esp32-ai
- Published results: https://github.com/slvDev/esp32-ai/blob/main/RESULTS.md
- TinyStories paper: https://arxiv.org/abs/2305.07759
- Gemma 3n PLE: https://ai.google.dev/gemma/docs/gemma-3n

## Extra Reading

- ESP32-S3 technical reference: https://www.espressif.com/sites/default/files/documentation/esp32-s3_technical_reference_manual_en.pdf
- TinyML overview: https://www.tensorflow.org/lite/microcontrollers
- Hugging Face NLP course: https://huggingface.co/learn/nlp-course/chapter1/1

## Timeline

- Week 1: Complete the assigned fundamentals or repository task.
- Week 2: Submit one 400 to 600 word research-paper summary; no code.
- Week 3: Match a tiny host model to a golden file, and propose one later experiment (talk in the weekly meet).
- Weeks 3-4: Reproduce the project on the host (week 3 is the first host slice).
- Weeks 5-6: Verify results on the ESP32-S3 N16R8.
- Weeks 7-8: Build and test a practical use case.
