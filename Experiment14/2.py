my_list = [10, 20, 30]

try:
    # Attempting to access an index that is out of range
    print(my_list[5])
except IndexError:
    print("Error: The index you are trying to access is out of range.")
