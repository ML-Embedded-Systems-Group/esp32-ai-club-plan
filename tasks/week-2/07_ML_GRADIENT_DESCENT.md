# An overview of gradient descent optimization algorithms

Member:
Pair/Reviewer:
Assigned date:
Status: Not started

[Back to the Week 2 task intro](00_TASK_INTRO.md) · [Read the mandatory Alexine guide](https://alexine.rip/lab/fix-your-paper-reading-game.html)

## Paper details

- **Year:** 2016
- **Source:** [An overview of gradient descent optimization algorithms](https://arxiv.org/pdf/1609.04747)

## Why it matters

Gradient descent is the basic loop behind training many machine-learning models, but its behavior changes with batch size, learning rate, momentum, and adaptive updates. This overview organizes the main variants and gives a vocabulary for discussing their trade-offs.

It is a useful first pure-ML paper because later methods such as Adam make more sense when their relationship to plain, stochastic, and momentum-based descent is clear. Read it as a map of optimization choices rather than as a recipe to implement.

## Focus questions

- How do batch, stochastic, and mini-batch gradient descent differ in cost and behavior?
- What problem does each major optimization improvement try to solve?
- Which assumptions or comparisons limit how broadly the overview's recommendations apply?

## Suggested reading

Read the Introduction and the sections introducing batch variants, momentum, and adaptive methods. Compare the update equations and any summary tables or convergence plots that show how the methods behave.
