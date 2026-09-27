# Read all names from the file
with open("name.txt", "r") as f:
    names = f.read().splitlines()   # one name per line

# a. Count number of names
num_names = len(names)
print("Total number of names:", num_names)

# b. Count names starting with a vowel
vowels = "AEIOUaeiou"
count_vowel = sum(1 for name in names if name and name[0] in vowels)
print("Names starting with vowel:", count_vowel)

# c. Find the longest name
if names:
    longest = max(names, key=len)
    print("Longest name:", longest)
else:
    print("File is empty.")
