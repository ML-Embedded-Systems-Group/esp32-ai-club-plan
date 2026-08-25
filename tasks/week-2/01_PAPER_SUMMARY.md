# Week 2: Research-paper summary

Week 2 has one task: write a **400–600 word summary of one research paper** from the lists below. This is a reading and writing task only. Submit one Markdown report; do not submit code, notebooks, model files, plots, benchmarks, or downloaded papers.

## Mandatory paper-reading guide: read this first

Before opening a paper, every student must read [Fix your paper reading game](https://alexine.rip/lab/fix-your-paper-reading-game.html). Follow its annotation approach while reading: set the stage with a paper copy or tablet, then identify the problem/state of the art, goal, challenges, key mechanism, key results, strengths, improvements, what you learned or liked, and a short summary in your own words. Keep those notes; they are the evidence for the report. Do not treat the abstract alone as a paper reading.

## Embedded and TinyML papers

Choose one paper from this list. The sequence moves from a small inference runtime to measurement, system design, and on-device learning.

1. [TensorFlow Lite Micro: Embedded Machine Learning on TinyML Systems](https://arxiv.org/abs/2010.08678)
2. [TinyML Platforms Benchmarking](https://arxiv.org/abs/2112.01319)
3. [MLPerf Tiny Benchmark](https://arxiv.org/abs/2106.07597)
4. [MCUNet: Tiny Deep Learning on IoT Devices](https://arxiv.org/abs/2007.10319)
5. [TinyTL: Reduce Activations, Not Trainable Parameters for Efficient On-Device Learning](https://arxiv.org/abs/2007.11622)

## Pure-ML papers

Choose one paper from this list. Read them in order if you want a progression from optimization and numerical foundations to neural-network training and attention. The fifth paper is the endpoint of this sequence.

1. [An overview of gradient descent optimization algorithms](https://arxiv.org/pdf/1609.04747)
2. [The NumPy array: a structure for efficient numerical computation](https://arxiv.org/pdf/1102.1523)
3. [Understanding the difficulty of training deep feedforward neural networks](https://proceedings.mlr.press/v9/glorot10a.html)
4. [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980)
5. [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

## Learning ladder

Read or use these resources in this order, moving from neural-network intuition toward research papers:

1. **Accessible overview of ML, neural networks, deep learning, tokenization, training, and transformers:** [Leerob — AI](https://leerob.com/ai)
2. [Arjun Virk — ML Guide](https://www.arjunvirk.com/writing/ml-guide)
3. [Aman AI — AI Primers](https://aman.ai/primers/ai/)
4. [Alisa's Book of LLMs](https://alisawuffles.notion.site/alisa-s-book-of-llms)
5. [Aleksa Gordic — Blog](https://www.aleksagordic.com/blog)
6. **Main intuition resource: [Colah's blog](https://colah.github.io/)**

Use these previously bookmarked resources when a paper assumes background you do not yet have:

- [Dive into Deep Learning (D2L)](https://d2l.ai/)
- [Stanford CS231n notes](https://cs231n.github.io/)
- [Stanford CS224N](https://web.stanford.edu/class/cs224n/)
- [Understanding Deep Learning](https://udlbook.github.io/udlbook/)
- [The Annotated Transformer](https://nlp.seas.harvard.edu/2018/04/03/attention.html)
- [Let's build GPT from scratch](https://www.youtube.com/watch?v=kCc8FmEb1nY)

These are supports, not extra assignments. Stop when you have enough context to explain the selected paper clearly.

## Embedded-paper supplements

Use a supplement only to clarify a paper's setting, terminology, or deployment path. Supplements do not replace the mandatory paper-reading guide or the selected paper.

- **Accessible — LiteRT for Microcontrollers overview:** [Google AI Edge documentation](https://ai.google.dev/edge/litert/microcontrollers/overview)
- **Accessible — TensorFlow Lite for Microcontrollers documentation:** [TensorFlow developer guide](https://www.tensorflow.org/lite/microcontrollers)
- **Accessible — MLPerf Tiny benchmark resources:** [MLCommons Tiny benchmark](https://mlcommons.org/working-groups/benchmarks/tiny/) and [the reference repository](https://github.com/mlcommons/tiny)
- **Accessible — TinyML walkthrough:** [Digi-Key video: TinyML with TensorFlow Lite for Microcontrollers](https://www.youtube.com/watch?v=gDFWCxrJruQ)
- **Accessible — implementation practice:** [TinyTorch getting started](https://mlsysbook.ai/tinytorch/getting-started.html) and [MLSysBook](https://www.mlsysbook.ai/)
- **Optional / advanced — video:** [MIT HAN Lab MCUNet lecture](https://www.youtube.com/watch?v=YBER-SNlkqs)

## Assignment

1. Read the mandatory paper-reading guide first.
2. Choose exactly one paper from either list and annotate it using the guide's prompts.
3. Use the learning ladder or an embedded supplement only when it helps you understand the selected paper.
4. Write one 400–600 word report in your own words. Include the paper title, authors, and link.
5. Submit only the Markdown report under `submissions/week-2/<paper>_<member>/`.

## Report headings

Use these headings. The report body must be 400–600 words; headings, paper metadata, and the source link do not count toward the limit.

```markdown
## Problem / State of the Art
## Goal
## Challenges
## Key Mechanism
## Key Results
## Strengths and Improvements
## What I Learned or Liked
## Summary
```

Keep the summary concrete: name the evidence you used (for example, a section, table, figure, or result) and explain one trade-off or limitation. Do not paste an abstract or copy sentences from the paper or supplements.

## Evidence checklist

- [ ] The mandatory paper-reading guide was read before the selected paper.
- [ ] The report identifies exactly one paper, its authors, and its source link.
- [ ] Notes cover problem/state of the art, goal, challenges, mechanism, results, strengths, improvements, learning, and summary.
- [ ] The report body is between 400 and 600 words.
- [ ] At least one claim is tied to a paper section, figure, table, or reported result.
- [ ] The report states one limitation, trade-off, or improvement.
- [ ] The writing is in the student's own words.
- [ ] No code, notebook, model, plot, benchmark output, or downloaded artifact is submitted.
