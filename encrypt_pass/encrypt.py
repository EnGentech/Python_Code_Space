import json
import os
from random import randint, choice
import string

passwordBank = {}
path = "passDir.json"
settr = randint(1, 9)
character = string.punctuation + string.ascii_letters
hashBit = 64

def getPreviousPass():
    testPath = os.path.exists(path)
    if testPath:
        with open(path, "r") as fp:
            data = json.load(fp)
            passwordBank.update(data)

def encryptPass(password):
    newPass = []
    [newPass.append(ord(each) + settr) for each in password]
    encryptedPass = []
    [encryptedPass.append(choice(character)) for times in range(settr)]
    [encryptedPass.append(chr(each)) for each in newPass]
    encryptedPass.insert(settr, str(settr))
    if len(encryptedPass) == hashBit:
        newPassword = "".join(encryptedPass)
    else:
        extras = hashBit - len(encryptedPass)
        [encryptedPass.append(choice(character)) for times in range(extras)]
        encryptedPass.append(str(len(password)))
        newPassword = "".join(encryptedPass)
    return newPassword

def decryptPass(username, password):
    hashedPassword = passwordBank[username]
    for findIndex in hashedPassword:
        try:
            if isinstance(int(findIndex), int):
                index = findIndex
                break
        except Exception:
            pass
    pointCheck = hashedPassword[-2:]
    addPoint = []
    for x in pointCheck:
        try:
            if isinstance(int(x), int):
                addPoint.append(x)
        except Exception:
            continue
    if len(addPoint) > 1:
        combine = addPoint[0] + addPoint[1]
        trueLength = int(combine)
    else:
        trueLength = int(addPoint[0])
    obtainPass = passwordBank[username][int(index) + 1: int(index) + len(password) + 1]
    if len(obtainPass) < trueLength:
        return False
    newPass = []
    [newPass.append(ord(each) - int(index)) for each in obtainPass]
    encryptedPass = []
    [encryptedPass.append(chr(each)) for each in newPass]
    validatedPassword = "".join(encryptedPass)
    if password == validatedPassword:
        return True

def createPass():
    name = input("Enter username: ")
    while True:
        password = input("Enter password: ")
        confirmPass = input("Confirm password: ")
        if password == confirmPass:
            password = encryptPass(password)
            getPreviousPass()
            passwordBank[name] = password
            with open("passDir.json", "w") as f:
                json.dump(passwordBank, f)
            break
        else:
            message = "Password do not match, try again!"
            print("*" * len(message))
            print(message)
            print()
            
    print("Successful")

def login(username, password):
    getPreviousPass()
    if username in passwordBank:
        validatePassword = decryptPass(username, password)
        if validatePassword:
            print("Login Successful")
        else:
            print("Invalid Password")
    else:
        print("User does not exist")


login("test", "pa$$word. ")
login("gentle", "admin@12345")
# createPass()
