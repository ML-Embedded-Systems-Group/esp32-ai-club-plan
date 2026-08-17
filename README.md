# ESP32 AI Club Plan

Week 1 tasks for the club ML group. The project: replicate the esp32-ai experiment, verify the published results, and build a practical use case.

Base repo: https://github.com/slvDev/esp32-ai

## Week 1 rule

R and H tracks: read a famous, readable paper, work out its math by hand, reproduce its result in a script, and write a doc in your own words. The E track skips this: they start on the project repo from day one, host-side only, no hardware.

## Repo contents

One file per member. Each file holds that member's week 1 task.

| File | Track | Paper or task | Verify against |
|---|---|---|---|
| 01_R1.md | ML research | Adam: A Method for Stochastic Optimization | Algorithm 1, theta 0.8014 |
| 02_R2.md | ML research | word2vec, Efficient Estimation of Word Representations | softmax sums to 1, shared contexts |
| 03_R3.md | ML research | Sennrich, subword units, BPE | Figure 1 segmentations |
| 04_R4.md | ML research | Srivastava, Dropout | E[x/p] = x |
| 05_R5.md | ML research | Jacob, integer-only quantization | error bound S/2 |
| 06_H1.md | ML + embedded | Kipply, inference arithmetic | the article's tok/s table |
| 07_H2.md | ML + embedded | Latency numbers list | the 200x and 100000x ratios |
| 08_H3.md | ML + embedded | GGUF format spec | the spec's header layout |
| 09_H4.md | ML + embedded | Drepper, memory article | 12.8 and 25.6 GB/s |
| 10_H5.md | ML + embedded | HF, generation strategies | greedy equals argmax |
| 11_E1.md | Embedded | Repo setup and build | tests pass, model fetch works |
| 12_E2.md | Embedded | Repo pipeline trace | one token, file to text |

## How to use

R and H task files have the same shape, four phases, one week. This is the research loop the club trains on every week: read a real result, understand its math, reproduce it in code, write it up.

1. Phase 1, reading: read the assigned paper. Log what it is, 3 things you learned, and 1 question you still have.
2. Phase 2, maths: one problem per task, with a published number to verify. You find the steps. The meetup questions come from here.
3. Phase 3, coding: write a script that reproduces the paper's published numbers. The script output must match the paper.
4. Phase 4, doc generation: write one markdown doc by hand, in your own words, minimum 350 words, with the math steps and the script output. No drawings, no slides, no posters.

E tasks have their own shape: clone the project repo, build it on the host, trace the pipeline, and write a repo map. No hardware this week.

The evidence checklist at the end of your file is what closes your issue. Write everything yourself. Do not paste from any AI tool. Your pair reads your doc before the meetup, and the lead asks you 2 questions from your maths.

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

## Task tracking

Every task has a GitHub issue in this repo, one per member, with a checkbox list. The issue closes when the task is done.

The tracking sheet (Google Sheets, owned by R2) is the single source of truth. It has one tab per week, plus a claims tab.

Sheet columns for task tabs:

| Column | Content |
|---|---|
| Member | R1, R2, ... |
| Task | Short name, e.g. "Big picture explainer" |
| Issue | Link to the GitHub issue |
| Status | not started / in progress / done / blocked |
| Deliverable link | Link to the file in the repo or Drive |
| Verify result | The number or evidence, e.g. "log done" |
| Date | When the status changed |

Rules:

- Each member updates their own rows.
- R2 keeps the sheet clean and reports at the meetup.
- The weekly meetup is the check-in. Blocked tasks get flagged there, not later.

## Code tracking

Week 1 has no code. From week 2, each member clones the base repo and works on their own fork.

Workflow:

- One branch per task: `week2/<member>-<task>`, e.g. `week2/r1-loss-dynamics`.
- Code changes go in a pull request to the base repo or the club fork.
- The lead (or R1) reviews and merges. Small PRs only.
- Deliverables that are docs, explainers, scripts, and logs live in this repo, one folder per member, e.g. `deliverables/r1/`.
- Set your own git identity first. Your commits must show your name, not a shared one.

Command to set your identity once per clone:

```
git config user.name "Your Name"
git config user.email "you@example.com"
```
