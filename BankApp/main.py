from transactions import Transaction
from register import Registration
import os
import csv

class MainExec:

    def __init__(self):
        pass
    
    def newRegister(self):
        Registration.register()

    def getDeposit(self, accountNumber, amount):
        Transaction(accountNumber=accountNumber, amount=amount).deposit()
    
    def getWithdrawal(self, accountNumber, amount):
        Transaction(accountNumber=accountNumber, amount=amount).withdraw()

    def getBalance(self, accountNumber):
        Transaction(accountNumber=accountNumber, amount=None).checkBalance()

    def getAccountNumber(self):
        userName = input("Enter your username: ")
        statuscode = 0
        with open("account_users.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if userName.lower() == row[2].lower():
                    statuscode = 1
                    print(f"Account Number: {int(row[9])}".center(100))
            if statuscode == 0:
                print("Username not found".center(100))

    def run(self):
        while True:
            print("=" * 100)
            print("Enter 1 to register, 2 to deposit, 3 to withdraw, 4 to check balance, 5 to get account Number, 6 to exit: ".center(100))
            select = input(" " * 38 + "Enter your selection: ")
            try:
                select = int(select)
                if select == 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    self.newRegister()
                elif select == 2:
                    accountNumber = input("Enter your account number: ")
                    amount = input("Enter the amount you want to deposit: ")
                    try:
                        accountNumber = int(accountNumber)
                        amount = int(amount)
                        self.getDeposit(accountNumber, amount)
                    except ValueError:
                        print("Only numeric input is allowed".center(100))
                elif select == 3:
                    accountNumber = input("Enter your account number: ")
                    amount = input("Enter the amount you want to deposit: ")
                    try:
                        accountNumber = int(accountNumber)
                        amount = int(amount)
                        self.getWithdrawal(accountNumber, amount)
                    except ValueError:
                        print("Only numeric input is allowed".center(100))
                elif select == 4:
                    accountNumber = input("Enter your account number: ")
                    try:
                        accountNumber = int(accountNumber)
                        self.getBalance(accountNumber)
                    except ValueError:
                        print("Only numeric input is allowed".center(100))
                elif select == 5:
                    self.getAccountNumber()
                elif select == 6:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    print("Invalid selection".center(100))
            except ValueError:
                print("only numeric input is allowed")

# if __name__ == "__main__":
#     runBankApp = MainExec()
#     os.system('cls' if os.name == 'nt' else 'clear')
#     runBankApp.run()