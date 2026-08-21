# Linear Regression with Gradient Descent

## Resource Summary
### Cost Function
Formula : 
$$
J = \frac{1}{2n}\sum_{i=1}^{n}(\hat{y}_i-y_i)^2
$$ 
where n = number of training examples, ŷᵢ = Predicted value for the i-th data point
yᵢ = Actual value for the i-th data point<br>
It calculates the error i.e. difference b/w predicted values with the actual values. The 1/2 is added to make the derivative simpler.
### Partial Derivatives
Formula : 
$$
\frac{\partial J}{\partial w}
=
\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i-y_i)x_i
$$

$$
\frac{\partial J}{\partial b}
=
\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i-y_i)
$$

where ŷᵢ = wx+b and xᵢ = feature of the i-th data point. <br>
It tells us how the cost changes when we change w or b. Gradient Descent uses these values to adjust w and b in order to lower the cost.

### Learning Rate(α)
The learning rate determines how big of a step we take down the slope. In this example, we take α = 0.01. <br>
If we choose α too small, the training becomes extremely slow, and if we choose α too large, the cost function may diverge, as a result it may miss the minima. Therefore, choosing the right α is crucial.


### Update Rule
The update rule used to find new w and b (w' & b').<br>
Formula :
$$
w' = w - \alpha \frac{\partial J}{\partial w},
\qquad
b' = b - \alpha \frac{\partial J}{\partial b}
$$ <br>
Gradient Descent repeatedly updates w and b in the direction that decreases the error. The model is considered converged when w and b change very little with each update and the cost is close to the minimum.



## Maths

Given points : (1,8),(2,11),(3,14),(4,17)

- Initialize: w = 0, b = 0
- Learning rate: α = 0.01
- Number of examples: n = 4
- Eq: ŷᵢ = w·xᵢ + b
- Loss function: (Mean Squared Error) MSE = (1/n) Σ (ŷᵢ − yᵢ)²

w=0,b=0, so: 

ŷᵢ = (0)(xᵢ) + 0 = 0

So ŷ₁ = ŷ₂ = ŷ₃ = ŷ₄ = 0.


### 1. MSE 
= (1/4) [ (0−8)² + (0−11)² + (0−14)² + (0−17)² ]
 = **167.5**


### 2. Partial Derivative : 

cost function(J) = (1/2n) Σ (ŷᵢ − yᵢ)², where ŷ = wx + b (we use 2n, so that calculation of derivative becomes easier)

∂J/∂w = (1/n) Σ (ŷᵢ − yᵢ) · xᵢ

∂J/∂b = (1/n) Σ (ŷᵢ − yᵢ)


**∂J/∂w :**

∂J/∂w = (1/4) [ (0−8)(1) + (0−11)(2) + (0−14)(3) + (0−17)(4) ]

= (1/4) [ −8 − 22 − 42 − 68 ]

= -35

**∂J/∂b :**

∂J/∂b = (1/4) [ (0−8) + (0−11) + (0−14) + (0−17) ]

= **−12.5**

### 3. Gradient Descent Update

w' = w − α (∂J/∂w),  b' = b − α (∂J/∂b)

w' = 0 − 0.01 × (−35) = **0.35**

b' = 0 − 0.01 × (−12.5) = **0.125**

So the new func is : ŷ = 0.35x + 0.125

New predictions:

- ŷ₁ = 0.35(1) + 0.125 = 0.475
- ŷ₂ = 0.35(2) + 0.125 = 0.825
- ŷ₃ = 0.35(3) + 0.125 = 1.175
- ŷ₄ = 0.35(4) + 0.125 = 1.525

New MSE:

MSE = (1/4) [ (0.475−8)² + (0.825−11)² + (1.175−14)² + (1.525−17)² ]
    = **141.028125**

**So, w = 0.35**<br>
**b = 0.125**<br>
**new loss(141.028125) < old loss(167.5)**


## Script Output
```
loss after  0 step :  167.5
loss after  100 step :  1.5748291649385493
loss after  200 step :  1.1671086151417072
loss after  300 step :  0.8649486346603753
loss after  400 step :  0.6410167236320916
loss after  500 step :  0.47505993247490763
loss after  600 step :  0.35206872320634286
loss after  700 step :  0.26091947012746947
loss after  800 step :  0.19336841191570214
loss after  900 step :  0.14330606569350188
Loss : Pass
w: fail
b: fail
Final prediction :
[7.4737873843256715, 10.745013951590302, 14.016240518854936, 17.287467086119566]
Biggest error: 0.5262126156743285
```


## Why the Line Is Recovered
Suppose the line is y=wx+b. First we initialize the calculation by taking any arbitrary values of w and b (for the given math problem, we take w=0 & b=0). Next, we use the current w and b to get the predicted values and then we compare them with the actual values. The difference between them is the error in our predictions. We have to find out the cost function(J) = (1/2n) Σ (ŷᵢ − yᵢ)², where ŷ = wx+b. If we plot the graph of cost function, then it forms a parabola. Our main aim is to minimize the error, so we find the global minima of cost function by taking its derivative. For line y=wx+b, we take derivative of ∂J/∂w & ∂J/∂b. Then to minimize the cost function we use Gradient Descent, w' = w − α (∂J/∂w),  b' = b − α (∂J/∂b) where α is the learning rate and ∂J/∂w & ∂J/∂b represent the slopes. The learning rate determines how big of a step we take down the slope. In this way we get new w & b. Again we find out the cost function, and repeat the whole process. Gradient Descent repeatedly updates w and b in the direction that decreases the error. Because these points follow the equation y = 3x + 5, as we reduce the error the values of w and b gradually approach 3 and 5. As a result we recover the final line y=3x+5.


## What I Still Need to Learn
I still need to learn the linear regression method using ordinary least squares, which scikit-learn uses by default