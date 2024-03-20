import re
import os

def passwrd():
    pattern = re.compile("[a-zA-Z\\d+]{4,8}")
    password = input("Enter password$ ")
    check = pattern.match(password)

    if check:
        with open("password.txt", 'w', encoding='utf8') as pas:
            pas.write(password)
            print("\n== Sign_Up Successful ==")
    else:
        print("Invalid password provided")
        passwrd()

print("== Welcome, please sign up ==")
username = input("Enter username$ ")

chkexist = os.path.exists("username.txt")

if chkexist:
    with open("username.txt", 'r', encoding='utf8') as name:
        check = name.read()
    if check == username:
        print("Username already exist\nPlease use the login platform")
    else:
        with open("username.txt", 'w', encoding='utf8') as name:
            name.write(username)
        passwrd()
