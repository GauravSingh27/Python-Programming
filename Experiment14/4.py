class AgeRestrictionError(Exception):
    """Custom exception for age under 18."""
    pass

age = 16

try:
    if age < 18:
        raise AgeRestrictionError("Age must be 18 or older.")
except AgeRestrictionError as e:
    print(f"Caught an error: {e}")
