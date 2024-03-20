import csv
import json


class InputHandler:
    """
    A class for handling input data from CSV or JSON files.

    Attributes:
        _file_path (str): The path to the input file.
    """

    def __init__(self, file_path: str):
        """
        Initializes an InputHandler class object.

        Parameters:
            file_path (str): The path to the input file.
        """
        self._file_path = file_path

    def get_file_format(self) -> str:
        """
        Gets the format of the input file.

        Returns:
            str: The file format (e.g., 'csv', 'json').
        """
        # return a string datatype of a file extension
        return self._file_path.split('.')[-1]

    def read_input_data(self) -> list:
        """
        Reads and returns input data from either a CSV or JSON file.

        Returns:
            list: The input data read from the file.
        """
        data = []
        file_format = self.get_file_format()
        if file_format == 'csv':
            data = self.read_csv_data()
        elif file_format == 'json':
            data = self.read_json_data()
        return data

    def read_csv_data(self) -> list:
        """
        Reads and returns input data from a CSV file.

        Returns:
            list: The input data read from the CSV file.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        input_data = []
        try:
            with open(self._file_path, 'r') as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    input_data.append(row)
            return input_data

        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self._file_path} does not exist.")

    def read_json_data(self) -> list:
        """
        Reads and returns input data from a JSON file.

        Returns:
            list: The input data read from the JSON file.

        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        # Research the json.load function so that you
        # understand the format of the data once it is
        # placed into input_data
        try:

            with open(self._file_path, 'r') as input_file:
                input_data = json.load(input_file)

            return input_data
        except FileNotFoundError:
            raise FileNotFoundError(f"File: {self._file_path} does not exist.")

    def data_validation(self):
        """
        This function reads the data content
        Return:
            returns a valid transaction
        parameter:
            data: value to be validated
        """
        valid_data = []
        transaction_type = ['withdrawal', 'deposit', 'transfer']
        for value in self.read_input_data():
            try:
                if float(value['Amount']) >= 0 \
                        and value['Transaction type'] in transaction_type:
                    valid_data.append(value)
            except ValueError:
                pass
        return valid_data
