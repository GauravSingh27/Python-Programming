n = int(input("Enter number of fruits (n): "))

print("\nEnter fruits for set s1:")
s1 = set()
for i in range(n):
    fruit = input(f"Fruit {i+1}: ").strip().lower()
    s1.add(fruit)

print("\nEnter fruits for set s2:")
s2 = set()
for i in range(n):
    fruit = input(f"Fruit {i+1}: ").strip().lower()
    s2.add(fruit)

print(f"\nSet s1: {s1}")
print(f"Set s2: {s2}")

print(f"a. Fruits in both s1 and s2: {s1 & s2}")

print(f"b. Fruits only in s1 but not in s2: {s1 - s2}")

print(f"c. Total unique fruits count: {len(s1 | s2)}")
