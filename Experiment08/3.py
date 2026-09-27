def print_1_to_n(n):
    if n >= 1:
        print_1_to_n(n-1)  
        print(n)          

print_1_to_n(int(input("Enter the number:")))
