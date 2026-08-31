# Understanding IEEE 754 Floating-Point Numbers

## Resource Summary
The primary resource used to understand this concept is Fabien Sanglard's "Floating Point Visually Explained." The article visualizes IEEE 754 format in three physical components: a 1-bit **Sign**, an **Exponent** window acting as a power-of-two scale, and a **Mantissa** acting as the linear offset within that specific window.

## Maths
To manually derive the IEEE 754 representation for specific targets like `3.5` and `0.25` without relying on hardware abstraction (e.g., Python's `struct`), we use base-2 extraction:
*   **Target 3.5:** 
    *   3.5 in binary is `11.1`.
    *   Normalized (Scientific Notation): `1.11 * 2^1`.
    *   Exponent: `1 + 127 (Bias) = 128` (`10000000` in binary).
    *   Mantissa: Drop the leading `1`, leaving `11`. Pad with 21 zeros (`11000000000000000000000`).
*   **Target 0.25:**
    *   0.25 in binary is `0.01`.
    *   Normalized: `1.0 * 2^-2`.
    *   Exponent: `-2 + 127 = 125` (`01111101` in binary).
    *   Mantissa: Drop the leading `1`, leaving `0`. Pad with 23 zeros.

## Script Output
Our reproduction script strictly avoids `struct` and mathematically processes the bits to verify the exact hex outputs and round-trip data retention required by the task:

*   **3.5 Verification:** Calculates as `0 10000000 11000000000000000000000`, which correctly maps to the exact hex requirement **0x40600000**. Round-trip decimal conversion confirms an exact match.
*   **0.25 Verification:** Calculates as `0 01111101 00000000000000000000000`, which correctly maps to the exact hex requirement **0x3E800000**. Round-trip decimal conversion confirms an exact match.

## Why 0.1 Is Not Exact
The decimal `0.1` (1/10) cannot be perfectly represented in base-2 because 10 is not a power of 2, creating an infinitely repeating binary fraction (`0.0001100110011...`). 

Our script calculates the exact decimal value of the chopped bits in memory for 0.1:
*   **32-bit Single Precision:** `0.09999990463256835938`
*   **64-bit Double Precision:** `0.09999999999999997780`

Because the 32-bit format runs out of bits earlier, it chops off the repeating sequence much sooner than the 64-bit format. Therefore, the single-precision version of 0.1 is mathematically distinct from the double-precision version, meaning `float32(0.1) == float64(0.1)` evaluates to `False`.

## What I Still Need to Learn
I need to investigate subnormal numbers and how IEEE 754 handles numbers that are too close to zero to have a leading `1` before the decimal point, as my current manual math functions do not account for the denormalization edge case.