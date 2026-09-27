bool1 = input("Enter first boolean (True/False): ").lower() == 'true'
bool2 = input("Enter second boolean (True/False): ").lower() == 'true'
bool3 = input("Enter third boolean (True/False): ").lower() == 'true'

result = (bool1 and bool2) or not bool3

print(f"The result of the expression ((bool1 and bool2) or not bool3) is: {result}")