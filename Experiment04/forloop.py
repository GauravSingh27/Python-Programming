text = input("Enter a string: ")

upper_text = ""

for char in text:
    if 'a' <= char <= 'z': 
        upper_text += chr(ord(char) - 32) 
    else:
        upper_text += char  

print("Uppercase string:", upper_text)
