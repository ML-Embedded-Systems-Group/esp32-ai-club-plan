# Attention Is All You Need

**Authors:** [Ashish Vaswani](https://arxiv.org/abs/1706.03762), [Noam Shazeer](https://arxiv.org/abs/1706.03762), [Niki Parmar](https://arxiv.org/abs/1706.03762), [Jakob Uszkoreit](https://arxiv.org/abs/1706.03762), [Llion Jones](https://arxiv.org/abs/1706.03762), [Aidan N. Gomez](https://arxiv.org/abs/1706.03762), [Lukasz Kaiser](https://arxiv.org/abs/1706.03762), and [Illia Polosukhin](https://arxiv.org/abs/1706.03762)

**Source Link:** [arXiv:1706.03762](https://arxiv.org/abs/1706.03762)

---

## Problem / State of the Art

Prior to this paper, standard models for processing language sequences—such as machine translation—relied heavily on Recurrent Neural Networks (RNNs) or Convolutional Neural Networks (CNNs) set up in an encoder-decoder architecture. The main flaw in these existing approaches was sequential processing. Because RNNs read words one step at a time, training could not easily run in parallel. Additionally, capturing relationships between distant words required many steps, making long-range context difficult and computationally expensive to retain.

## Goal

The authors set out to build a simpler, faster network architecture—called the **Transformer**—that processes language sequences without using any recurrent loops or convolution layers. Their target was to create a model that relies entirely on attention mechanisms to learn relationships between words faster and achieve better translation quality.

## Challenges

The main difficulty under the traditional constraints was removing recurrence entirely while still preserving word order and sequence relationships. Sequence models inherently need a way to understand which word comes first, middle, or last without losing context across long sentences, all while keeping computation efficiently parallelizable across modern GPUs.

## Key Mechanism

The central innovation is the **Self-Attention Mechanism** inside an encoder-decoder framework. Instead of stepping through words sequentially, self-attention looks at all words in a sentence simultaneously to calculate how much weight or focus each word should give to every other word. This allows the Transformer to connect distant relationships directly in a single step.

## Key Results

The Transformer established new benchmarks on standard translation tasks while using significantly less computational power:

* **WMT 2014 English-to-German:** Achieved a **28.4 BLEU** score, setting a new record and improving existing ensemble benchmarks by over 2 BLEU points.
* **WMT 2014 English-to-French:** Reached a state-of-the-art **41.8 BLEU** score.
* **Training Efficiency:** The English-to-French model reached these results in just **3.5 days of training on 8 GPUs**, which is a small fraction of the training time and cost required by previous top-performing models.
* **Generalization:** As shown in the paper's experiments on English constituency parsing, the architecture generalized remarkably well to other language-parsing tasks with both small and large datasets.

## Strengths and Improvements

* **Strengths:** Eliminating sequential loops allows full parallelization during training, drastically speeding up learning time while producing superior accuracy.
* **Limitations & Trade-offs:** Because self-attention evaluates all pairs of words simultaneously, the memory required grows quadratically with the length of the input text, making very long sequences challenging without further optimization.

## What I Learned or Liked

It is fascinating how removing complex structures like RNNs and relying strictly on attention simplified the model while drastically improving performance. The realization that position and order can be encoded alongside attention without step-by-step reading fundamentally changed modern artificial intelligence architectures.

## Summary

The paper introduces the Transformer, a novel network architecture built entirely on self-attention mechanisms without recurrence or convolutions. By processing sequence data in parallel rather than step-by-step, it significantly reduces training time while achieving state-of-the-art translation scores on major translation benchmarks.