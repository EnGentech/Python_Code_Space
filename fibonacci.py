num = int(input("Fibonacci range$ "))
a = 0
b = 1
for x in range(num):
    if x <= 1:
        print(x, end=" ")
    else:
        c = a + b
        a, b = b, c
        print(c, end=" ")