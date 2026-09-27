import re

def count_word(text, word):
    count = 0
    for match in re.finditer(r'\b' + re.escape(word) + r'\b', text):
        count += 1
    return count

text = "Python is great. Python rocks!"
print(count_word(text, "Python"))  # 2
