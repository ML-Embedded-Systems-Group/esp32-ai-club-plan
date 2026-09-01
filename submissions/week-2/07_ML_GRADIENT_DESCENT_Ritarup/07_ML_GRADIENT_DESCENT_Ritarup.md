# An Overview of Gradient Descent Optimization Algorithms

**Paper:** *An Overview of Gradient Descent Optimization Algorithms*<br>
**Author:** Sebastian Ruder<br>
**Source:** https://arxiv.org/abs/1609.04747

## Problem / State of the Art

Gradient descent is the core algorithm used to train neural networks and minimize cost functions. Although almost every deep learning library relies on it, coders often treat these optimizers like black boxes. Traditional gradient descent comes in three main styles - batch, SGD, and mini batch which trade off computation speed for parameter update accuracy. Mini-batch SGD is commonly used, but choosing a suitable learning rate and using the same update behavior for every parameter can still cause problems.

## Goal

The main goal of the paper is how different gradient descent algorithms works, It first introduces three approaches to gradient descent—Batch Gradient Descent, SGD, and Mini batch Gradient Descent. Then it explains improved optimization algorithms such as Momentum, Nesterov Momentum, AdaGrad, RMSprop, and Adam.

## Challenges

Training deep networks with basic gradient descent presents multiple major difficulties:
*The first problem is the data size, if the data size is too big, and if we use normal gradient descent method, then the process become expensive.
* The learning rate controls how large each step is. If it is too small, training can take a very long time. If it is too large, the weights can jump over the minimum or make training unstable.
* The optimization process can encounter local minima, saddle points, and relatively flat areas where progress becomes difficult.

## Key Mechanism

The paper explains several optimizers by showing how each one modifies the basic gradient update:

* **Stochastic Gradient Descent (SGD):** SGD updates the weights using the gradient calculated from a batch of training data. Its main difficulty is that the learning rate has to be chosen manually.
* **SGD with Momentum:** Momentum adds a velocity term to the update. When the weights continue moving in roughly the same direction, it increases the velocity as a result it covers more distance and reduces the random looking movement of normal SGD.
* **SGD with Nesterov Momentum:** Nesterov momentum makes a look ahead move before calculating the gradient. Instead of calculating the gradient at the current position, it checks the position after the velocity step, then it allows the  optimizer to react to the new direction.
* **AdaGrad:** AdaGrad changes the effective learning rate separately for each parameter. It keeps track of previous squared gradients, reducing the step for parameters that have changed a lot and giving more emphasis to parameters that have changed less.
* **Adadelta & RMSprop** RMSprop addresses AdaGrad's problem of continually reducing the learning rate. It keeps a discounted memory of previous gradients, allowing the effective learning rate to increase or decrease depending on the recent gradients.
* **Adam:** It takes the best parts of Momentum + RMSprop, then also fixes an initial bias problem. It uses recent squared gradients to adjust the learning rate and a separate term to smooth the direction of movement.

## Key Results

The paper shows that the different optimizers can follow noticeably different paths while trying to reach a minimum. Adam combines two useful ideas, adaptive learning rates and momentum, making it a practical optimizer for many situations. However, the paper points out that a newer optimizer should not automatically be considered better in every situation.

## Strengths and Improvements

* **Strengths:** The paper explains different optimization algorithms in a step by step manner, making it easier to understand what problems the previous method has, and how next method can improve it.
* **Improvements:** The paper is mainly an overview of existing optimization techniques. More standardized comparisons across different modern neural network architectures would make it easier to judge the methods under the same conditions.

## What I Learned or Liked

I liked how the optimizers build on one another instead of being presented as completely separate methods. For example, Momentum introduces the idea of remembering previous movement, while Nesterov improves this by looking ahead. AdaGrad then approaches the problem from another angle by changing the effective learning rate for individual parameters. The discussion also makes it clear that Adam is not automatically better than SGD in every situation, since SGD can sometimes generalize better to unseen data.

## Summary

The paper explains how different optimizers (like- momentum, NAG, adagrad, adam etc.) try to improve the gradient descent process. The paper also emphasizes that there is no single optimizer that is always best, and the behavior of these methods is still an active area of research.
