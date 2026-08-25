# TensorFlow Lite Micro: Embedded Machine Learning on TinyML Systems

Member:
Pair/Reviewer:
Assigned date:
Status: Not started

[Back to the Week 2 task intro](00_TASK_INTRO.md) · [Read the mandatory Alexine guide](https://alexine.rip/lab/fix-your-paper-reading-game.html)

## Paper details

- **Year:** 2020
- **Source:** [TensorFlow Lite Micro: Embedded Machine Learning on TinyML Systems](https://arxiv.org/abs/2010.08678)

## Why it matters

TinyML needs inference on devices with very little memory, compute, and power. This paper explains the design of TensorFlow Lite Micro, a runtime that brings machine-learning inference to embedded systems without assuming an operating system or a large heap.

Read it to see how a deployment runtime turns a trained model into something that can run predictably on constrained hardware, and what engineering trade-offs make embedded ML practical.

## Focus questions

- Which constraints distinguish embedded inference from desktop or mobile inference?
- How do the runtime architecture and memory-planning choices address those constraints?
- What evidence shows the runtime is usable across supported microcontroller systems?

## Suggested reading

Read the abstract, Introduction, runtime/system-design sections, and evaluation. Pay attention to the architecture or memory-planning figures and the tables reporting model size, memory use, latency, or supported platforms.
