"""
Description: Enumerations to keep track of valid mortgage rates
and payment frequencies. A list to keep track of valid amortization periods.
Author: ACE Department
Edited By: {Student Name}
Date: {Date}
Usage: The enumerations and list in this file may be used when working
with mortgages to ensure only valid rates, frequencies and amortization
periods are used.
"""


from enum import Enum

VALID_AMORTIZATION = [5, 10, 15, 20, 25, 30]


class MortgageRate(Enum):
    """
    A class definition that creates a symbolic name for
    different mortgage rate options with ease to utilizing
    different rate value within the code

    Options:
        - FIXED_5: 5-year fixed mortgage rate at 5.00%
        - FIXED_3: 3-year fixed mortgage rate at 5.79%
        - FIXED_1: 1-year fixed mortgage rate at 5.89%
        - VARIABLE_5: 5-year variable mortgage rate at 6.50%
        - VARIABLE_3: 3-year variable mortgage rate at 6.60%
        - VARIABLE_1: 1-year variable mortgage rate at 6.79%
    """
    FIXED_5 = 0.0500
    FIXED_3 = 0.0579
    FIXED_1 = 0.0589
    VARIABLE_5 = 0.0650
    VARIABLE_3 = 0.0660
    VARIABLE_1 = 0.0679


class MortgageFrequency(Enum):
    """
    Enumeration representing various payment frequency options.
    This enumeration defines symbolic names for different
    payment frequency options, indicating how often
    mortgage payments are made throughout the year.

    Options:
        - MONTHLY: Monthly payments (12 times a year)
        - BI_WEEKLY: Bi-weekly payments (26 times a year)
        - WEEKLY: Weekly payments (52 times a year)
    """
    MONTHLY = 12
    BI_WEEKLY = 26
    WEEKLY = 52
