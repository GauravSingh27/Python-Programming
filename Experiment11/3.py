import re

text = "Hello World Python"
result = re.sub(r'\s', '_', text)
print(result)  # Output: Hello_World_Python
