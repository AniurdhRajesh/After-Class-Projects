number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Cannot calculate the square root of a negative number.")
else:
    for i in range(number + 1):
        if i * i == number:
            print(f"The exact square root of {number} is {i}.")
            break
    else:
        print(f"{number} does not have an exact square root.")
