import os
import random
import time
import json

balance = 1000


def clear():
    os.system("cls")


def home():
    print("[1] Sign Up\n[2] Login")
    homein = input("[>] ")
    if homein == "1":
        clear()
        signup()
    elif homein == "2":
        clear()
        login()
    else:
        clear()
        print("Incorrect operation")
        time.sleep(3)
        clear()
        home()


def signup():
    print("Sign Up")
    signupuser = input("Enter your username: ")
    signuppass = input("Enter your password: ")
    with open("gamble.json") as file:
        data = json.load(file)
    data[signupuser] = {"password": signuppass}
    data["balance"] = balance
    with open("gamble.json", "w") as file:
        json.dump(data, file, indent=4)
    print("You have been registered!")
    time.sleep(2)
    clear()
    print("Redirecting to login")
    time.sleep(2)
    clear()
    login()


def login():
    print("Login")
    user = input("Enter your username: ")
    passs = input("Enter your password: ")
    with open("gamble.json") as file:
        data = json.load(file)
    if passs == data[user]["password"]:
        clear()
        print("Access granted")
        time.sleep(2)
        clear()
        gamble()
    else:
        clear()
        print("Incorrect login details")
        time.sleep(3)
        clear()
        login()


def gamble():
    global balance
    print(f"Balance: {balance}")
    print("How much do you want to bet?")
    money = int(input("[>]"))
    guidelines = "Enter a number between 1 and 20 to compete with the bot"
    print(guidelines)
    h = int(input("[>] "))
    f = random.randint(1, 20)
    if h == f:
        clear()
        print("You guess right!")
        balance = int(balance) + int(money)
        print(f"You have {balance} dollars")
        time.sleep(2)
        clear()
        gamble()
    elif h > 20:
        clear()
        print("Enter a number less than 20 please!")
        time.sleep(2)
        clear()
        gamble()
    else:
        clear()
        print("You guess wrong!Try again.")
        balance = int(balance) - int(money)
        print(f"I guessed {f}")
        print(f"You have {balance} dollars")
        time.sleep(2)
        clear()
        gamble()


home()