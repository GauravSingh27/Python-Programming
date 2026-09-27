import cmath  
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("This is not a quadratic equation (a cannot be 0).")
else:
    d = (b ** 2) - (4 * a * c)

    root1 = (-b + cmath.sqrt(d)) / (2 * a)
    root2 = (-b - cmath.sqrt(d)) / (2 * a)

    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

    if d > 0:
        print("The equation has two distinct real roots.")
    elif d == 0:
        print("The equation has two equal real roots.")
    else:
        print("The equation has two complex (imaginary) roots.")
