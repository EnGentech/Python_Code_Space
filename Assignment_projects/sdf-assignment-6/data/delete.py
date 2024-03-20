from enum import Enum

class MortgageRate(Enum):
    FIXED_5 = 0.0500
    FIXED_3 = 0.0579
    FIXED_1 = 0.0589
    VARIABLE_5 = 0.0650
    VARIABLE_3 = 0.0660
    VARIABLE_1 = 0.0679

# Get user input
a = input("Enter a value: ")

if isinstance(a, MortgageRate):
    print("fine")
else:
    raise ValueError("Invalid")