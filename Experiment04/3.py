my_string = input("Enter a string: ")

vowels = "aeiouAEIOU"

vowel_count = sum(1 for char in my_string if char in vowels)

print("Number of vowels:", vowel_count)
