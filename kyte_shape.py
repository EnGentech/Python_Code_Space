def kyte_shape():
    try:
        trigle = int(input("Enter an odd number$ "))
        if trigle % 2 == 0:
            print("== Invalid, only odd numbers are allowed ==")
            kyte_shape()
        else:
            top_space = int(trigle/2)
            for x in range(1, trigle, 2):
                print("  " * top_space + "* " * x)
                top_space = top_space - 1
            space = 0
            for x in range(trigle, 0, -2):
                print("  " * space + "* " * x)
                space = space + 1
    except ValueError:
        print("== Only Odd integers are allowed ==")
        kyte_shape()


kyte_shape()