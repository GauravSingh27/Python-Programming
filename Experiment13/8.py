import re
with open('original.txt', 'r') as src, open('single_space.txt', 'w') as dst:
    content = src.read()
    cleaned = re.sub(r'\s+', ' ', content)
    dst.write(cleaned.strip())
print("Multiple spaces replaced with single space in single_space.txt")