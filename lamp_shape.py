import pyinputplus
from time import sleep
import os

def check():
    print("== Only odd numbers above 9 are allowed ==")
    a = pyinputplus.inputInt("Enter shape size$ ")

    if a % 2 != 1 or a < 9:
        check()
    else:
        os.system('cls')
        space = 0
        decrementor = a
        for x in range(0, a, 2):
            print(" "*space + " *"*decrementor)
            sleep(0.5)
            space += 2
            decrementor -= 2

        space = int((a-3))
        incrementor = 3
        for x in range(a-1, 0, -2):
            print(" "*space + " *"*incrementor)
            sleep(0.5)
            space -= 2
            incrementor += 2

        big = "\n== THE BIG TEAM TREE =="

        for x in range(len(big)):
            sleep(0.3)
            print(big[x], end="")

        print("\n_________________________")
check()

