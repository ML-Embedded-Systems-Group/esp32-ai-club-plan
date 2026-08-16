# ESP32 AI Club Plan

Week 1 tasks for the club ML group. The project: replicate the esp32-ai experiment, verify the published results, and build a practical use case.

Base repo: https://github.com/slvDev/esp32-ai

## Repo contents

One file per member. Each file holds that member's week 1 task.

| File | Track | Task |
|---|---|---|
| 01_R1.md | ML research | Data setup with prepare.py |
| 02_R2.md | ML research | Verification tracking sheet |
| 03_R3.md | ML research | Training pipeline explainer |
| 04_R4.md | ML research | Analyzer notes |
| 05_R5.md | ML research | Quantization (PTQ) explainer |
| 06_H1.md | ML + embedded | Host golden tests |
| 07_H2.md | ML + embedded | Deploy pipeline doc |
| 08_H3.md | ML + embedded | Export explainer |
| 09_H4.md | ML + embedded | Memory layout map |
| 10_H5.md | ML + embedded | Colab runbook |
| 11_E1.md | Embedded | Toolchain and firmware study |
| 12_E2.md | Embedded | Measurement protocol |

## How to use

1. Open your file.
2. Do the project setup steps first.
3. Finish your task before the weekly meetup.
4. Check the "Done when" list at the end of your file.

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
| Task | Short name, e.g. "Data setup" |
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

Code lives in the club fork of the base repo: https://github.com/slvDev/esp32-ai

Workflow:

- Each member clones the club fork. Never push to main directly.
- One branch per task: `week1/<member>-<task>`, e.g. `week1/r1-data-setup`.
- Code changes go in a pull request to the club fork.
- The lead (or R1) reviews and merges. Small PRs only.
- Docs and explainers live in this repo (esp32-ai-club-plan). Code lives in the fork.
- Set your own git identity first. Your commits must show your name, not a shared one.

Command to set your identity once per clone:

```
git config user.name "Your Name"
git config user.email "you@example.com"
```
