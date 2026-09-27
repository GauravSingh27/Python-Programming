num = int(input("Enter the number:"))
i = 1
table = 1
for i in range(1,11):
    table = num*i
    print(f"{num} × {i} = {num*i}")