import struct

def print_ieee754_components(number):
    """
    Takes a decimal number and prints its IEEE 754 representation 
    in Half, Single, and Double precision, broken down into Sign, Exponent, and Mantissa.
    """
    print(f"=== Analyzing Number: {number} ===\n")

    # A dictionary to hold our configurations for the 3 formats
    # Format: (struct_code, total_bits, exponent_bits, mantissa_bits, bias)
    formats = {
        "Half (16-bit)":   (">e", 16, 5,  10, 15),
        "Single (32-bit)": (">f", 32, 8,  23, 127),
        "Double (64-bit)": (">d", 64, 11, 52, 1023)
    }

    for name, (struct_code, total_bits, exp_bits, mant_bits, bias) in formats.items():
        try:
            
            packed_bytes = struct.pack(struct_code, number)
            
            binary_string = "".join(f"{byte:08b}" for byte in packed_bytes)
            
            
            sign_bit = binary_string[0]
            exponent_bits = binary_string[1 : 1 + exp_bits]
            mantissa_bits = binary_string[1 + exp_bits : ]
            
            
            raw_exponent_val = int(exponent_bits, 2)
            actual_exponent = raw_exponent_val - bias
            
            
            print(f"--- {name} ---")
            print(f"Raw Bits : {sign_bit} {exponent_bits} {mantissa_bits}")
            print(f"Sign     : {sign_bit} (0 = Positive, 1 = Negative)")
            print(f"Exponent : {exponent_bits} (Raw: {raw_exponent_val}, Actual Window: 2^{actual_exponent})")
            print(f"Mantissa : {mantissa_bits} (The linear offset in the window)")
            print("-" * 40)
            
        except OverflowError:
            print(f"--- {name} ---")
            print("Number is too large/small to be represented in this format!")
            print("-" * 40)


if __name__ == "__main__":
    test_number = float(input("Enter a decimal number to analyze: "))
    print_ieee754_components(test_number)