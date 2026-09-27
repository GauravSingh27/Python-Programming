numbers = [1, 2, 2, 3, 4, 4, 5, 2]
unique = list(set(numbers))
print(unique)  

#using sets
numbers = [1, 2, 2, 3, 4, 4, 5, 2]
unique = list(dict.fromkeys(numbers))
print(unique)  
