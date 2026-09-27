with open('original.txt', 'r') as file:
    lines = sum(1 for line in file)
print(f"Total lines in backup.txt: {lines}")