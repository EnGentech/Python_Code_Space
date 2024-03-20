"""
Description: A client program written to verify accuracy of and 
calculate payments for PiXELL River Mortgages.
Author: ACE Faculty
Edited by: {Student Name}
Date: {Date}
"""

### REQUIREMENT
### ADD IMPORT STATEMENTS FOR THE MORTGAGE CLASS, THE 
### MORTGAGERATE AND MORTGAGEFREQUENCY ENUMERATIONS AND THE 
### VALID_AMORTIZATION LIST

from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import VALID_AMORTIZATION, \
    MortgageRate, MortgageFrequency

### REQUIREMENT
### ENCLOSE THE FOLLOWING 'WITH OPEN' BLOCK IN A 'TRY-EXCEPT' BLOCK WHICH 
### WILL CATCH A 'FILENOTFOUNDERROR' EXCEPTION
with open("data\\pixell_river_mortgages.txt", "r") as file:
    print("**************************************************")
    
    for data in file:
        items = data.split(",")
        
        try:
            amount = float(items[0])
            rate = items[1]
            amortization = items[2]
            frequency = items[3]

            ### REQUIREMENT:
            ### INSTANTIATE A MORTGAGE OBJECT USING THE VALUES
            ### FOR AMOUNT, RATE, FREQUENCY AND AMORTIZATION ABOVE.
            mortgage_calculator = Mortgage(
                loan_amount=amount,
                rate=MortgageRate[rate],
                frequency=MortgageFrequency[frequency],
                amortization=int(amortization)
            )
            
            ### REQUIREMENT:
            ### PRINT THE MORTGAGE OBJECT
            print(mortgage_calculator)

        except ValueError as e:
            # This except block will catch Explicit exceptions: 
            # Those raised by the programmer in the Mortgage class.
            print(f"Data: {data.strip()} caused Exception: {e}")
        
        except Exception as e:
            # This except block will catch Implicit exceptions:
            # Those raised through normal execution.
            print(f"Data: {data.strip()} caused Exception: {e}")
        finally:
            print("**************************************************")
