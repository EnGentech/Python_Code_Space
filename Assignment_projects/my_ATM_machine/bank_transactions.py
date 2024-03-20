from random import uniform
import os
from time import sleep

randomNumber = uniform(-1000, 10000)
amount = randomNumber
while True:
    def center(char):
        """position values within a 40 character screen resolution"""
        lengthOfCharacter = len(char)
        difference = 40 - lengthOfCharacter
        space = difference // 2
        return " " * space + char

    bankingOption = ['D', 'W', 'Q']
    line = '*' * 40
    transaction_amount = "Enter amount of transaction: "

    print(line + '\n', center('PIXEL RIVER FINANCIAL\n'), center('ATM Simulator'))
    print(center(f'Your current balance is: ${amount:,.2f}\n'))
    print(center(f"Deposit: D") + '\n' + center(f'Withdraw: W') + '\n' + center(f'To Quit: Q') + '\n' + line)

    prompt = input("Enter your selection: ")
    if prompt.upper() not in bankingOption:
        print(line + '\n', center('INVALID SELECTION'), '\n' + line)

    elif prompt.upper() == 'D':
        prompt = float(input(transaction_amount))
        amount += prompt
        print(line + '\n', center(f'Your current balance is: ${amount:,.2f}'), '\n' + line)

    elif prompt.upper() == 'W':
        prompt = float(input(transaction_amount))
        if prompt < 0:
            print(line + '\n', center('NEGATIVE NUMBER NOT ALLOWED'), '\n' + line)
        elif prompt > amount:
            print(line + '\n', center('INSUFFICIENT FUND'), '\n' + line)
        else:
            amount -= prompt
            print(line + '\n', center(f'Your current balance is: ${amount:,.2f}'), '\n' + line)
    elif prompt.upper() == 'Q':
        exit()

    sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
