def prime_number():
    try:
        prim = int(input("Prime_Number$ "))
        prime = 0
        for a in range(prim):
            if a <= 2:
                print(a, end=" ")
            else:
                for x in range(2, a):
                    if a % x == 0:
                        prime = 1
                        break
                    else:
                        prime = 0
                if prime == 0:
                    print(a, end=" ")
    except ValueError:
        print("== Only Integer variable are allowed ==")
        prime_number()


prime_number()
