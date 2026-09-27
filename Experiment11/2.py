import re

text = "abc123def456"
digits = re.findall(r'\d', text)
print(digits)  # Output: 123456
