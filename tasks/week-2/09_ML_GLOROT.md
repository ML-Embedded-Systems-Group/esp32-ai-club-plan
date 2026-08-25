# Understanding the difficulty of training deep feedforward neural networks

Member:
Pair/Reviewer:
Assigned date:
Status: Not started

[Back to the Week 2 task intro](00_TASK_INTRO.md) · [Read the mandatory Alexine guide](https://alexine.rip/lab/fix-your-paper-reading-game.html)

## Paper details

- **Year:** 2010
- **Source:** [Understanding the difficulty of training deep feedforward neural networks](https://proceedings.mlr.press/v9/glorot10a.html)

## Why it matters

Deep networks can be difficult to train when signals or gradients become too small or too large as they pass through layers. This paper analyzes that difficulty and motivates initialization choices that keep forward activations and backward gradients better behaved.

Read it to connect an abstract training failure to the practical question of how weights should be initialized. The analysis also provides a foundation for understanding why depth, activation functions, and variance interact.

## Focus questions

- What causes signal or gradient saturation and instability in deep feedforward networks?
- What does the proposed initialization aim to preserve across layers?
- Which theoretical or experimental evidence supports the paper's explanation, and where does it stop applying?

## Suggested reading

Read the Introduction, the theoretical analysis, and the experiments. Pay attention to figures showing activation or gradient behavior across depth and tables comparing initialization or training outcomes.
