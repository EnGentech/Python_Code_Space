"""
Description: A class meant to manage Mortgage options.
Author: {Student Name}
Date: {Date}
Usage: Create an instance of the Mortgage
class to manage mortgage records and
calculate payments.
"""
from mortgage.pixell_lookup import \
    VALID_AMORTIZATION, MortgageRate, MortgageFrequency


class Mortgage:
    """class definition"""

    def __init__(self, loan_amount: float,
                 rate: MortgageRate, frequency: MortgageFrequency,
                 amortization: int):
        """Public instance attribute"""
        self._loan_amount = loan_amount
        self.rate = rate
        self.frequency = frequency
        self.amortization = amortization
        if loan_amount > 0:
            self._loan_amount = loan_amount
        else:
            raise ValueError("Loan Amount must be positive")
        if isinstance(rate, MortgageRate):
            self.rate = rate
        else:
            raise ValueError("Rate provided is invalid")
        if isinstance(frequency, MortgageFrequency):
            self.frequency = frequency
        else:
            raise ValueError("Frequency provided is invalid")
        if amortization not in VALID_AMORTIZATION:
            raise ValueError("Amortization provided is invalid")
        self.amortization = amortization

    @property
    def loan_amount(self):
        """get instant attribute"""
        return self._loan_amount

    @loan_amount.setter
    def loan_amount(self, value):
        """set loan_amount to value"""
        if value <= 0:
            raise ValueError("Loan Amount must be positive")
        else:
            self._loan_amount = value

    @property
    def rate_func(self):
        """get instance attribute rate"""
        return self.rate

    @rate_func.setter
    def rate_func(self, value):
        """set a value for rate"""
        if not isinstance(value, MortgageRate):
            raise ValueError("Rate provided is invalid")
        else:
            self.rate = value

    @property
    def frequency_func(self):
        """get instance attribute for frequency"""
        return self.frequency

    @frequency_func.setter
    def frequency_func(self, value):
        """set a value for frequency"""
        if not isinstance(value, MortgageFrequency):
            raise ValueError("Frequency provided is invalid")
        else:
            self.frequency = value

    @property
    def amortization_func(self):
        """get instance attribute for amortization"""
        return self.amortization

    @amortization_func.setter
    def amortization_func(self, value):
        """set a value for frequency"""
        if value in VALID_AMORTIZATION:
            self.amortization = value
        else:
            raise Exception("Amortization provided is invalid")

    def calculate_payment(self) -> float:
        """return the calculation given by a certain formula"""
        p = self.loan_amount
        i = self.rate.value / self.frequency.value
        n = self.amortization * self.frequency.value
        formula = p * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        return round(formula, 2)

    def __str__(self):
        """A string method to return a string data-type"""
        freq = str(self.frequency).split(".")
        display = (f'Mortgage Amount: ${self.loan_amount:,.2f}'
                   f'\nRate: {self.rate.value * 100:,.2f}%'
                   f'\nAmortization: {self.amortization}'
                   f'\nFrequency: {freq[1].capitalize()}'
                   f' -- Calculated Payment: ${self.calculate_payment():,.2f}')
        return display

    def __repr__(self):
        """this function returns a representation of an instance"""
        loan = self.loan_amount
        rate = self.rate.value
        freq = self.frequency.value
        amortization = self.amortization
        store_repr = [loan, rate, freq, amortization]
        return str(store_repr)
