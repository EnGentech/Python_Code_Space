from sys import argv
import os

if len(argv) < 3:
    print("Sorry, args not enough\n")
else:
    sign = argv[2]
    val1 = int(argv[1])
    val2 = int(argv[3])
    if sign == "+":
        ans = val1 + val2
        os.system("cls")
        print("Sum of {} + {} = {}\n".format(val1, val2, ans))

    elif sign == "-":
        ans = val1 - val2
        print("Subtraction of {} - {} = {}\n".format(val1, val2, ans))
    elif sign == "*":
        ans = val1 * val2
        print("Product of {} * {} = {}\n".format(val1, val2, ans))
    elif sign == "/":
        ans = val1 / val2
        print("Division of {} / {} = {}\n".format(val1, val2, ans))
    elif sign == "%":
        ans = val1 % val2
        print("Mod of {} % {} = {}\n".format(val1, val2, ans))
    else:
        print("Invalid query\n")
