# Understanding IEEE 754 Floating-Point Numbers

## Resource Summary
The primary resource used to understand this concept is Fabien Sanglard's brilliant article, "Floating Point Visually Explained." Instead of relying on heavy mathematical jargon right out of the gate, Sanglard breaks down the IEEE 754 format into three distinct, visual components that map directly to the bit sequence in memory. 

The **Sign** bit (1 bit) simply tells us whether the number is positive (0) or negative (1). The **Exponent** acts as a "window" or a scale, determining which power-of-two range the number falls into. Finally, the **Mantissa** (or fraction) acts as an "offset," pinpointing the exact linear position of the number within that specific power-of-two window. This visual framing makes understanding precision loss and binary representation highly intuitive.

## Maths
To convert the binary representation back into a human-readable decimal number, IEEE 754 relies on a specific mathematical formula:

**Value = (-1)^Sign × 2^(Exponent - Bias) × (1 + Mantissa_Fraction)**

Here is how the math breaks down:
- **(-1)^Sign:** If the sign bit is 0, this evaluates to 1 (positive). If it's 1, it evaluates to -1 (negative).
- **Exponent - Bias:** The exponent bits form a standard binary integer. To allow for negative exponents (which give us tiny fractions like 0.0001), IEEE 754 subtracts a fixed "Bias" (e.g., 127 for 32-bit Single Precision). If your raw exponent bits equal 129, the actual math uses `129 - 127 = 2`.
- **1 + Mantissa_Fraction:** The mantissa bits represent a fraction. Because scientific notation always has a leading '1' before the decimal point (e.g., 1.xxx), IEEE 754 assumes the '1' is there and doesn't bother storing it to save space. We add it back mathematically.

## Script Output
When running the Python script we created to inspect the number `3.14159`, the script elegantly extracts the exact memory bytes and slices them into our three components. 

For **Single Precision (32-bit)**, the output for `3.14159` looks like this:
- **Raw Bits:** `0 10000000 10010010000111111011011`
- **Sign:** `0` (Positive)
- **Exponent:** `10000000` (Raw value is 128. Minus the 127 bias, our window is 2^1)
- **Mantissa:** `10010010000111111011011` (The linear offset)

By observing the output across Half, Single, and Double precisions, it becomes instantly clear that the extra bits in Double precision simply expand the Exponent window range and massively increase the Mantissa's fractional granularity.

## Why 0.1 Is Not Exact
A classic hurdle for every new programmer is discovering that `0.1 + 0.2 == 0.3` evaluates to `False` in most programming languages. The reason lies in how fractions are represented in base-2 (binary).

In base-10, the fraction `1/3` cannot be represented perfectly; it becomes a repeating decimal (`0.33333...`). We have to truncate it eventually. The exact same limitation exists in base-2, but for different numbers. The decimal `0.1` is a clean, terminating fraction in base-10 (1/10). However, in base-2, the denominator (10) is not a power of 2, which results in a repeating, non-terminating binary fraction: `0.00011001100110011...`

Because our computer only has a finite number of bits (like 32 or 64) to store the Mantissa, it is forced to chop off the repeating tail. This truncation introduces a microscopic rounding error. When you perform math operations on these slightly inaccurate numbers, the errors compound, revealing themselves as bizarre results like `0.30000000000000004`.

## What I Still Need to Learn
While I now understand the core mechanics of normalized floating-point numbers, there is still a vast territory to explore. Specifically, I need to delve into how IEEE 754 handles edge cases, such as **Subnormal (or Denormalized) numbers**, which allow the computer to represent extremely tiny numbers close to zero by relaxing the "assumed leading 1" rule. 

I also need to learn how special values are mapped out in the bit sequence, such as **Infinity** (both positive and negative) and **NaN** (Not a Number, which occurs during impossible operations like dividing zero by zero). Finally, I would like to explore hardware rounding modes and how Fused Multiply-Add (FMA) instructions preserve precision during complex graphical calculations.
