# Understanding the difficulty of training deep feedforward neural networks

**Paper:** *Understanding the difficulty of training deep feedforward neural networks*  
**Authors:** Xavier Glorot, Yoshua Bengio  
**Year:** 2010  
**Source:** https://proceedings.mlr.press/v9/glorot10a.html

---

## Problem / State of the Art

By 2010, deep networks were theoretically appealing but difficult to train in practice. The standard recipe — random uniform initialization and sigmoid activations — worked for shallow networks but broke down with depth. Researchers knew that gradients could vanish or explode, but there was no quantitative analysis of when or why. Without a principled account, practitioners had no systematic basis for choosing weight scales.

## Goal

Glorot and Bengio aimed to explain, analytically and experimentally, why standard initialization and sigmoid activations cause training to fail in deep networks, and to derive an initialization rule that keeps activations and gradients well-scaled through the full depth of the network.

## Challenges

Sigmoid maps any input to (0, 1) and saturates near its boundaries. With random initialization, neurons often receive large inputs, pushing sigmoid into flat saturation regions where the local gradient is near zero. The paper shows that with naive initialization, activation variance either decays to zero or explodes as it crosses multiple layers. These effects compound: saturated neurons produce near-zero gradients, which cannot propagate backward to update earlier layers.

## Key Mechanism

To keep variance stable, weights in a layer with n_in inputs and n_out outputs should be drawn from U[−√(6 / (n_in + n_out)), √(6 / (n_in + n_out))]. This Glorot uniform initializer is derived by requiring that activation variance stay constant across the forward pass and gradient variance stay constant across the backward pass — a compromise between the two constraints. The paper also identifies sigmoid's non-zero mean output (~0.5) as a source of bias that saturates deeper layers. Tanh and softsign, which are symmetric around zero, work markedly better with this initialization.

## Key Results

Experiments on MNIST and sentiment-classification tasks with networks up to five layers support the theory directly. Figure 1 in the paper plots activation histograms across layers: with standard initialization and sigmoid, activations collapse toward zero in early layers and saturate near zero or one in later layers within the first training epoch. Glorot initialization with tanh keeps histograms spread throughout training. Gradient norms also stabilize, and final test errors drop compared with the standard recipe.

## Strengths and Improvements

The main strength is the tight link between a simple variance argument and histogram evidence from real networks — the theory makes a concrete prediction, and the figures confirm it layer by layer. The limitation is that the derivation assumes approximately linear activations, so it does not cover ReLU networks (He et al., 2015 addressed this) or architectures using batch normalization or residual connections, which change variance dynamics enough to make the original criterion less critical.

## What I Learned or Liked

I found it striking that a single algebraic constraint — balance fan-in and fan-out so that activation variance is preserved — has such a decisive effect on trainability. The paper reframes initialization from guesswork into a design choice with a clear objective. It also made me appreciate that activation function and initialization are not independent choices: sigmoid's asymmetry actively undermines the initialization scheme.

## Summary

Glorot and Bengio showed that standard uniform initialization combined with sigmoid activations causes signal collapse in the forward pass and gradient vanishing in the backward pass. Their Glorot initialization, which sets weight variance to 2 / (fan-in + fan-out), keeps both signals stable across depth. This work provides the theoretical foundation for modern weight initialization and highlights that the activation function is not an independent design choice — it must be matched to the initialization scheme.

