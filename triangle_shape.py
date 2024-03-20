def triangle():
    try:
        trigle = int(input("Enter an odd number$ "))
        if trigle % 2 == 0:
            print("== Invalid, only odd numbers are allowed ==")
            triangle()
        else:
            space = 0
            for x in range(trigle, 0, -2):
                print("  " * space + "* " * x)
                space = space + 1
    except ValueError:
        print("== Only Odd integers are allowed ==")
        triangle()


triangle()