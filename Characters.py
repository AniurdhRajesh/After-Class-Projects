user_input = input("Enter some numbers: ")
num_digits = sum(char.isdigit() for char in user_input)
print(f"You entered {num_digits} digits.")

