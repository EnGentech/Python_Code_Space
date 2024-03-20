"""
Description: A class used to test the Mortgage class.
Author: {Student Name}
Date: {Date}
Usage: Use the tests encapsulated within
this class to test the MortgagePayment class.
"""


from unittest import TestCase
from mortgage.mortgage import Mortgage
from mortgage.pixell_lookup import MortgageRate, \
    MortgageFrequency, VALID_AMORTIZATION


class MortgageTests(TestCase):
    """Test cases for Mortgage loan implementation"""

    def setUp(self):
        # Create a valid Mortgage instance for testing
        self.valid_loan_amount = 100000
        self.valid_rate = MortgageRate.FIXED_5
        self.valid_frequency = MortgageFrequency.MONTHLY
        self.valid_amortization = 30

        self.mortgage_instance = Mortgage(
            loan_amount=self.valid_loan_amount,
            rate=self.valid_rate,
            frequency=self.valid_frequency,
            amortization=self.valid_amortization
        )

    def test_valid_loan_amount_input_exception(self):
        """
        A test case to validate self.valid_loan_amount  input
        :return: ValueError when invalid input is encountered
        """
        with self.assertRaises(ValueError) as context:
            Mortgage(
                0,
                self.valid_rate,
                self.valid_frequency,
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         'Loan Amount must be positive')

        with self.assertRaises(ValueError) as context:
            Mortgage(
                -20000,
                self.valid_rate,
                self.valid_frequency,
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         'Loan Amount must be positive')

    def test_valid_loan_amount_input(self):
        valid = Mortgage(
            20000,
            self.valid_rate,
            self.valid_frequency,
            self.valid_amortization
        )
        self.assertEqual(valid.loan_amount, 20000)

    def test_rate_input_exception(self):
        """
        A test case to validate self.valid_loan_amount  input
        :return: ValueError when invalid input is encountered
        """
        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                "text",
                self.valid_frequency,
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         "Rate provided is invalid")

        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                -20, self.valid_frequency,
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         "Rate provided is invalid")

        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                0, self.valid_frequency,
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         "Rate provided is invalid")

        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                0.0500,
                self.valid_frequency,
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         "Rate provided is invalid")

    def test_valid_rate_input(self):
        valid = Mortgage(
            self.valid_loan_amount,
            MortgageRate.VARIABLE_1,
            self.valid_frequency,
            self.valid_amortization
        )
        self.assertEqual(valid.rate.value, 0.0679)

    def test_frequency_input(self):
        """
        A test case to validate loan_amount  input
        :return: ValueError when invalid input is encountered
        """
        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                self.valid_rate,
                'text',
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         'Frequency provided is invalid')

        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                self.valid_rate, -200,
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         'Frequency provided is invalid')

        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                self.valid_rate, 12,
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         'Frequency provided is invalid')

        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                self.valid_rate, 0,
                self.valid_amortization
            )
        self.assertEqual(str(context.exception),
                         'Frequency provided is invalid')

    def test_valid_frequency_input(self):
        valid = Mortgage(
            self.valid_loan_amount,
            self.valid_rate,
            MortgageFrequency.MONTHLY,
            self.valid_amortization
        )
        self.assertEqual(valid.frequency.value, 12)

    def test_valid_amortization_input(self):
        valid = Mortgage(
            self.valid_loan_amount,
            self.valid_rate,
            self.valid_frequency,
            20
        )
        self.assertEqual(valid.amortization, 20)

    def test_amortization_input(self):
        """
        A test case to validate self.valid_loan_amount  input
        :return: ValueError when invalid input is encountered
        """
        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                self.valid_rate,
                self.valid_frequency,
                5000
            )
        self.assertEqual(str(context.exception),
                         'Amortization provided is invalid')

        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                self.valid_rate,
                self.valid_frequency,
                "text"
            )
        self.assertEqual(str(context.exception),
                         'Amortization provided is invalid')

        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                self.valid_rate,
                self.valid_frequency,
                -300
            )
        self.assertEqual(str(context.exception),
                         'Amortization provided is invalid')

        with self.assertRaises(ValueError) as context:
            Mortgage(
                self.valid_loan_amount,
                self.valid_rate,
                self.valid_frequency,
                0
            )
        self.assertEqual(str(context.exception),
                         'Amortization provided is invalid')

    def test_negative_loan(self):
        """test for negative self.valid_loan_amount  effect"""
        with self.assertRaises(ValueError) as context:
            self.mortgage_instance.loan_amount = -200
        self.assertEqual(str(context.exception),
                         'Loan Amount must be positive')

    def test_zero_loan(self):
        """test is a valueError is raised on zero input"""
        with self.assertRaises(ValueError) as context:
            self.mortgage_instance.loan_amount = 0
        self.assertEqual(str(context.exception),
                         "Loan Amount must be positive")

    def test_positive_loan(self):
        """Test if the instance return the input value is positive"""
        self.mortgage_instance.loan_amount = 200
        self.assertEqual(self.mortgage_instance.loan_amount, 200)

    def test_valid_mortgage_enum(self):
        """test if the valid input returns valid result"""
        self.mortgage_instance.rate_func = MortgageRate.VARIABLE_1
        self.assertEqual(self.mortgage_instance.rate.value, 0.0679)

    def test_invalid_mortgage_enum(self):
        """test if invalid rate input raises an exception"""
        with self.assertRaises(ValueError) as context:
            self.mortgage_instance.rate_func = 200
        self.assertEqual(str(context.exception), "Rate provided is invalid")

        with self.assertRaises(ValueError) as context:
            self.mortgage_instance.rate_func = "text"
        self.assertEqual(str(context.exception), "Rate provided is invalid")

    def test_valid_mortgage_frequency(self):
        """test if the valid input returns valid result"""
        self.mortgage_instance.frequency_func = MortgageFrequency.WEEKLY
        self.assertEqual(self.mortgage_instance.frequency.value, 52)

    def test_invalid_mortgage_frequency(self):
        """test if invalid rate input raises an exception"""
        with self.assertRaises(ValueError) as context:
            self.mortgage_instance.frequency_func = 200
        self.assertEqual(str(context.exception),
                         "Frequency provided is invalid")

        with self.assertRaises(ValueError) as context:
            self.mortgage_instance.frequency_func = "text"
        self.assertEqual(str(context.exception),
                         "Frequency provided is invalid")

    def test_valid_mortgage_amortization(self):
        """test if the valid input returns valid result"""
        self.mortgage_instance.amortization_func = 10
        self.assertEqual(self.mortgage_instance.amortization, 10)

    def test_invalid_mortgage_amortization(self):
        """test if invalid rate input raises an exception"""
        with self.assertRaises(Exception) as context:
            self.mortgage_instance.amortization_func = 200
        self.assertEqual(str(context.exception),
                         "Amortization provided is invalid")

        with self.assertRaises(Exception) as context:
            self.mortgage_instance.amortization_func = "text"
        self.assertEqual(str(context.exception),
                         "Amortization provided is invalid")

    def test_formula_result(self):
        """test the result obtained from the formula fnx"""
        self.valid_loan_amount = 682912.43
        self.valid_rate = MortgageRate.FIXED_1
        self.valid_frequency = MortgageFrequency.MONTHLY
        self.valid_amortization = 30

        result = Mortgage(
            self.valid_loan_amount,
            self.valid_rate,
            self.valid_frequency,
            self.valid_amortization
        )

        self.assertAlmostEqual(result.calculate_payment(), 4046.23)

    def test_str_monthly_return_value(self):
        """return a string method of the class instance"""
        obtained = str(self.mortgage_instance)

        expected_result = ('Mortgage Amount: $100,000.00\nRate:'
                           ' 5.00%\nAmortization: 30\nFrequency:'
                           ' Monthly -- Calculated Payment: $536.82')
        self.assertEqual(obtained, expected_result)

    def test_str_BiWeekly_return_value(self):
        """return a string method of the class instance"""
        self.mortgage_instance.frequency = MortgageFrequency.BI_WEEKLY
        obtained = str(self.mortgage_instance)

        expected_result = ('Mortgage Amount: $100,000.00\nRate:'
                           ' 5.00%\nAmortization: 30\nFrequency:'
                           ' Bi_weekly -- Calculated Payment: $247.64')
        self.assertEqual(obtained, expected_result)

    def test_str_Weekly_return_value(self):
        """return a string method of the class instance"""
        self.mortgage_instance.frequency = MortgageFrequency.WEEKLY
        obtained = str(self.mortgage_instance)

        expected_result = ('Mortgage Amount: $100,000.00\nRate:'
                           ' 5.00%\nAmortization: 30\nFrequency:'
                           ' Weekly -- Calculated Payment: $123.80')
        self.assertEqual(obtained, expected_result)

    def test_repr_list_return(self):
        """test for the representation of the instance"""
        obtained = repr(self.mortgage_instance)

        self.assertEqual(obtained, '[100000, 0.05, 12, 30]')
