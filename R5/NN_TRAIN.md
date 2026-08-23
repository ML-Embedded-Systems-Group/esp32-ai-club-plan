# R5: Backpropagation
## Resource Summary
Backpropagation is the algorithm used to train a neural network by calculating how much each weight contributed to the output error and then adjusting the weights to reduce that error. The process starts with a forward pass, where the input values are passed through each layer of the network. Each neuron calculates a weighted sum of its inputs and applies an activation function. In this implementation, the sigmoid activation function is used.
After the forward pass, the network compares its output with the target value. The difference between the target and the predicted output is used to calculate the error. Backpropagation then works backwards through the network using the chain rule of differentiation. The gradient calculated for each neuron determines the direction and magnitude in which its incoming weights should be changed.
The learning rate controls how large each weight update is. A larger learning rate can make learning faster but may also make training unstable. A smaller learning rate produces smaller updates and generally requires more training iterations.
For this task, I implemented the neural network with two input neurons, two hidden neurons, and one output neuron. Bias neurons are also included in each layer. The network was trained using the four possible input combinations of the AND gate.

## Maths
For the manual calculation, the input is `(1, 1)` and the target output is `1`. The initial weights are `w1 = 0.2` and `w2 = 0.2`, with bias `b = 0`. The learning rate is `0.5`.
The weighted sum is:
`z = w1*x1 + w2*x2 + b`
Substituting the values:
`z = (0.2)(1) + (0.2)(1) + 0`
`z = 0.4`
Using the sigmoid activation function:
`y = 1 / (1 + e^(-z))`
Therefore:
`y = 1 / (1 + e^(-0.4))`
`y ≈ 0.5987`
The error relative to the target is:
`e = target - output`
`e = 1 - 0.5987`
`e ≈ 0.4013`
Using mean squared error:
`MSE = (target - output)^2`
`MSE ≈ 0.1610`
For sigmoid activation:
`f'(z) = y(1-y)`
Therefore:
`f'(z) ≈ 0.5987(1 - 0.5987)`
`f'(z) ≈ 0.2403`
The gradient term is therefore proportional to:
`δ = (target - output)f'(z)`
`δ ≈ (0.4013)(0.2403)`
`δ ≈ 0.0964`
The weight gradients are:
`∂L/∂w1 ≈ -0.0964`
`∂L/∂w2 ≈ -0.0964`
The corresponding update using a learning rate of `0.5` gives approximately:
`w1_new ≈ 0.248`
`w2_new ≈ 0.248`
The bias is also updated according to the same gradient mechanism. The important observation is that the updated weights move the network output closer to the target value of `1`, resulting in a lower loss.

## Script Output
The C++ implementation was trained for 5000 epochs using all four possible inputs of the AND gate. The network used a `2-2-1` topology, sigmoid activation, a learning rate of `0.5`, and no momentum.
The training output showed the prediction for `(1,1)` progressively increasing toward the required output of `1`.
Example output:

`Made Neuron 0 0\n`
`Made Neuron 0 1`
`Made Neuron 0 2`
`Made Neuron 1 0`
`Made Neuron 1 1`
`Made Neuron 1 2`
`Made Neuron 2 0`
`Made Neuron 2 1`
`Epoch: 0 | Loss: 0.0171158`
`Epoch: 500 | Loss: 0.0146935`
`Epoch: 1000 | Loss: 0.00300284`
`Epoch: 1500 | Loss: 0.00152613`
`Epoch: 2000 | Loss: 0.000996743`
`Epoch: 2500 | Loss: 0.000731362`
`Epoch: 3000 | Loss: 0.000573806`
`Epoch: 3500 | Loss: 0.000470165`
`Epoch: 4000 | Loss: 0.000397127`
`Epoch: 4500 | Loss: 0.000343043`

`Initial Loss: 0.0171158`
`Final Loss:   0.000301547`
`PASS: Loss decreased.`

`Final predictions:`
`0 AND 0 -> 0.00307343 (target = 0)`
`0 AND 1 -> 0.0188374 (target = 0)`
`1 AND 0 -> 0.0185458 (target = 0)`
`1 AND 1 -> 0.978036 (target = 1)`
`PASS: All outputs are within 0.1 of targets.`

## How the Network Learned AND
The AND function produces `1` only when both inputs are `1`. Its truth table is:
| Input 1 | Input 2 | Target |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

Initially, the network weights are random, so its predictions are not necessarily close to these targets. During each training iteration, an input is passed through the network using the forward propagation step.
The output is then compared with the target. Backpropagation calculates the output gradient and propagates the error backwards through the hidden layer. Each connection weight is updated using its gradient and the learning rate.
Repeating this process thousands of times causes the network to find a set of weights that represents the AND relationship. The hidden neurons learn intermediate representations of the input combination, while the output neuron combines these representations to produce the final prediction.
The training results demonstrate this clearly. The output for `(1,1)` increased from approximately `0.738` at the beginning to approximately `0.978` after training. At the same time, the other three combinations converged close to zero.
This demonstrates the main purpose of backpropagation: repeatedly reducing the prediction error by using gradients to adjust the network parameters.
## What I Still Need to Learn
First of all the various activation functions and why they are needed and which ones are suitable for which case needs to be studied. Also the whole process now is a linear thing but we have to implement the things and processes in a parallel fashion and also a lot of optimizations can be done still also this is just a bare metal network it has no way of changing the parameters efficiently and thus that need to be addressed when deploying in an edge device. Also vectors are good there are good better objects and containers that can  be used for more efficient operations.
