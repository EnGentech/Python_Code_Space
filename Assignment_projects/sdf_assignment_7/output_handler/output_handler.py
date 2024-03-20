import csv


class OutputHandler:
    """
    Handles writing financial data to CSV files.
    """

    def __init__(self, account_summaries: dict,
                 suspicious_transactions: list,
                 transaction_statistics: dict) -> None:
        """
        Initializes an OutputHandler object.

        Parameters:
            account_summaries (dict): Dictionary containing account summaries.
            suspicious_transactions (list): List of suspicious transactions.
            transaction_statistics (dict): Dictionary containing transaction statistics.
        """
        self._account_summaries = account_summaries
        self._suspicious_transactions = suspicious_transactions
        self._transaction_statistics = transaction_statistics

    def write_account_summaries_to_csv(self, file_path: str) -> None:
        """
        Writes account summaries to a CSV file.

        Parameters:
            file_path (str): The path to the output CSV file.
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Account number', 'Balance', 'Total Deposits', 'Total Withdrawals'])

            for account_number, summary in self._account_summaries.items():
                writer.writerow([
                    account_number,
                    summary['balance'],
                    summary['total_deposits'],
                    summary['total_withdrawals']
                ])

    def write_suspicious_transactions_to_csv(self, file_path: str) -> None:
        """
        Writes suspicious transactions to a CSV file.

        Parameters:
            file_path (str): The path to the output CSV file.
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(
                ['Transaction ID', 'Account number', 'Date', 'Transaction type', 'Amount', 'Currency', 'Description'])

            for transaction in self._suspicious_transactions:
                writer.writerow([
                    transaction['Transaction ID'],
                    transaction['Account number'],
                    transaction['Date'],
                    transaction['Transaction type'],
                    transaction['Amount'],
                    transaction['Currency'],
                    transaction['Description']
                ])

    def write_transaction_statistics_to_csv(self, file_path: str) -> None:
        """
        Writes transaction statistics to a CSV file.

        Parameters:
            file_path (str): The path to the output CSV file.
        """
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['Transaction type', 'Total amount', 'Transaction count'])

            for transaction_type, statistic in self._transaction_statistics.items():
                writer.writerow([
                    transaction_type,
                    statistic['total_amount'],
                    statistic['transaction_count']
                ])

    def filter_account_summaries(self, filter_field: str,
                                 filter_value: int,
                                 filter_mode: bool):
        filtered_list = []
        filter_field_list = [
            'balance',
            'total_deposits',
            'total_withdrawals'
        ]
        if filter_field in filter_field_list:
            if filter_mode:
                filtered_list = list(filter(
                    lambda valid_record: valid_record[1][filter_field] >= filter_value,
                    self._account_summaries.items()))
            else:
                filtered_list = list(filter(
                    lambda valid_record: valid_record[1][filter_field] <= filter_value,
                    self._account_summaries.items()))
        return filtered_list

    def write_filtered_summaries_to_csv(self, filtered_data, file_path):
        with open(file_path, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            for row in filtered_data:
                writer.writerow(row)

filtered_data = [
            ('1002', {'account_number': '1002',
                      'balance': 100,
                      'total_deposits': 200,
                      'total_withdrawals': 50}
             ),
                ('1002', {'account_number': '1002',
                      'balance': 150,
                      'total_deposits': 200,
                      'total_withdrawals': 50}
             )
        ]
x = OutputHandler({"key": "value"}, [4,5 ], {'hi': 'hello'})
x.write_filtered_summaries_to_csv(filtered_data, 'delete.csv')
