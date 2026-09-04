# Week 3: host match and one proposal

Each member does the same two jobs. The week 1 tracks (R, H, E) do not split this work.

You can use an AI helper. You must run each command yourself.

Job 1 is complete only when `max abs diff` is less than `1e-5`. You will run the check many times.

## The two jobs

1. [Match a tiny model to a golden file](01_GOLDEN.md). This job takes most of the week.
2. [Propose one later experiment](02_PROPOSAL.md). This job takes a few hours. In the weekly meet, you say how you reached the idea.

Read both guides before you start.

Do not flash a board this week.
Do not train the full TinyStories model this week.

## What you submit

Put your files in `submissions/week-3/<member>/`.

| File | Job |
|---|---|
| `student_forward.py` | Your NumPy forward (job 1) |
| `RUNS.md` | Commands and `max abs diff` after each run (job 1) |
| `PROPOSAL.md` | One experiment, 400 to 600 words (job 2) |

Job 2 is complete only after you speak in the weekly meet. Do not write a long "how I reached this" section in the file.

## Work order

1. Read this file and the two task guides.
2. Copy the starter from [`lab/`](lab/).
3. Run `python check.py` until `max abs diff` is less than `1e-5`.
4. Record each run in `RUNS.md`.
5. Write `PROPOSAL.md`. Use one topic from the closed list.
6. Open a pull request.
7. In the weekly meet, speak for 3 to 5 minutes about how you reached the proposal.

You can submit the proposal before job 1 prints `PASS`. You must start job 1 first. Record at least two runs so the proposal stays tied to this project.

## Out of scope

- ESP-IDF, flash, and ESP32-S3 measurements
- Full TinyStories training and Barista training
- A second week 2 paper summary
- A new large architecture
