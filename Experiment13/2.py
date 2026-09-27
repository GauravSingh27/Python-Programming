with open('student.txt', 'r') as file:
    content = file.read()
upper, lower, digits = 0, 0, 0
for char in content:
    if char.isupper(): upper += 1
    elif char.islower(): lower += 1
    elif char.isdigit(): digits += 1
print(f"Uppercase: {upper}, Lowercase: {lower}, Digits: {digits}")