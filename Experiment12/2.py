# Write some integers to the file (one per line)
with open("numbers.txt", "w") as f:
    numbers = [50, 75, 120, 90, 200, 30, 150]
    for n in numbers:
        f.write(str(n) + "\n")
