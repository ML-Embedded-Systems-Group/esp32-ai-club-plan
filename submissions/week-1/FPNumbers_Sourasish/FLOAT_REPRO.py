import math

def decimal_to_ieee32(n):
    """Mathematically converts a float to 32-bit IEEE 754 binary without struct."""
    if n == 0.0: return "0" * 32
    
    sign_bit = "1" if n < 0 else "0"
    n = abs(n)
    
    # Calculate Exponent
    exponent = math.floor(math.log(n, 2))
    bias = 127
    stored_exp = exponent + bias
    exp_bits = f"{stored_exp:08b}"
    
    # Calculate Mantissa
    mantissa_val = (n / (2 ** exponent)) - 1
    mantissa_bits = ""
    for _ in range(23):
        mantissa_val *= 2
        if mantissa_val >= 1:
            mantissa_bits += "1"
            mantissa_val -= 1
        else:
            mantissa_bits += "0"
            
    return sign_bit + exp_bits + mantissa_bits

def decimal_to_ieee64(n):
    """Mathematically converts a float to 64-bit IEEE 754 binary for 0.1 comparison."""
    if n == 0.0: return "0" * 64
    sign_bit = "1" if n < 0 else "0"
    n = abs(n)
    exponent = math.floor(math.log(n, 2))
    exp_bits = f"{(exponent + 1023):011b}"
    
    mantissa_val = (n / (2 ** exponent)) - 1
    mantissa_bits = ""
    for _ in range(52):
        mantissa_val *= 2
        if mantissa_val >= 1:
            mantissa_bits += "1"
            mantissa_val -= 1
        else:
            mantissa_bits += "0"
    return sign_bit + exp_bits + mantissa_bits

def ieee_to_decimal(binary_str, precision="single"):
    """Performs the exact round-trip calculation from binary back to decimal."""
    exp_len, bias = (8, 127) if precision == "single" else (11, 1023)
    
    sign = -1 if binary_str[0] == '1' else 1
    exponent = int(binary_str[1 : 1+exp_len], 2) - bias
    
    mantissa_fraction = 0.0
    for i, bit in enumerate(binary_str[1+exp_len:]):
        if bit == '1':
            mantissa_fraction += 2 ** -(i + 1)
            
    return sign * (2 ** exponent) * (1 + mantissa_fraction)

if __name__ == "__main__":
    print("--- H1 Task Verification ---\n")
    
    targets = [3.5, 0.25]
    for num in targets:
        bin_32 = decimal_to_ieee32(num)
        hex_32 = hex(int(bin_32, 2))
        round_trip = ieee_to_decimal(bin_32, "single")
        
        print(f"Target: {num}")
        print(f"Binary: {bin_32[0]} {bin_32[1:9]} {bin_32[9:]}")
        print(f"Hex:    {hex_32.upper().replace('X', 'x')}")
        print(f"Round-trip exact match: {num == round_trip} (Calculated: {round_trip})\n")

    print("--- 0.1 Single vs Double Comparison ---")
    bin_01_single = decimal_to_ieee32(0.1)
    bin_01_double = decimal_to_ieee64(0.1)
    
    single_val = ieee_to_decimal(bin_01_single, "single")
    double_val = ieee_to_decimal(bin_01_double, "double")
    
    print(f"0.1 Single precision exact value: {single_val:.20f}")
    print(f"0.1 Double precision exact value: {double_val:.20f}")
    print(f"Match: {single_val == double_val}")