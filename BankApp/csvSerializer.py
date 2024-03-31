import csv

class CSVSerializers:
    """Define a method to serialize csv data"""

    def __init__(self):
        pass

    def loadCSV(self):
        """load all csv data and return list"""
        csvData = []
        with open('account_users.csv', 'r') as file:
            data = csv.reader(file)
            for datas in data:
                csvData.append(datas)

        return csvData
