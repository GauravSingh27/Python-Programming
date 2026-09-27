my_dict = {"name": "Alice", "age": 25}

try:
    # Attempting to access a key that doesn't exist
    print(my_dict["city"])
except KeyError:
    print("Error: The key 'city' does not exist in the dictionary.")
