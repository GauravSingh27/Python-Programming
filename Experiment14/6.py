try:
    # Outer block: Handles input errors (e.g., entering text instead of a number)
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    try:
        # Inner block: Handles division errors
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Inner Error: Cannot divide by zero.")

except ValueError:
    print("Outer Error: Please enter a valid integer.")
