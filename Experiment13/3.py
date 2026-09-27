with open('original.txt', 'r') as src, open('backup.txt', 'w') as dst:
    while True:
        char = src.read(1)
        if not char: break
        dst.write(char)
print("Copied character by character to backup.txt")