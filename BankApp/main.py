from transactions import Transaction
from register import Registration
import os
import csv
from jsonSerializer import JsonSerializers as bank
from auth import AuthEngine

class MainExec:

    def __init__(self):
        pass

    def bankData(self):
        data = bank().loadData()
        return data
    
    def newRegister(self):
        Registration.register()

    def getDeposit(self, accountNumber, amount):
        Transaction(accountNumber=accountNumber, amount=amount).deposit()
    
    def getWithdrawal(self, accountNumber, amount):
        Transaction(accountNumber=accountNumber, amount=amount).withdraw()

    def getBalance(self, accountNumber):
        Transaction(accountNumber=accountNumber, amount=None).checkBalance()

    def validateBarred(self, accountNumber):
        """validate if user has been barred or not"""
        try:
            barredStatus = self.bankData()[accountNumber]['barred']
            if barredStatus == 1:
                return True
        except KeyError:
            pass

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

    def checkWithdrawalPin(self, accountNumber, pin):
        """Confirm if pin is available in database"""
        if accountNumber in self.bankData():
            accountPin = self.bankData()[accountNumber]['auth']
            try:
                pin = int(pin)
                if accountPin == pin:
                    return True
                else:
                    print("Invalid pin")
            except ValueError:
                pass

    def validateAuth(self, accountNumber):
        """this function will validate users authenticity"""
        if accountNumber in self.bankData():
            password = self.bankData()[accountNumber]['auth']
            if password == None:
                while True:
                    print("Please set up withdrawal pin (only 4 numeric digits are allowed)".center(100))
                    getPassword = input("Enter pin$ ")
                    if len(getPassword) == 4:
                        try:
                            getPassword = int(getPassword)
                            confirmation = input("Please confirm Password$ ")
                            if getPassword == int(confirmation):
                                passkey = input("Enter your passkey [Note this will be used in case you forget your password]$ ")
                                updateData = self.bankData()
                                updateData[accountNumber]['auth'] = getPassword
                                updateData[accountNumber]['passkey'] = passkey
                                bank().dumpData(updateData)
                                print("You have successfully registered a withdrawal pin, proceed to withdrawal".center(100))
                                confirmation = self.checkWithdrawalPin(accountNumber, getPassword)
                                if confirmation:
                                    return True
                            else:
                                print("Password does not match")
                        except ValueError:
                            print("Only Numberic input are allowed, please try again")
                    else:
                        print("You must enter only 4 digit numeric pin\n")
            else:
                count = 3
                while True:
                    pin = input("Enter authentication pin$ ")
                    confirmation = self.checkWithdrawalPin(accountNumber, pin)
                    if confirmation:
                        return True
                    count -= 1
                    if count == 0:
                        print()
                        print('You have exceeded your limit, you are now barred from this service, reset your pin to continue'.center(100))
                        data = self.bankData()
                        data[accountNumber]['barred'] = 1
                        bank().dumpData(data)
                        break
                    print(f"Invalid pin you have {count} more attempt".center(100))
        else:
            print("Account Number not found")


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
                    amount = input("Enter the amount you want to Withdraw: ")
                    checkValidation = self.validateBarred(accountNumber)
                    if checkValidation:
                        print()
                        print("This account Number has been barred".center(100))
                        response = AuthEngine().reset(accountNumber, amount=amount)
                        if response == False:
                            return False
                    validate = self.validateAuth(accountNumber)
                    try:
                        accountNumber = int(accountNumber)
                        amount = int(amount)
                        if validate:
                            self.getWithdrawal(accountNumber, amount)

                    except ValueError:
                        print("Only numeric input is allowed".center(100))
                elif select == 4:
                    accountNumber = input("Enter your account number: ")
                    checkValidation = self.validateBarred(accountNumber)
                    if checkValidation:
                        print()
                        print("This account Number has been barred".center(100))
                        response = AuthEngine().reset(accountNumber)
                        if response == False:
                            return False
                    validate = self.validateAuth(accountNumber)
                    try:
                        accountNumber = int(accountNumber)
                        if validate:
                            self.getBalance(accountNumber)
                    except ValueError:
                        print("Only numeric input is allowed".center(100))
                elif select == 5:
                    self.getAccountNumber()
                elif select == 6:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Welcome to First Bank, enter run to start the app or exit to quit.".center(100))
                    break
                else:
                    print("Invalid selection".center(100))
            except ValueError:
                print("only numeric input is allowed".center(100))

# if __name__ == "__main__":
#     runBankApp = MainExec()
#     os.system('cls' if os.name == 'nt' else 'clear')
#     runBankApp.run()