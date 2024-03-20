import unittest
from unittest import TestCase
from unittest.mock import patch, mock_open
from input_handler.input_handler import InputHandler


class InputHandlerTests(TestCase):
    """
    Unit tests for the InputHandler class.
    """

    def setUp(self):
        # Arrange
        self.test_csv_file = 'test_data.csv'
        self.test_json_file = 'test_data.json'

    def tearDown(self):
        # Arrange
        import os
        try:
            os.remove(self.test_csv_file)
            os.remove(self.test_json_file)
        except FileNotFoundError:
            pass

    def test_get_file_format_with_proper_extension(self):
        # Arrange
        input_handler = InputHandler('example.csv')

        # Act
        result = input_handler.get_file_format()

        # Assert
        self.assertEqual(result, 'csv')

    def test_get_file_format_with_no_extension(self):
        # Arrange
        input_handler = InputHandler('example.')

        # Act
        result = input_handler.get_file_format()

        # Assert
        self.assertEqual(result, '')

    @patch("builtins.open",
           new_callable=mock_open,
           read_data='Name,Age\nJohn,25\nJane,30\n')
    def test_read_csv_data_with_populated_file(self, mock_file_open):
        # Arrange
        input_handler = InputHandler(self.test_csv_file)

        # Act
        data = input_handler.read_csv_data()

        # Assert
        self.assertEqual(data, [{'Name': 'John',
                                 'Age': '25'},
                                {'Name': 'Jane', 'Age': '30'}])
        mock_file_open.assert_called_once_with(self.test_csv_file, 'r')

    @patch("builtins.open", new_callable=mock_open, read_data='')
    def test_read_csv_data_with_empty_file(self, mock_file_open):
        # Arrange
        input_handler = InputHandler(self.test_csv_file)

        # Act
        data = input_handler.read_csv_data()

        # Assert
        self.assertEqual(data, [])
        mock_file_open.assert_called_once_with(self.test_csv_file, 'r')

    #@patch("builtins.open")
    def test_read_csv_data_with_nonexistent_file(self):
        # Arrange
        input_handler = InputHandler('nonexistent.csv')

        # Act
        with self.assertRaises(FileNotFoundError) as context:
            result = input_handler.read_csv_data()

            # Assert
            self.assertEqual(result,
                         "File nonexistent.csv does not exists")

    @patch.object(InputHandler,
                  'read_csv_data',
                  return_value=[{'Name': 'John', 'Age': '25'},
                                {'Name': 'Jane', 'Age': '30'}])
    def test_read_input_data_with_valid_csv_file(self,
                                                 mock_read_csv_data):
        # Arrange
        input_handler = InputHandler(self.test_csv_file)

        # Act
        data = input_handler.read_input_data()

        # Assert
        self.assertEqual(data,
                         [{'Name': 'John', 'Age': '25'},
                          {'Name': 'Jane', 'Age': '30'}])
        mock_read_csv_data.assert_called_once()

    def test_read_input_data_with_invalid_extension(self):
        # Arrange
        input_handler = InputHandler('invalid.txt')

        # Act
        data = input_handler.read_input_data()

        # Assert
        self.assertEqual(data, [])

    input_data = ("Name,Account number,Transaction"
                  "type,Amount\nHannah,220,deposit,"
                  "text\nGentle,220,deposit,1000")

    @patch('builtins.open',
           new_callable=mock_open,
           read_data=input_data)
    def test_data_validation_with_non_numeric_amount(self,
                                                     mock_file_open):
        # Arrange
        expected_result = [
            {"Name": "Gentle",
             "Account number": "220",
             "Transaction type": "deposit",
             "Amount": 1000}
        ]

        # Act
        with patch.object(InputHandler,
                          'read_input_data',
                          return_value=[
                              {"Name": "Hannah",
                               "Account number": "220",
                               "Transaction type": "deposit",
                               "Amount": "text"},
                              {"Name": "Gentle",
                               "Account number": "220",
                               "Transaction type": "deposit",
                               "Amount": 1000}
                          ]):
            validate = InputHandler('mock_file')
            obtained = validate.data_validation()

        # Assert
        self.assertEqual(obtained, expected_result)

    input_data = ("Name,Account number,"
                  "Transaction type,Amount\nHannah,"
                  "220,deposit,-4000\nGentle,220,deposit,1000")

    @patch('builtins.open',
           new_callable=mock_open,
           read_data=input_data)
    def test_data_validation_with_negative_amount(self,
                                                  mock_file_open):
        # Arrange
        expected_result = [
            {"Name": "Gentle",
             "Account number": "220",
             "Transaction type": "deposit",
             "Amount": 1000}
        ]

        # Act
        with patch.object(InputHandler,
                          'read_input_data',
                          return_value=[
                              {"Name": "Hannah",
                               "Account number": "220",
                               "Transaction type": "deposit",
                               "Amount": "text"},
                              {"Name": "Gentle",
                               "Account number": "220",
                               "Transaction type": "deposit",
                               "Amount": 1000}
                          ]):
            validate = InputHandler('mock_file')
            obtained = validate.data_validation()

        # Assert
        self.assertEqual(obtained, expected_result)

    input_data = ("Name,Account"
                  "number,Transaction type,Amount\nHannah,"
                  "220,depo,3000\nGentle,220,deposit,1000")

    @patch('builtins.open',
           new_callable=mock_open,
           read_data=input_data)
    def test_data_validation_with_invalid_transaction_type(self,
                                                           mock_file_open):
        # Arrange
        expected_result = [
            {"Name": "Gentle",
             "Account number": "220",
             "Transaction type": "deposit", "Amount": 1000}
        ]

        # Act
        with patch.object(InputHandler,
                          'read_input_data',
                          return_value=[
                              {"Name": "Hannah",
                               "Account number": "220",
                               "Transaction type": "deposit",
                               "Amount": "text"},
                              {"Name": "Gentle",
                               "Account number": "220",
                               "Transaction type": "deposit",
                               "Amount": 1000}
                ]):
            validate = InputHandler('mock_file')
            obtained = validate.data_validation()

        # Assert
        self.assertEqual(obtained, expected_result)


if __name__ == "__main__":
    unittest.main()
