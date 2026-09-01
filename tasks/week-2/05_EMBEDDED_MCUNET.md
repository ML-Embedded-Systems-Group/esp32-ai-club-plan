# MCUNet: Tiny Deep Learning on IoT Devices

Member:
Pair/Reviewer:
Assigned date:
Status: Not started

[Back to the Week 2 task intro](00_TASK_INTRO.md) · [Read the mandatory Alexine guide](https://alexine.rip/lab/fix-your-paper-reading-game.html)

## Paper details

- **Year:** 2020
- **Source:** [MCUNet: Tiny Deep Learning on IoT Devices](https://arxiv.org/abs/2007.10319)

## Why it matters

Many neural networks are designed for hardware far more capable than a microcontroller. MCUNet treats the model architecture and the inference engine as a joint design problem, aiming to make useful deep learning fit within the memory and latency limits of IoT devices.

Read it to understand why optimizing only the network or only the runtime can leave performance on the table. The paper connects neural architecture search with a purpose-built engine for end-to-end TinyML deployment.

## Focus questions

- What makes the joint model-and-engine problem different from ordinary model compression?
- How do TinyNAS and TinyEngine divide the work of fitting inference to a microcontroller?
- Which experiments demonstrate improvements in accuracy, memory, latency, or feasibility?

## Suggested reading

Read the Introduction, the TinyNAS and TinyEngine method sections, and the deployment experiments. Study the system diagrams, architecture-search figures, and tables comparing memory, latency, and accuracy with prior approaches.
