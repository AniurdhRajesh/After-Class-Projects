def decimal_to_binary(decimal_number, bit_length=16):
    return format(decimal_number, f'0{bit_length}b')

decimal_number = 45
binary_representation = decimal_to_binary(decimal_number, 16)
print(f"Decimal: {decimal_number} -> Binary: {binary_representation}")
