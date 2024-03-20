import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open
from data_processor.data_processor import DataProcessor


class TestDataProcessor(TestCase):
    INPUT_DATA = [
        {"Transaction ID": "1",
         "Account number": "1001",
         "Date": "2023-03-01",
         "Transaction type": "deposit",
         "Amount": 1000, "Currency": "CAD",
         "Description": "Salary"},
        {"Transaction ID": "2", "Account number": "1002",
         "Date": "2023-03-01", "Transaction type": "deposit",
         "Amount": 1500, "Currency": "CAD", "Description": "Salary"}
    ]

    def setUp(self):
        # Arrange
        self.processor = DataProcessor(self.INPUT_DATA)

    def tearDown(self):
        # Act
        pass

    def test_update_account_summary_deposit(self):
        # Arrange
        with patch.object(DataProcessor,
                          'update_account_summary',
                          wraps=self.processor.update_account_summary) \
                as mock_method:
            # Act
            self.processor.update_account_summary(self.INPUT_DATA[0])

            # Assert
            account_summary = self.processor._account_summaries['1001']
            self.assertEqual(account_summary['balance'], 1000)
            self.assertEqual(account_summary['total_deposits'], 1000)
            mock_method.assert_called_once()

    def test_update_account_summary_withdrawal(self):
        # Arrange
        with patch.object(DataProcessor, 'update_account_summary',
                          wraps=self.processor.update_account_summary) \
                as mock_method:
            # Act
            self.processor.update_account_summary(self.INPUT_DATA[1])

            # Assert
            account_summary = self.processor._account_summaries['1002']
            self.assertEqual(account_summary['balance'], 1500)
            self.assertEqual(account_summary['total_withdrawals'], 0)
            mock_method.assert_called_once()

    def test_check_suspicious_transactions_large_amount(self):
        # Arrange
        SUSPICIOUS_DATA = [
            {"Transaction ID": "1", "Account number": "1001",
             "Date": "2023-03-01", "Transaction type": "deposit",
             "Amount": 100000, "Currency": "CAD", "Description": "Salary"}
        ]
        with patch.object(DataProcessor, 'check_suspicious_transactions',
                          wraps=self.processor.check_suspicious_transactions) \
                as mock_method:
            # Act
            self.processor.check_suspicious_transactions(SUSPICIOUS_DATA[0])

            # Assert
            self.assertIn(SUSPICIOUS_DATA[0],
                          self.processor._suspicious_transactions)
            suspect_account = self.processor._suspicious_transactions
            self.assertEqual(suspect_account, SUSPICIOUS_DATA)

    def test_check_suspicious_transactions_uncommon_currency(self):
        # Arrange
        SUSPICIOUS_DATA = [
            {"Transaction ID": "1", "Account number": "1001",
             "Date": "2023-03-01", "Transaction type": "deposit",
             "Amount": 1000, "Currency": "XRP", "Description": "Salary"}
        ]
        with patch.object(DataProcessor,
                          'check_suspicious_transactions',
                          wraps=self.processor.check_suspicious_transactions) \
                as mock_method:
            # Act
            self.processor.check_suspicious_transactions(SUSPICIOUS_DATA[0])

            # Assert
            self.assertIn(SUSPICIOUS_DATA[0],
                          self.processor._suspicious_transactions)
            suspect_account = self.processor._suspicious_transactions
            self.assertEqual(suspect_account, SUSPICIOUS_DATA)

    def test_update_transaction_statistics(self):
        # Arrange
        with patch.object(DataProcessor,
                          'update_transaction_statistics',
                          wraps=self.processor.update_transaction_statistics) \
                as mock_method:
            # Act
            self.processor.update_transaction_statistics(self.INPUT_DATA[0])

            # Assert
            self.assertEqual(
                self.processor._transaction_statistics['deposit']
                ['total_amount'],
                1000)
            self.assertEqual(
                self.processor._transaction_statistics['deposit']
                ['transaction_count'],
                1)
            mock_method.assert_called_once()

    def test_get_average_transaction_amount(self):
        # Arrange
        with patch.object(DataProcessor,
                          'update_transaction_statistics',
                          wraps=self.processor.update_transaction_statistics
                          ):
            # Act
            self.processor.update_transaction_statistics(self.INPUT_DATA[0])
            self.processor.update_transaction_statistics(self.INPUT_DATA[1])

            deposit_average = self.processor.get_average_transaction_amount(
                'deposit'
            )
            # withdrawal_average = self.processor.\
            # get_average_transaction_amount(
            # 'withdrawal'
            # )

            # Assert
            self.assertEqual(deposit_average, 1250)
            # self.assertEqual(withdrawal_average, 1500)


if __name__ == "__main__":
    unittest.main()
