try:
    print("Executing the try block...")
    # No errors here
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print("Success")  # This runs because no exception occurred
