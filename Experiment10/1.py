import re

def starts_with_hello(text):
    if re.match(r'^Hello', text):
        return True
    return False

# Test cases
print(starts_with_hello("Hello world"))  # True
print(starts_with_hello("Hi there"))     # False
print(starts_with_hello("Hello"))        # True
print(starts_with_hello("hellO"))        # False
