def cone_volume():
    r = float(input("Enter radius (r): "))
    h = float(input("Enter height (h): "))
    volume = ((3.14 * r * r * h) / 3)
    print(f"Volume of cone = {volume:.2f}")
    return volume

cone_volume()
