# TinyTL: Reduce Activations, Not Trainable Parameters for Efficient On-Device Learning

Member:
Pair/Reviewer:
Assigned date:
Status: Not started

[Back to the Week 2 task intro](00_TASK_INTRO.md) · [Read the mandatory Alexine guide](https://alexine.rip/lab/fix-your-paper-reading-game.html)

## Paper details

- **Year:** 2020
- **Source:** [TinyTL: Reduce Activations, Not Trainable Parameters for Efficient On-Device Learning](https://arxiv.org/abs/2007.11622)

## Why it matters

On-device learning is harder than inference because training usually needs large activation buffers and more memory. TinyTL proposes a way to adapt a model on a small device by reducing activation storage while keeping the trainable-parameter budget practical.

The paper matters because it questions the usual instinct to freeze or shrink parameters first. It shows how the choice of what to store during backpropagation can determine whether local personalization is feasible.

## Focus questions

- Why are activations, rather than only trainable parameters, the key memory bottleneck?
- What is the central TinyTL design and how does it preserve useful adaptation?
- How do the experiments compare memory use and accuracy with parameter-efficient or full fine-tuning baselines?

## Suggested reading

Read the motivation, method, and experimental sections. Focus on the diagrams explaining the training path and the tables or ablations that compare activation memory, trainable parameters, and task accuracy.
