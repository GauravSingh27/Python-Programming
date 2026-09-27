import re

def extract_all_digits(text):
    digits = re.findall(r'\d+', text)
    return ''.join(digits) if digits else ''

# Test cases
print(extract_all_digits("abc123def456"))     # 123456
print(extract_all_digits("No digits here"))   # ''
print(extract_all_digits("42 is the answer")) # 42
