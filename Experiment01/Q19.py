main_string = "Hello, world!"

char_to_find = 'o'
is_present = char_to_find in main_string

if is_present:
    print(f"The character '{char_to_find}' was found in the string.")
else:
    print(f"The character '{char_to_find}' was not found in the string.")