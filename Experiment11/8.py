import re

paragraph = "Hello World python Apple Cat dog"
caps_words = re.findall(r'\b[A-Z][a-z]*\b', paragraph)
print(caps_words)  # ['Hello', 'World', 'Apple', 'Cat']
