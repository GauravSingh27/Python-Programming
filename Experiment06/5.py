s = str(input("ENTER sentence: "))
s_lower = s.lower()
freq = {}
for char in s_lower:
    if char.isalpha(): 
        freq[char] = freq.get(char, 0) + 1

for char in sorted(freq):
    print(f"{char.upper()}{freq[char]}", end='\n')
