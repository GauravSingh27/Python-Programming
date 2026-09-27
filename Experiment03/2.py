num = int(input("Enter a number: "))
original = num
length = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** length
    num //= 10

if total == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")
