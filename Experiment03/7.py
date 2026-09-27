count = 0
print("Numbers divisible by both 5 and 7 (1-100):")

for i in range(1, 101):
    if i % 5 == 0 and i % 7 == 0:
        print(i, end=" ")
        count += 1

print(f"\nTotal count: {count}")
