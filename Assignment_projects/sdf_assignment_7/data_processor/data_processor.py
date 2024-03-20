import logging


class DataProcessor:
    """
    A class for processing financial transaction data.

    Class Attributes:
        LARGE_TRANSACTION_THRESHOLD (int): Threshold amount for considering a transaction as large.
        UNCOMMON_CURRENCIES (list): List of uncommon currencies.

    Attributes:
        _input_data (list): List of dictionaries representing financial transaction data.
        _account_summaries (dict): Dictionary storing account summaries.
        _suspicious_transactions (list): List of suspicious transactions.
        _transaction_statistics (dict): Dictionary storing transaction statistics.
    """

    LARGE_TRANSACTION_THRESHOLD = 10000
    UNCOMMON_CURRENCIES = ['XRP', 'LTC']

    def __init__(self, input_data: list,
                 logging_level=logging.WARNING,
                 logging_format='%(asctime)s - %(levelname)s - %(message)s',
                 log_file=None):
        """
        Initializes a DataProcessor object.

        Parameters:
            input_data (str): The path to the input file.
            logging_level (int): The level of severity which will cause a record to be logged. Default is WARNING.
            logging_format (str): The way in which the log messages should be formatted. Default is provided format.
            log_file (str): The file to which logging will be written. Default is None (logging to console).
        """
        self._input_data = input_data
        self._account_summaries = {}
        self._suspicious_transactions = []
        self._transaction_statistics = {}
        self._log_file = log_file
        self._log_format = logging_format
        self._log_level = logging_level

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging_level)
        formatter = logging.Formatter(logging_format)

        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        else:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self.logger.addHandler(stream_handler)

    def process_data(self) -> dict:
        """
        Processes the financial transaction data and returns a dictionary containing summaries and statistics.

        Returns:
            dict: Dictionary containing account summaries, suspicious transactions, and transaction statistics.
        """
        for row in self._input_data:
            self.update_account_summary(row)
            self.check_suspicious_transactions(row)
            self.update_transaction_statistics(row)

            self.logger.setLevel(logging.INFO)
            self.logger.info(f"Data Processing Complete")

        return {
            "account_summaries": self._account_summaries,
            "suspicious_transactions": self._suspicious_transactions,
            "transaction_statistics": self._transaction_statistics
        }

    def update_account_summary(self, row: dict) -> None:
        """
        Updates the account summary based on the given transaction row.

        Parameters:
            row (dict): Dictionary representing a financial transaction.
        """
        account_number = row['Account number']
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        if account_number not in self._account_summaries:
            self._account_summaries[account_number] = {
                "account_number": account_number,
                "balance": 0,
                "total_deposits": 0,
                "total_withdrawals": 0
            }

        if transaction_type == "deposit":
            self._account_summaries[account_number]["balance"] += amount
            self._account_summaries[account_number]["total_deposits"] += amount
        elif transaction_type == "withdrawal":
            self._account_summaries[account_number]["balance"] -= amount
            self._account_summaries[account_number]["total_withdrawals"] += amount
        self.logger.setLevel(logging.INFO)
        self.logger.info(f"Account summary updated: {row['Account number']}")

    def check_suspicious_transactions(self, row: dict) -> None:
        """
        Checks if a transaction is suspicious and updates the list of suspicious transactions.

        Parameters:
            row (dict): Dictionary representing a financial transaction.
        """
        amount = float(row['Amount'])
        currency = row['Currency']

        if amount > self.LARGE_TRANSACTION_THRESHOLD or currency in self.UNCOMMON_CURRENCIES:
            self._suspicious_transactions.append(row)
            self.logger.setLevel(logging.WARNING)
            self.logger.warning(f"Suspicious transaction: {row}")

    def update_transaction_statistics(self, row: dict) -> None:
        """
        Updates transaction statistics based on the given transaction row.

        Parameters:
            row (dict): Dictionary representing a financial transaction.
        """
        transaction_type = row['Transaction type']
        amount = float(row['Amount'])

        if transaction_type not in self._transaction_statistics:
            self._transaction_statistics[transaction_type] = {
                "total_amount": 0,
                "transaction_count": 0
            }

        self._transaction_statistics[transaction_type]["total_amount"] += amount
        self._transaction_statistics[transaction_type]["transaction_count"] += 1
        self.logger.setLevel(logging.INFO)
        self.logger.info(f"Updated transaction statistics for: {row['Transaction type']}")

    def get_average_transaction_amount(self, transaction_type: str) -> float:
        """
        Calculates and returns the average transaction amount for a specific transaction type.

        Parameters:
            transaction_type (str): The type of financial transaction.

        Returns:
            float: The average transaction amount.
        """
        total_amount = self._transaction_statistics[transaction_type]["total_amount"]
        transaction_count = self._transaction_statistics[transaction_type]["transaction_count"]

        if transaction_count == 0:
            average = 0
        else:
            average = total_amount / transaction_count

        return average
