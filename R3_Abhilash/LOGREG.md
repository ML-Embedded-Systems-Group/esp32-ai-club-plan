# Logistic Regression

## Resource Summary

Logistic regression is a foundational supervised machine learning algorithm tailored primarily for binary classification tasks, predicting the probability that a given input vector belongs to a particular class (typically denoted as $y \in \{0, 1\}$). While linear regression models continuous target variables and can produce unbounded outputs ($-\infty$ to $+\infty$), fitting a straight line to binary targets leads to nonsensical predictions outside the $[0, 1]$ probability range and extreme sensitivity to outliers.

To resolve this, logistic regression applies a non-linear activation function—the logistic sigmoid function—to a linear combination of features. The input to the sigmoid function is the linear predictor or "logit" $z$, defined as:

$$z = w_1 x_1 + w_2 x_2 + \dots + w_k x_k + b = w^T x + b$$

where $w$ represents feature weights and $b$ denotes the bias term. The sigmoid function maps any real-valued $z$ into a valid probability $p \in (0, 1)$ using the formula:

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

The resulting output $p = P(y=1\vert{}X)$ represents the conditional probability of the positive class. To convert probabilities into discrete class predictions, a decision threshold is applied (commonly $0.5$). When $p \ge 0.5$ (or equivalently $z \ge 0$), the model predicts class 1; otherwise, it predicts class 0.

Model parameters ($w$ and $b$) are estimated by optimizing a loss function called Binary Cross-Entropy (BCE) or Log-Loss, derived from Maximum Likelihood Estimation (MLE). Unlike Mean Squared Error, which produces a non-convex loss surface when combined with the sigmoid activation, Binary Cross-Entropy yields a convex loss surface, guaranteeing that gradient descent can converge to the global minimum. The loss penalizes confident wrong predictions exponentially as the predicted probability diverges from the true binary label.

---

## Maths

Given parameters $w = [1.0, -0.5]$, $b = 0.1$, and input vector $x = [2.0, 3.0]$:

### 1. Calculate the Logit $z$

$$z = w \cdot x + b = (1.0 \cdot 2.0) + (-0.5 \cdot 3.0) + 0.1 = 2.0 - 1.5 + 0.1 = 0.6$$

### 2. Calculate the Sigmoid $\sigma(z)$

$$\sigma(0.6) = \frac{1}{1 + e^{-0.6}} = \frac{1}{1 + 0.5488116} = \frac{1}{1.5488116} \approx 0.645656 \approx 0.646$$

### 3. Calculate Binary Cross-Entropy for Label $y = 1$

$$L = - \left[ y \ln(\hat{p}) + (1 - y) \ln(1 - \hat{p}) \right]$$

Since $y = 1$:

$$L = -\ln(\hat{p}) = -\ln(0.645656) \approx 0.43746 \approx 0.437$$

### 4. Identity Proof: $\sigma(z) + \sigma(-z) = 1$

$$\sigma(z) + \sigma(-z) = \frac{1}{1 + e^{-z}} + \frac{1}{1 + e^{z}}$$

Multiply the numerator and denominator of the second term by $e^{-z}$:

$$\frac{1}{1 + e^{z}} \cdot \frac{e^{-z}}{e^{-z}} = \frac{e^{-z}}{e^{-z} + 1}$$

Substitute back into the summation:

$$\sigma(z) + \sigma(-z) = \frac{1}{1 + e^{-z}} + \frac{e^{-z}}{1 + e^{-z}} = \frac{1 + e^{-z}}{1 + e^{-z}} = 1$$

---

## Script Output

```text
Update  100 | Loss: 0.3367
Update  200 | Loss: 0.2234
Update  300 | Loss: 0.1651
Update  400 | Loss: 0.1304
Update  500 | Loss: 0.1076
Update  600 | Loss: 0.0916
Update  700 | Loss: 0.0797
Update  800 | Loss: 0.0705
Update  900 | Loss: 0.0633
Update 1000 | Loss: 0.0574
------------------------------
PASS
PASS
sigmoid indentity accuracy: 1.0000
Decision Boundary (z = 0): 1.0595*x1 + 1.0595*x2 + -5.8570 = 0
```

---

## Decision Boundary

The decision boundary occurs where $z = 0$, which corresponds to a predicted probability $\sigma(z) = 0.5$.

From the script output:

$$1.0595 x_1 + 1.0595 x_2 - 5.8570 = 0$$

Rearranging into slope-intercept form ($x_2$ in terms of $x_1$):

$$1.0595 x_2 = -1.0595 x_1 + 5.8570$$

$$x_2 = -x_1 + \frac{5.8570}{1.0595}$$

$$x_2 = -x_1 + 5.528$$

* **Slope:** $-1.0$
* **$x_2$-intercept:** $5.528$

**Interpretation:** Points lying above the line $x_2 = -x_1 + 5.528$ correspond to $z > 0$ ($\hat{p} > 0.5$) and are classified as class 1, while points below correspond to $z < 0$ ($\hat{p} < 0.5$) and are classified as class 0.

---

## What I Still Need to Learn

* **Regularization Techniques:** Implementing $L_1$ (Lasso) and $L_2$ (Ridge) penalties in the loss function to prevent overfitting and perform feature selection.
* **Evaluation Metrics & ROC-AUC:** Analyzing model performance beyond raw accuracy using Precision, Recall, F1-Score, Receiver Operating Characteristic (ROC) curves, and Area Under the Curve (AUC).
* **Multiclass Classification:** Extending binary logistic regression to non-binary outcomes using One-vs-Rest (OvR) strategies and Multinomial Logistic Regression (Softmax Regression).
