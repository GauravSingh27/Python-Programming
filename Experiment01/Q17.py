def calculate_shifts(number, shift_amount):
    
    left_shifted_value = number << shift_amount
    
    right_shifted_value = number >> shift_amount
    
    print(f"Original number: {number}")
    print(f"Shift amount: {shift_amount}")
    print("-" * 30)
    print(f"Left shifted value: {left_shifted_value}")
    print(f"Right shifted value: {right_shifted_value}")

calculate_shifts(number=20, shift_amount=2)

print("\n" + "=" * 30 + "\n")

calculate_shifts(number=128, shift_amount=4)
