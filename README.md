# ESP32 AI Club Plan

Week 1 tasks for the club ML group. The project: replicate the esp32-ai experiment, verify the published results, and build a practical use case.

Base repo: https://github.com/slvDev/esp32-ai

## Week 1 rule

No code. No cloning. No accounts. Everyone reads the fundamentals first, keeps a reading log, and makes one small deliverable. Repo work starts in week 2.

## Repo contents

One file per member. Each file holds that member's week 1 task.

| File | Track | Task |
|---|---|---|
| 01_R1.md | ML research | Big picture explainer |
| 02_R2.md | ML research | Glossary of 20 terms |
| 03_R3.md | ML research | Tokenization hands-on |
| 04_R4.md | ML research | Loss and perplexity |
| 05_R5.md | ML research | Why quantize |
| 06_H1.md | ML + embedded | Model to device flow |
| 07_H2.md | ML + embedded | Memory tiers |
| 08_H3.md | ML + embedded | The model file |
| 09_H4.md | ML + embedded | What tok/s means |
| 10_H5.md | ML + embedded | Inside the runtime |
| 11_E1.md | Embedded | The board |
| 12_E2.md | Embedded | Firmware 101 |

## How to use

Every task file has the same shape, three parts, one week.

1. Part 1: read the given links in order. For each source, log what it is, 3 things you learned, and 1 question you still have.
2. Part 2: make your deliverable. One small file per member, with real numbers from the repo where they exist.
3. Part 3: meetup teach-back. 5 minutes, then 2 questions from the lead.

The evidence checklist at the end of your file is what closes your issue. Write everything yourself. The meetup questions will show the difference.

## Project timeline

- Week 1: fundamentals. No repo work.
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
