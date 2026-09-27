import re

def validate_mobile(num):
    pattern = r'^\d*[6-9]\d{9}$'
    return bool(re.match(pattern, num)) and len(num) == 10

print(validate_mobile("9876543210"))  # True
print(validate_mobile("5123456789"))  # False
