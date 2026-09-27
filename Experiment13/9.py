# Create name.txt
names = ['Alice\nBob\nEve\nDavid\nAnna']
with open('name.txt', 'w') as f: f.writelines(names)

# 1a. Count names
with open('name.txt') as f: print(f"Total names: {len(f.readlines())}")

# 1b. Vowel-starting names
vowels = 'aeiouAEIOU'
vowel_count = sum(1 for line in open('name.txt') if line.strip() and line[0] in vowels)
print(f"Vowel-starting: {vowel_count}")

# 1c. Longest name
names = [line.strip() for line in open('name.txt') if line.strip()]
print(f"Longest: {max(names, key=len)}")