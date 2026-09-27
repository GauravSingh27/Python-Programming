filename = input("Enter filename: ")
word = input("Enter word to search: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
    print("Word found" if word in content else "Word not found")
except FileNotFoundError:
    print("File not found!")