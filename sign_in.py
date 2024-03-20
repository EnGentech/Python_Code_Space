import pyinputplus

uname = input("Enter your username$ ")
passwd = input("Enter your password$ ")

with open("username.txt", 'r') as fname:
    getuser = fname.read()

with open("password.txt", 'r') as fpass:
    getpas = fpass.read()

if getuser != uname and getpas != passwd:
    print("Invalid credentials\n== Sign Up please ==")
elif getuser == uname:
    if getpas == passwd:
        print("Login Successful")
    else:
        print("Incorrect password")
else:
    print("User name does not exist, \n\n== Do you wish to SignUp ==")
    value = pyinputplus.inputYesNo("Select Option 'Yes or No'$ ")