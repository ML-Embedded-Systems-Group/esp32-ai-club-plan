# ESP32 AI Club Plan

This repository contains the Week 1 task guides and the Week 2 research-paper summary task for the ESP32 AI Club.

The club project studies machine learning on the ESP32-S3. In Week 1, members read a trusted resource, solve a small problem, reproduce the result in code, and write a short report. In Week 2, members read one research paper and write only a short summary.

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

## Submissions

Week 1 reports and reproduction programs live under `submissions/week-1/<task>_<member>/`. Week 2 has one Markdown summary under `submissions/week-2/<paper>_<member>/` and no code.
Task guides live under [`tasks/week-1/`](tasks/week-1/) and [`tasks/week-2/`](tasks/week-2/); do not add submission files beside them.

Current Week 1 submissions:

| Task | Submission |
|---|---|
| R1 | [`submissions/week-1/R1_Raunak/`](submissions/week-1/R1_Raunak/) |
| R2 | [`submissions/week-1/R2_Ritarup/`](submissions/week-1/R2_Ritarup/) |
| R5 | [`submissions/week-1/R5/`](submissions/week-1/R5/) |

Use the same layout under `submissions/week-2/` when Week 2 begins. Every pull request is reviewed before merge.

## Common Report Rules

Use the report name and headings listed in your task file. Write the report by hand in your own words.

Week 1 R and H reports must contain at least 350 words. Week 1 E reports must contain at least 300 words. The Week 2 report body must contain 400–600 words.

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
4. Write and submit only the 400–600 word summary.
5. Complete the evidence checklist and ask your pair to review it.

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
- Week 2: Submit one 400–600 word research-paper summary; no code.
- Weeks 3-4: Reproduce the project on the host.
- Weeks 5-6: Verify results on the ESP32-S3 N16R8.
- Weeks 7-8: Build and test a practical use case.
