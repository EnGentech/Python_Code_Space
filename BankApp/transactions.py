import csv

class Transaction:

    def __init__(self, accountNumber, amount):
        self.accountNumber = accountNumber
        self.amount = amount

    @staticmethod
    def validateAccountNumber(accountNumber):
        accountUpdate = []
        with open("account_users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                accountUpdate.append([row[8], row[9]])
        for accNumbs in accountUpdate:
            try:
                if accountNumber == int(accNumbs[1]):
                    return True
            except ValueError:
                pass

    def deposit(self):
        validate = self.validateAccountNumber(self.accountNumber)
        if validate:
            updatedRow = []
            with open("account_users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        if self.accountNumber == int(row[9]):
                            balance = int(row[8])
                            balance += self.amount
                            row[8] = balance
                    except ValueError:
                        pass
                    updatedRow.append(row)
                with open("account_users.csv", "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(updatedRow)
                    print(f"Deposited {self.amount} into account number {self.accountNumber}".center(100))
        else:
            print("Account Number: Invalid".center(100))
    
    def withdraw(self):
        validateAccountNumber = self.validateAccountNumber(self.accountNumber)
        if validateAccountNumber:
            updatedRow = []
            netBalance = None
            with open("account_users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        if self.accountNumber == int(row[9]):
                            balance = int(row[8])
                            if balance >= self.amount:
                                balance -= self.amount
                                row[8] = balance
                                netBalance = balance
                            else:
                                print("Insufficient balance".center(100))
                                return -1
                    except ValueError:
                        pass
                    updatedRow.append(row)
                with open("account_users.csv", "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerows(updatedRow)
                    print(f"Transaction was successful, Balance: ${netBalance}".center(100))

    def checkBalance(self):
        validateAccountNumber = self.validateAccountNumber(self.accountNumber)
        if validateAccountNumber:
            with open("account_users.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    try:
                        if self.accountNumber == int(row[9]):
                            print(f"Balance for {self.accountNumber}: ${row[8]}".center(100))
                    except ValueError:
                        pass

