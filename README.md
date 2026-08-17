# ESP32 AI Club Plan

Week 1 tasks for the club ML group. The project: replicate the esp32-ai experiment, verify the published results, and build a practical use case.

Base repo: https://github.com/slvDev/esp32-ai

## Week 1 rule

R and H tracks: read a short, readable resource, work out its math by hand, reproduce its result in a script, and write a doc in your own words. The R track moves from ML fundamentals to neural network fundamentals, one step per member. The E track skips this: they start on the project repo from day one, host-side only, no hardware.

## Repo contents

One file per member. Each file holds that member's week 1 task.

| File | Track | Paper or task | Verify against |
|---|---|---|---|
| 01_R1.md | ML research | CS229 probability review | Bayes: P(A1 given B1) = 0.333 |
| 02_R2.md | ML research | Gradient descent in linear regression | recover y = 3x + 5 |
| 03_R3.md | ML research | Logistic regression, MLU Explain | all 6 points classified |
| 04_R4.md | ML research | Nielsen ch. 1, sigmoid neurons | sigma(0.2) = 0.550 |
| 05_R5.md | ML research | Backpropagation, GfG | the network learns AND |
| 06_H1.md | ML + embedded | Floating point, visually explained | 3.5 is 0x40600000 |
| 07_H2.md | ML + embedded | Interactive latency numbers | the 200x and 100000x ratios |
| 08_H3.md | ML + embedded | Little and big endian | bytes 78 56 34 12 |
| 09_H4.md | ML + embedded | Bandwidth vs latency | 12.8 and 25.6 GB/s |
| 10_H5.md | ML + embedded | Softmax function | 0.090, 0.245, 0.665 |
| 11_E1.md | Embedded | Repo setup and build | tests pass, model fetch works |
| 12_E2.md | Embedded | Repo pipeline trace | one token, file to text |

## How to use

R and H task files have the same shape, four phases, one week. This is the research loop the club trains on every week: read a real result, understand its math, reproduce it in code, write it up.

1. Phase 1, reading: read the assigned paper or article. Log what it is, 3 things you learned, and 1 question you still have.
2. Phase 2, maths: one problem per task, with a published number to verify. You find the steps.
3. Phase 3, coding: write a script that reproduces the paper's published numbers. The script output must match the paper.
4. Phase 4, doc generation: write one markdown doc by hand, in your own words, minimum 350 words, with the math steps and the script output. No drawings, no slides, no posters.

E tasks have their own shape: clone the project repo, build it on the host, trace the pipeline, and write a repo map. No hardware this week.

The evidence checklist at the end of your file is what closes your issue. Write everything yourself. Do not paste from any AI tool. Your pair reads your doc and verifies your checklist.

## Project timeline

- Week 1: fundamentals for R and H. E starts repo work.
- Weeks 2-4: host-side replication.
- Weeks 5-6: hardware verification on the ESP32-S3 N16R8.
- Weeks 7-8: improvise and use case.

## Key resources

- Repo: https://github.com/slvDev/esp32-ai
- RESULTS.md: https://github.com/slvDev/esp32-ai/blob/main/RESULTS.md
- TinyStories paper: https://arxiv.org/abs/2305.07759
- Gemma 3n (PLE): https://ai.google.dev/gemma/docs/gemma-3n
