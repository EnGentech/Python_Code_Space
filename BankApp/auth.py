from jsonSerializer import JsonSerializers as bank
import os
from csvSerializer import CSVSerializers as loadData
from time import sleep
from transactions import Transaction
from register import Registration


class AuthEngine:
    """This class manages user authentications"""

    def __init__(self):
        pass

    def reset(self, accountNumber, amount=None):
        """Reset User withdrawal pin"""
        while True:
            reset = input("Would you love to reset your password [enter yes or no]$ ")
            if reset.lower() == "yes":
                print()
                print("Please provide some security checks for account authentication".center(100))
                print("You will need to provide at least two correct answers from the questions below".center(100))
                userName = input("\nEnter your Username$ ")
                passkey = input("Enter your passkey$ ")
                dob = Registration.validateDateOfBirth()
                data = loadData().loadCSV()
                authData = bank().loadData()
                count = 0
                for datas in data:
                    if accountNumber in datas[9]:
                        if userName.lower() == datas[2].lower():
                            count += 1
                        if dob == datas[4]:
                            count += 1
                        if passkey.lower() == authData[accountNumber]['passkey'].lower():
                            count += 1
                if count >= 2:
                    print()
                    print("Your details have been verified, reset pin".center(100))
                    while True:
                        print("Please set up authentication pin (only 4 numeric digits are allowed)".center(100))
                        getPassword = input("Enter pin$ ")
                        if len(getPassword) == 4:
                            try:
                                getPassword = int(getPassword)
                                confirmation = input("Please confirm Password$ ")
                                if getPassword == int(confirmation):
                                    from main import MainExec
                                    updateData = MainExec().bankData()
                                    updateData[accountNumber]['auth'] = getPassword
                                    updateData[accountNumber]['barred'] = 0
                                    bank().dumpData(updateData)
                                    print("Your authentication pin has been reset".center(100))
                                    print("You will be redirected in 4 seconds".center(100))
                                    sleep(4)
                                    os.system('cls' if os.name == "nt" else 'clear')
                                    if amount:
                                        return Transaction(accountNumber, amount=amount).withdraw()
                                    else:
                                        return MainExec().getBalance(accountNumber)
                            except ValueError:
                                print("Only Numeric input are allowed, please try again")
                else:
                    print()
                    print("You details are not verifiable, you will be logged out in 5 seconds".center(100))
                    print("Exiting...")
                    sleep(5)
                    os.system("cls" if os.name == 'nt' else "clear")
                    print("Welcome to First Bank, enter run to start the app or exit to quit.".center(100))
                    return False
            elif reset.lower() == "no":
                os.system("cls" if os.name == 'nt' else "clear")
                print("Welcome to First Bank, enter run to start the app or exit to quit.".center(100))
                return False
            else:
                print('Invalid Selection, try again'.center(100))
