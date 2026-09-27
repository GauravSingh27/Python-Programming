import re

def starts_with_hello(text):
    match = re.match(r"Hello", text)
    return bool(match)

# Test cases
print(starts_with_hello("Hello World"))  # True
print(starts_with_hello("Hi there Hello"))     # False
