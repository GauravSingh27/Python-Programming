class InsufficientBalanceError(Exception):
    """Custom exception for insufficient ATM balance."""
    pass

def withdraw_money(balance, amount):
    try:
        if amount > balance:
            raise InsufficientBalanceError(f"Error: Insufficient balance. Available: ${balance}")
        
        balance -= amount
        print(f"Withdrawal successful! Remaining balance: ${balance}")
    except InsufficientBalanceError as e:
        print(e)

# Example Usage
current_balance = 500
withdraw_money(current_balance, 600)  # This will trigger the exception
