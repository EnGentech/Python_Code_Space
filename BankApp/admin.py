def phoneNumber():
    try:
        number = int(input("Enter your phone number$: "))
        convertNumber = str(number)
        if len(convertNumber) == 11 and (convertNumber[0] == '0'):
            print()
            return convertNumber
        else:
            print("Phone number must be 11 digits and must begin with 0")
    except ValueError:
        print("Only numeric values are allowed")

phoneNumber()