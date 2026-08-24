import random
 
# Joint probability table
joint = {
    ("A1", "B1"): 0.2,
    ("A1", "B2"): 0.3,
    ("A2", "B1"): 0.4,
    ("A2", "B2"): 0.1,
}
 
# P(B1) = sum over A of P(A, B1)
p_b1 = joint[("A1", "B1")] + joint[("A2", "B1")]
 
# Bayes rule: P(A1 | B1) = P(A1, B1) / P(B1)
p_a1_given_b1 = joint[("A1", "B1")] / p_b1
 
print(f"P(B1) = {p_b1:.4f}")
print(f"P(A1 | B1) = {p_a1_given_b1:.4f}")
 
print("PASS" if abs(p_b1 - 0.6) < 1e-9 else "FAIL")
print("PASS" if abs(p_a1_given_b1 - 0.333) < 1e-3 else "FAIL")
 
# Coin toss simulation
random.seed(42)
for n in (100, 1000, 10000):
    heads = sum(1 for _ in range(n) if random.random() < 0.5)
    freq = heads / n
    error = abs(freq - 0.5)
    print(f"n={n}: freq={freq:.4f}, error={error:.4f}")
    if n == 10000:
        print("PASS" if error <= 0.01 else "FAIL")
 