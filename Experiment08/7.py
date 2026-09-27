def cube_recursive(n):
    if n == 0:
        return 0
    return n**3 + cube_recursive(n-1) - (n-1)**3

# Test
print("Cube of 5:", cube_recursive(5))  # 125
print("Cube of 3:", cube_recursive(3))  # 27
print("Cube of 1:", cube_recursive(1))  # 1
