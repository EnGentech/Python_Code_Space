from datetime import date
import json
import csv
from random import randint
import re
import os
from time import sleep

class Registration: 

    def __init__(self, firstName, lastName, email, userName, address, initialDeposit, gender, dateOfBirth, BVN, phoneNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userName = userName
        self.address = address
        self.initialDeposit = initialDeposit
        self.gender = gender
        self.dateOfBirth = dateOfBirth
        self.BVN = BVN
        self.phoneNumber = phoneNumber

    
    @staticmethod
    def register():
        print("=" * 100)
        notification = "Fill in the required details below, all fields are mandatory"
        print(notification.center(100))
        print()
        firstName = Registration.validateName("first")
        lastName = Registration.validateName("last")
        userName = Registration.validateName("User")
        address = Registration.validateName("address")
        dateofBirth = Registration.validateDateOfBirth()
        bvn = Registration.numericValidation("BVN")
        phoneNumber = Registration.numericValidation("phoneNumber")
        email = Registration.emailValidation()
        initialDeposit = Registration.validateInitialDeposit()
        accountNumber = Registration.generateAccountNumber()

        # create an auth system
        with open('auth.json', 'r') as file:
            try:
                storage = json.load(file)
            except Exception:
                storage = {}

        authFile = {
            accountNumber: {
                'auth': None,
                'passkey': None,
                'barred': 0
            }
        }

        storage.update(authFile)
        with open('auth.json', 'w') as file:
            json.dump(storage, file)

        with open("account_users.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([firstName, lastName, userName, address, dateofBirth, bvn, phoneNumber, email, initialDeposit, accountNumber])
            print()
            print(("=" * 40).center(100))
            print("Account created successfully".center(100))
            print(f"Your account number is: {accountNumber}".center(100))
            print()
            sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def generateAccountNumber():
        while True:
            statusCode = 0
            accountNumber = randint(3000000001, 3999999999)
            previousAccountNumbers = Registration.getAllAccountNumbers()
            for accountDigits in previousAccountNumbers:
                if accountNumber == accountDigits:
                    statusCode = 1
                    break
            if statusCode == 0:
                return accountNumber
    
    @staticmethod
    def validateInitialDeposit():
        while True:
            amount = input("Enter the amount you want to deposit$: ")
            try:
                amount = int(amount)
                if amount < 1000:
                    print("Initial deposit must be at least 1000")
                else:
                    print()
                    return amount
            except ValueError:
                print("Only numeric values are allowed")

    @staticmethod
    def getAllAccountNumbers():
        accountNumbers = []
        with open("account_users.csv", "r") as file:
            allAccount = csv.reader(file)
            for account in allAccount:
                accountNumbers.append(account[9])
        return accountNumbers
    
    @staticmethod
    def getAllUserNames():
        userNames = []
        with open("account_users.csv", "r", newline='') as file:
            allAccount = csv.reader(file)
            for users in allAccount:
                userNames.append(users[2].lower())
        return userNames
                       

    @staticmethod
    def validateName(nameType):
        while True:
            name = input(f"Enter your {nameType} name$: ")
            if nameType == "address" and len(name) >= 5:
                print()
                return name
            elif nameType == "address" and len(name) < 5:
                print("Address must be up to or more than 5 characters")
                
            elif nameType == "User" and len(name) >= 3:
                checkExintingUserNames = Registration.getAllUserNames()
                while True:
                    if name.lower() in checkExintingUserNames:
                        number = randint(1, 99)
                        print(f"Username already exist, we suggest {name + '0'}{number}")
                        name = input(f"Enter your {nameType} name$: ")
                    else:
                        print()
                        return name
                
            elif nameType == "User" and len(name) < 3:
                print("Username must be up to or more than 3 characters")

            elif len(name) >= 3 and name.isalpha():
                print()
                return name
            elif len(name) < 3 or not name.isalpha():
                print(f"{nameType} name must be up to or more than 3 characters and must contain only alphabets")

    @staticmethod
    def numericValidation(NumType):
        while True:
            if NumType == "phoneNumber":
                try:
                    number = int(input("Enter your phone number$: "))
                    if len(str(number)) == 10:
                        print()
                        return "0" + str(number)
                    else:
                        print("Phone number must be 11 digits and must begin with 0")
                except ValueError:
                    print("Only numeric values are allowed")
            elif NumType == 'BVN':
                try:
                    bvn = int(input("Enter your BVN$: "))
                    if len(str(bvn)) == 11:
                        print()
                        return bvn
                    else:
                        print("BVN must be 11 digits")
                except ValueError:
                    print("Only numeric values are allowed")

    @staticmethod
    def validateDateOfBirth():
        today = date.today()
        presentYear = today.year 

        while True:
            dateOfBirth = input("Enter your date of birth [format dd/mm/yyyy]$: ")

            times = 0
            for x in dateOfBirth:
                if x == '/':
                    times += 1

            if len(dateOfBirth) != 10 or times != 2:
                print("Invalid date of birth")
            
            else:
                day, month, year = dateOfBirth.split('/')
                try:
                    day = int(day)
                    month = int(month)
                    year = int(year)
                    if 0 < day <= 31 and 0 < month <= 12 and year <= presentYear:
                        print()
                        return dateOfBirth
                    else:
                        print("Follow the format strictly")
                except ValueError:
                    print("Only numeric values are allowed")

    @staticmethod            
    def emailValidation():
        while True:
            email = input("Enter your email address$: ")
            pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
            if re.match(pattern, email):
                print()
                return email
            else:
                print("Invalid email address")
