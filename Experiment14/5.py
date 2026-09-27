correct_user = "admin"
correct_pass = "12345"

try:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != correct_user or password != correct_pass:
        raise Exception("Invalid username or password!")
    
    print("Login successful!")
except Exception as e:
    print(f"Login failed: {e}")
