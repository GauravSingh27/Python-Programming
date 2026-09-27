import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9.]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Tests
print(validate_email("test@example.com"))  # True
print(validate_email("invalid-email"))     # False
