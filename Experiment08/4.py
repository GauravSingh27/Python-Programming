def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)


print("Fibonacci terms:", [fib(i) for i in range(int(input("Enter the Number: ")))])


