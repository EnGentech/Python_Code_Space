import random
import time
import os
"""The ludo dice game"""

global lis
lis = ['toss', 'quit']


def check(command):
    while True:
        if command not in lis:
            print("Invalid input, try again")
            command = input("Enter command\t")

        elif command in lis:
            print("")
            ludo(command)

def ludo(use):
    while True:
        if use == lis[0]:
            num1 = random.randint(1, 6)
            num2 = random.randint(1, 6)
            print("processing")
            time.sleep(2)
            print("You tossed  {} : {}".format(num1, num2))
            print("")
            use = input("Enter command\t")
        elif use == lis[1]:
            print("GoodBye, See you next time")
            exit(98)
        else:
            print("")
            check(use)


print("Please enter toss to toss dice or quit to quit game")
print("Please wait while processing the game")
time.sleep(3)
os.system('cls')


command = input("Enter command\t")
check(command)