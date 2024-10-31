
while True:
 string_input = input("Enter a string: ")

 length = len(string_input)
 uppercase = string_input.upper()
 lowercase = string_input.lower()
 reversed_string = string_input[::-1]
 contains_substring = "anirudh" in string_input
 
 print(f"Length of the string: {length}")
 print(f"Uppercase: {uppercase}")
 print(f"Lowercase: {lowercase}")
 print(f"Reversed: {reversed_string}")
 print(f"Contains 'anirudh': {contains_substring}")
