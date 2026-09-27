var1 = input("Enter value of first variable: ")
var2 = input("Enter value of second variable: ")

print(f"Before swapping: var1 = {var1}, var2 = {var2}")
var1, var2 = var2, var1

print(f"After swapping: var1 = {var1}, var2 = {var2}")