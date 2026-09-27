# Create numbers.txt
with open('numbers.txt', 'w') as f: 
    f.write('45\n120\n89\n150\n200\n75\n')

# 2a. Max number
numbers = [int(line) for line in open('numbers.txt')]
print(f"Max: {max(numbers)}")

# 2b. Average
print(f"Average: {sum(numbers)/len(numbers):.2f}")

# 2c. Count > 100
count_big = sum(1 for n in numbers if n > 100)
print(f"Numbers > 100: {count_big}")