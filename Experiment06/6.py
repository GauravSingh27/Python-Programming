n = int(input("Enter n: "))
values = list(map(int, input("Enter {} values: ".format(n)).split()))

counts = [0] * 4
for val in values:
    if 0 <= val <= 3:
        counts[val] += 1

print("Occurrences:")
for i in range(4):
    print(f"{i}: {counts[i]}")
