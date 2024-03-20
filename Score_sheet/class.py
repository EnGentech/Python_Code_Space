from sys import argv
num1 = int(argv[1])
sign = argv[2]
num2 = int(argv[3])
if sign == "+":
    sum = num1 + num2
elif   sign == "-":
    sum = num1 - num2
elif sign == "/":
    sum = num1 / num2

print(sum)