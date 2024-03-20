import unittest
import csv
import os
from output_handler.output_handler import OutputHandler


class TestOutputHandler(unittest.TestCase):
    ACCOUNT_SUMMARIES = {
        '1001': {'account_number': '1001',
                 'balance': 50, 'total_deposits': 100,
                 'total_withdrawals': 50},
        '1002': {'account_number': '1002',
                 'balance': 200, 'total_deposits': 200,
                 'total_withdrawals': 0}
    }

    SUSPICIOUS_TRANSACTIONS = [{
        "Transaction ID": "1",
        "Account number": "1001",
        "Date": "2023-03-14",
        "Transaction type": "deposit",
        "Amount": 250, "Currency": "XRP",
        "Description": "crypto investment"
    }]

    TRANSACTION_STATISTICS = {
        'deposit': {'total_amount': 300,
                    'transaction_count': 2},
        'withdrawal': {'total_amount': 50,
                       'transaction_count': 1}
    }

    def setUp(self):
        # Arrange
        self.output_handler = OutputHandler(
            account_summaries=self.ACCOUNT_SUMMARIES,
            suspicious_transactions=self.SUSPICIOUS_TRANSACTIONS,
            transaction_statistics=self.TRANSACTION_STATISTICS
        )

    def tearDown(self):
        # Act
        self.remove_output_files()

    def remove_output_files(self):
        # Arrange
        output_files = ['account_summaries.csv',
                        'suspicious_transactions.csv',
                        'transaction_statistics.csv']

        # Act
        for file_path in output_files:
            if os.path.exists(file_path):
                os.remove(file_path)

    def test_write_account_summaries_to_csv(self):
        # Arrange
        output_file_path = 'account_summaries.csv'

        # Act: Call the method being tested
        self.output_handler.write_account_summaries_to_csv(output_file_path)

        # Assert
        self.assertTrue(os.path.exists(output_file_path))

        with open(output_file_path, 'r') as output_file:
            csv_reader = csv.reader(output_file)
            rows = list(csv_reader)

        expected_rows = len(self.ACCOUNT_SUMMARIES) + 1
        self.assertEqual(len(rows), expected_rows)

    def test_write_suspicious_transactions_to_csv(self):
        # Arrange
        output_file_path = 'suspicious_transactions.csv'

        # Act
        self.output_handler.write_suspicious_transactions_to_csv(output_file_path)

        # Assert
        self.assertTrue(os.path.exists(output_file_path))

        with open(output_file_path, 'r') as output_file:
            csv_reader = csv.reader(output_file)
            rows = list(csv_reader)

        expected_rows = len(self.SUSPICIOUS_TRANSACTIONS) + 1
        self.assertEqual(len(rows), expected_rows)

    def test_write_transaction_statistics_to_csv(self):
        # Arrange
        output_file_path = 'transaction_statistics.csv'

        # Act
        self.output_handler.write_transaction_statistics_to_csv(output_file_path)

        # Assert
        self.assertTrue(os.path.exists(output_file_path))

        with open(output_file_path, 'r') as output_file:
            csv_reader = csv.reader(output_file)
            rows = list(csv_reader)

        expected_rows = len(self.TRANSACTION_STATISTICS) + 1
        self.assertEqual(len(rows), expected_rows)

    def test_output_handler_filter_account_summaries_less_than(self):
        # Arrange
        balance = "balance"
        value = 100
        mode = False

        # Act
        instantiate_test = self.output_handler.filter_account_summaries(
            balance,
            value,
            mode
        )

        expected_result = [
            ('1001', {'account_number': '1001',
                      'balance': 50, 'total_deposits': 100,
                      'total_withdrawals': 50}
             )
        ]

        self.assertEqual(instantiate_test, expected_result)

    def test_output_handler_filter_account_summaries_greater_than(self):
        # Arrange
        balance = "balance"
        value = 100
        mode = True

        # Act
        instantiate_test = self.output_handler.filter_account_summaries(
            balance,
            value,
            mode
        )

        expected_result = [
            ('1002', {'account_number': '1002',
                      'balance': 200, 'total_deposits': 200,
                      'total_withdrawals': 0}
             )
        ]

        self.assertEqual(instantiate_test, expected_result)

    def test_write_filtered_summaries_to_csv(self):
        # Arrange
        filtered_data = [
            ('1002', {'account_number': '1002',
                      'balance': 150,
                      'total_deposits': 200,
                      'total_withdrawals': 50}
             )
        ]
        file_path = 'test_filtered_summaries.csv'

        # Act
        self.output_handler.write_filtered_summaries_to_csv(
            filtered_data,
            file_path
        )

        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            data = [row for row in reader]

        expected_row = [
            '1002',
            "{'account_number': '1002', "
            "'balance': 150, "
            "'total_deposits': 200, "
            "'total_withdrawals': 50}"
        ]

        self.assertEqual(data, [expected_row])


if __name__ == '__main__':
    unittest.main()
