def count_capital_letters(s):
    count = 0
    for char in s:
        if char.isupper():  
            count += 1
    return count

text = str(input("Enter sentence:"))
print(count_capital_letters(text))  
