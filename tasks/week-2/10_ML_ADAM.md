# Adam: A Method for Stochastic Optimization

Member:
Pair/Reviewer:
Assigned date:
Status: Not started

[Back to the Week 2 task intro](00_TASK_INTRO.md) · [Read the mandatory Alexine guide](https://alexine.rip/lab/fix-your-paper-reading-game.html)

## Paper details

- **Year:** 2014
- **Source:** [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)

## Why it matters

Adam combines ideas from momentum and adaptive per-parameter step sizes to make stochastic optimization easier to use across a range of problems. Its update rule became a common baseline, so understanding the paper helps explain a tool often treated as a default.

The paper is valuable for tracing an optimizer from intuition to equations, bias correction, convergence claims, and empirical comparisons. It also invites a careful question: when does an adaptive method's convenience translate into better results?

## Focus questions

- What information do Adam's first- and second-moment estimates keep?
- Why is bias correction needed, especially early in optimization?
- What evidence and assumptions support Adam's claimed advantages over comparison methods?

## Suggested reading

Read the Introduction, the algorithm and theoretical sections, and the experiments. Study Algorithm 1 and the convergence or comparison plots and tables; connect each displayed quantity to the optimizer's behavior.
