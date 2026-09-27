vowels = 'aeiouAEIOU'
with open('original.txt', 'r') as src, open('vowel_filtered.txt', 'w') as dst:
    content = src.read()
    filtered = ''.join(c for c in content if c not in vowels)
    dst.write(filtered); print(filtered)