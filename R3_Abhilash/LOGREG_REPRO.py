import math
import random

def sigmoid(z): return 1 / (1 + math.exp(-z))

def classify(x1, x2, w1, w2, b):
    return 1 if sigmoid(w1 * x1 + w2 * x2 + b) >= 0.5 else 0

dataset = [[1.0, 1.0, 0], [1.5, 2.0, 0], [2.0, 1.5, 0], [4.0, 4.0, 1], [4.5, 5.0, 1], [5.0, 4.5, 1]]
n = len(dataset)
alpha, updates = 0.1, 1000
w1 = w2 = b = initial_loss = loss = 0.0

for update in range(1, updates + 1):
    l_tot = d_w1 = d_w2 = d_b = 0.0
    
    for (x1, x2, y) in dataset:
        p = sigmoid(w1 * x1 + w2 * x2 + b)
        l_tot -= y * math.log(p) + (1 - y) * math.log(1 - p)
        d_w1 += (p - y) * x1
        d_w2 += (p - y) * x2
        d_b += (p - y)
        
    loss = l_tot / n
    if update == 1: initial_loss = loss
    if update % 100 == 0: print(f"Update {update:4d} | Loss: {loss:.4f}")
        
    w1 -= alpha * (d_w1 / n)
    w2 -= alpha * (d_w2 / n)
    b -= alpha * (d_b / n)

print("-" * 30)
if loss <= initial_loss:
    print("PASS")

flag = any(classify(x1, x2, w1, w2, b) != y for (x1, x2, y) in dataset)
if not flag:
    print("PASS")

identity_true_counter = 0
for _ in range(100):
    z_rand = random.uniform(-10, 10)
    assert math.isclose(sigmoid(z_rand) + sigmoid(-z_rand), 1.0, rel_tol=1e-9), f"Identity check failed for {z_rand}"
    identity_true_counter += 1

print(f"sigmoid identity accuracy: {(identity_true_counter/100):.4f}")
print(f"Decision Boundary (z = 0): {w1:.4f}*x1 + {w2:.4f}*x2 + {b:.4f} = 0")
