"""
Description:
Author:
Date:
Usage:
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount, get_balance, make_deposit, user_selection
from src.chatbot import VALID_TASKS, ACCOUNTS


class ChatbotTests(unittest.TestCase):

    def test_get_account(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["123456"]

            # Act
            obtained = get_account()

            # Assert
            self.assertEqual(obtained, 123456)

    def test_get_account_valueError(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]

            # Assert and Act
            with self.assertRaises(Exception) as context:
                get_account()

            # Assert
            self.assertEqual(str(context.exception), "Account number must be a whole number.")

    def test_get_account_account_exist(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["112233"]

            # Assert and Act
            with self.assertRaises(Exception) as context:
                get_account()

            # Assert
            self.assertEqual(str(context.exception), "Account number entered does not exist.")

    def test_get_amount(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.return_value = 500.10

            # Act
            result = get_amount()

            # Assert
            self.assertEqual(result, 500.10)

    def test_get_amount_value_error(self):
        # Arrange
        with patch("builtins.input") as mock_input:
            mock_input.side_effect = ["non_numeric_data"]

            # Assert and Act
            with self.assertRaises(Exception) as context:
                get_amount()

            # Assert
            self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")

    def test_get_amount_zero(self):
        # Arrange
        with patch("builtins.input") as value:
            value.side_effect = ["0"]

            # Assert and Act
            with self.assertRaises(Exception) as error:
                get_amount()

            # Assert
            self.assertEqual(str(error.exception), "Invalid amount. Please enter a positive number.")

    def test_get_amount_negative_number(self):
        # Arrange
        with patch("builtins.input") as negative:
            negative.side_effect = ['-500']

            # Assert and Act
            with self.assertRaises(Exception) as error:
                get_amount()

            # Assert
            self.assertEqual(str(error.exception), "Invalid amount. Please enter a positive number.")

    def test_get_balance_correct_output(self):
        # Arrange
        account_number = 123456

        # Act
        obtained = get_balance(account_number)

        # Assert
        self.assertEqual(obtained, "Your current balance for account 123456 is $1,000.00.")

    def test_get_balance_invalid_account_number(self):
        # Assert and Act
        with self.assertRaises(Exception) as error:
            get_balance(112233)

        # Assert
        self.assertEqual(str(error.exception), 'Account number does not exist.')

    def test_make_deposit_updates_balance_correctly(self):
        # Arrange
        account_number = 123456
        initial_balance = ACCOUNTS[account_number]["balance"]
        deposit_amount = 1500.01

        # Act
        make_deposit(account_number, deposit_amount)

        # Assert
        updated_balance = ACCOUNTS[account_number]["balance"]
        expected_balance = initial_balance + deposit_amount
        self.assertEqual(updated_balance, expected_balance)

    def test_make_deposit_returns_correct_string(self):
        # Arrange
        account_number = 123456
        deposit_amount = 1500.01

        # Act
        result = make_deposit(account_number, deposit_amount)

        # Assert
        expected_result = f'You have made a deposit of ${deposit_amount:,.2f} to account {account_number}.'
        self.assertEqual(result, expected_result)

    def test_make_deposit_invalid_account_raises_exception(self):
        # Arrange
        account_number = 112233
        deposit_amount = 1500.01

        # Assert
        with self.assertRaises(Exception) as context:
            make_deposit(account_number, deposit_amount)
        self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_make_deposit_negative_amount_raises_value_error(self):
        # Arrange
        account_number = 123456
        deposit_amount = -50.01

        # Assert
        with self.assertRaises(ValueError) as context:
            make_deposit(account_number, deposit_amount)
        self.assertEqual(str(context.exception), "Invalid Amount. Amount must be positive.")

    def test_user_selection(self):
        # Arrange
        with patch("builtins.input") as user:
            user.side_effect = ["balance"]

            # Act
            obtained = user_selection()

            # Assert
            self.assertEqual(obtained, 'balance')

    def test_user_selection_mixed_cases(self):
        # Arrange
        with patch("builtins.input") as user:
            user.side_effect = ['DepOSit', 'DEPOSIT']

            # Act
            obtained = user_selection()

            # Assert
            self.assertEqual(obtained, 'deposit')

    def test_user_selection_invalid_input(self):
        # Arrange
        with patch("builtins.input") as invalid:
            invalid.side_effect = ['invalid']

            # Assert and Act
            with self.assertRaises(Exception) as error:
                user_selection()

            expect = "Invalid task. Please choose balance, deposit, or exit."
            # Assert
            self.assertEqual(str(error.exception), expect)


if __name__ == '__main__':
    unittest.main()
