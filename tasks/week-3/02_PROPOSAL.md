# Week 3 job 2: one experiment proposal

Member: everyone
Time budget: a few hours for the note, plus 3 to 5 minutes in the weekly meet

## Goal

Propose one later experiment for this club. The change is a small change to [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) after the host path is reproduced.

This job is not a week 2 paper summary. You pick one fork of this project. You say how you will measure it.

## Closed topic list

Choose exactly one topic:

1. Different training text instead of TinyStories (name the corpus, the size, and the metric).
2. Barista-style Q and A versus stories ([models](https://github.com/slvDev/esp32-ai#models)).
3. Keep `ple`, or try `fatembed` or `bigcore`, for one use case (`src/model.py` arms).
4. A smaller or factorized output head ([RESULTS.md](https://github.com/slvDev/esp32-ai/blob/main/RESULTS.md) says the head uses most of the bandwidth).
5. Vocabulary size (4k versus 32k) as a design choice.
6. Int4 head and SIMD versus the current int8 head (named in RESULTS.md).
7. Interactive serial prompt (listed under Next in RESULTS.md).
8. What must stay in SRAM, PSRAM, or flash for one change that you care about.
9. One on-device task (short FAQ or log phrases) and whether a TinyStories-sized core can do it.

You can use an AI helper to search and to draft. You must open the sources yourself.

Cut any plan that does not fit the chip: about 559K dense core, 25M flash table, TinyStories-level skill.

## What to write (`PROPOSAL.md`)

The body is 400 to 600 words. Headings, links, and the topic number do not count in that limit.

```markdown
## Topic
## Problem (in this repo)
## What I would change
## How I would know it worked
## Memory / size risk
## Sources
```

Topic: write the number and the name from the list.

Problem: write what is missing or hard in this project. Do not write a general ML complaint.

What I would change: write one experiment. Do not write a long program of work.

How I would know it worked: write one metric (for example host ppl, greedy text, or size in flash).

Memory / size risk: write SRAM, PSRAM, flash, or core versus table versus stream.

Sources: write 2 or 3 links that you opened, plus one fact from this project (`RESULTS.md`, `src/model.py`, `param_budget`, or a number from job 1).

Do not write a long "how I reached this" section. You speak that part in the meet.

## Weekly meet (required)

Job 2 is complete only after you explain the path in the weekly meet. Speak for about 3 to 5 minutes. Do not read a script.

Say these points in this order:

1. What you thought at first.
2. What you opened or ran (a paper, RESULTS.md, or a job 1 number).
3. What made you keep this idea.
4. One idea that you dropped, and why.
5. The experiment in one sentence.

If you used an AI helper, say what it suggested. Then say what you kept or cut after you checked a source. Do not show the chat.

If you cannot explain the path in the meet, the write-up is not enough.

## Evidence checklist

- [ ] I picked exactly one topic from the list.
- [ ] `PROPOSAL.md` is 400 to 600 words and uses the headings above.
- [ ] At least one claim cites this project (a file or a number).
- [ ] The idea is one experiment that can fit the ESP32 memory split.
- [ ] I started job 1 (at least two runs in `RUNS.md`).
- [ ] A pair reviewed the note.
- [ ] I explained how I reached the conclusion in the weekly meet (3 to 5 minutes).

## Out of scope

- A large cloud model on the chip
- An AI research program pasted as your own
- Code, notebooks, or plots for job 2
- A Markdown file with no meet talk
