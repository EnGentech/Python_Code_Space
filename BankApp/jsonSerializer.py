import json

class JsonSerializers:
    """This class is written to serialize my bank application"""

    def __init__(self):
        pass

    def loadData(self):
        """This method loads data from the bank application"""
        with open("auth.json", 'r') as file:
            data = json.load(file)
        return data

    def dumpData(self, data):
        """Use this method to dump all data in json"""
        with open('auth.json', 'w') as file:
            json.dump(data, file)
