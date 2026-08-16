# ESP32 AI Club Plan

Week 1 tasks for the club ML group. The project: replicate the esp32-ai experiment, verify the published results, and build a practical use case.

Base repo: https://github.com/slvDev/esp32-ai

## Repo contents

One file per member. Each file holds that member's week 1 task.

| File | Track | Task |
|---|---|---|
| 01_R1.md | ML research | Loss dynamics study |
| 02_R2.md | ML research | Claims evidence table |
| 03_R3.md | ML research | Mini tokenizer study |
| 04_R4.md | ML research | Run record and analyzer explained |
| 05_R5.md | ML research | Int4 quantizer in numpy |
| 06_H1.md | ML + embedded | Host runtime timing |
| 07_H2.md | ML + embedded | Download checksum verification |
| 08_H3.md | ML + embedded | Export tour |
| 09_H4.md | ML + embedded | Memory budget calc |
| 10_H5.md | ML + embedded | Resume procedure test |
| 11_E1.md | Embedded | Token trace through runtime |
| 12_E2.md | Embedded | Measurement protocol and parser |

## How to use

Every task file has the same shape. Four parts, one week:

1. Part 1: run the full pipeline yourself. Data, training, sampling, quantization, C runtime. You paste every real output into PIPELINE_LOG.md.
2. Part 2: your own depth task. Each member dissects one part of the project and produces a deliverable with real numbers.
3. Part 3: learn the fundamentals with proof. 3Blue1Brown notes, a numpy XOR MLP, a hardest-thing paragraph.
4. Part 4: meetup teach-back. A 10-minute talk with your own numbers.

The evidence checklist at the end of your file is what closes your issue. The lead asks questions from your log, not from memory.

## Project timeline

- Weeks 1-4: host-side replication. No board work.
- Weeks 5-6: hardware verification on the ESP32-S3 N16R8.
- Weeks 7-8: improvise and use case.

## Key resources

- Repo: https://github.com/slvDev/esp32-ai
- RESULTS.md: https://github.com/slvDev/esp32-ai/blob/main/RESULTS.md
- TinyStories paper: https://arxiv.org/abs/2305.07759
- Gemma 3n (PLE): https://ai.google.dev/gemma/docs/gemma-3n
- 3Blue1Brown neural networks: https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi

## Task tracking

Every task has a GitHub issue in this repo, one per member, with a checkbox list. The issue closes when the task is done.

The tracking sheet (Google Sheets, owned by R2) is the single source of truth. It has one tab per week, plus a claims tab.

Sheet columns for task tabs:

| Column | Content |
|---|---|
| Member | R1, R2, ... |
| Task | Short name, e.g. "Loss dynamics study" |
| Issue | Link to the GitHub issue |
| Status | not started / in progress / done / blocked |
| Deliverable link | Link to the file in the repo or Drive |
| Verify result | The number or evidence, e.g. "diff 1e-5" |
| Date | When the status changed |

Rules:

- Each member updates their own rows.
- R2 keeps the sheet clean and reports at the meetup.
- The weekly meetup is the check-in. Blocked tasks get flagged there, not later.

## Code tracking

Each member clones the base repo and works on their own fork.

Workflow:

- One branch per task: `week1/<member>-<task>`, e.g. `week1/r1-loss-dynamics`.
- Code changes go in a pull request to the base repo or the club fork.
- The lead (or R1) reviews and merges. Small PRs only.
- Deliverables that are docs, explainers, scripts, and logs live in this repo (esp32-ai-club-plan), one folder per member, e.g. `deliverables/r1/`.
- Set your own git identity first. Your commits must show your name, not a shared one.

Command to set your identity once per clone:

```
git config user.name "Your Name"
git config user.email "you@example.com"
```
