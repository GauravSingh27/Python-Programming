# Input number of values
n = int(input("Enter number of values (n): "))

# Create tuple by taking n numeric inputs
numbers = []
for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Convert list to tuple
num_tuple = tuple(numbers)

# Calculate average
total_sum = sum(num_tuple)
average = total_sum / len(num_tuple)

# Display results
print(f"\nTuple created: {num_tuple}")
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
