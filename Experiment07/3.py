S1 = {"Red", "yellow", "orange", "blue"}
S2 = {"violet", "blue", "purple"}

print("S1 =", S1)
print("S2 =", S2)
print()

# 1. Union (all elements from both sets)
union = S1 | S2
print("1. Union (S1 | S2):", union)

# 2. Intersection (common elements)
intersection = S1 & S2
print("2. Intersection (S1 & S2):", intersection)

# 3. Difference S1 - S2 (only in S1)
diff_s1 = S1 - S2
print("3. S1 - S2:", diff_s1)

# 4. Difference S2 - S1 (only in S2)
diff_s2 = S2 - S1
print("4. S2 - S1:", diff_s2)

# 6. Subset check
print("6. Is S1 subset of S2?", S1.issubset(S2))
print("7. Is S2 subset of S1?", S2.issubset(S1))
