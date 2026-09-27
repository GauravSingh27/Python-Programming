class InvalidMarksError(Exception):
    """Custom exception for marks outside the 0-100 range."""
    pass

def input_marks():
    try:
        marks = float(input("Enter student marks (0-100): "))
        
        if marks < 0 or marks > 100:
            raise InvalidMarksError("Error: Marks must be between 0 and 100.")
        
        print(f"Marks accepted: {marks}")
    except InvalidMarksError as e:
        print(e)
    except ValueError:
        print("Error: Please enter a valid numerical value.")

# Example Usage
input_marks()
