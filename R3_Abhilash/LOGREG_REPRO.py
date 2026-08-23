import math
import random

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

def classify(x1, x2, w1, w2, b):
    z = w1 * x1 + w2 * x2 + b
    p = sigmoid(z)
    threshold = 0.5
    if p >= threshold:
        return 1
    else:
        return 0

# Dataset containing [x1, x2, y]
dataset = [
    [1.0, 1.0, 0],
    [1.5, 2.0, 0],
    [2.0, 1.5, 0],
    [4.0, 4.0, 1],
    [4.5, 5.0, 1],
    [5.0, 4.5, 1]
]
dataset_size = len(dataset)

# Hyperparameters
alpha = 0.1
updates = 1000
w1 = 0.0
w2 = 0.0
b = 0.0
initial_loss = 0.0
loss = 0.0

# Training loop
for update in range(1, updates + 1):
    loss_total = 0.0
    loss_total_der_w1 = 0.0
    loss_total_der_w2 = 0.0
    loss_total_der_b = 0.0
    
    for (x1, x2, y) in dataset:
        z = w1 * x1 + w2 * x2 + b
        p = sigmoid(z)
        
        # Binary cross-entropy loss
        log_loss = -y * math.log(p) - (1 - y) * math.log(1 - p)
        loss_total += log_loss
        
        # Accumulate gradients
        loss_total_der_w1 += (p - y) * x1
        loss_total_der_w2 += (p - y) * x2
        loss_total_der_b += (p - y)
        
    # Average loss over dataset
    loss = loss_total / dataset_size
    
    if update == 1:
        initial_loss = loss
        
    if update % 100 == 0:
        print(f"Update {update:4d} | Loss: {loss:.4f}")
        
    # Update weights
    temp_w1 = w1 - alpha * (loss_total_der_w1 / dataset_size)
    temp_w2 = w2 - alpha * (loss_total_der_w2 / dataset_size)
    temp_b = b - alpha * (loss_total_der_b / dataset_size)
    
    w1 = temp_w1
    w2 = temp_w2
    b = temp_b

# Check if learning successfully reduced loss
print("-" * 30)
if loss <= initial_loss:
    print("PASS")

# Check classification accuracy
flag = 0
for (x1, x2, y) in dataset:
    predicted_y = classify(x1, x2, w1, w2, b)
    if predicted_y != y:
        flag = 1
        break

if flag == 0:
    print("PASS")

# Identity: sigmoid(z) + sigmoid(-z) = 1
identity_true_counter = 0
for _ in range(100):
    z_rand = random.uniform(-10, 10)
    if sigmoid(z) + sigmoid(-z) == 1:
        identity_true_counter += 1
print(f"sigmoid indentity accuracy: {(identity_true_counter/100):.4f}")

# Print the decision boundary where z = 0
print(f"Decision Boundary (z = 0): {w1:.4f}*x1 + {w2:.4f}*x2 + {b:.4f} = 0")
