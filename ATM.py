# Kalen & Sophia - 7/2/2021

import time
import math

username = "Apple72"
pin = "5254"

spend = 750
growth = 1250
reserve = 1750

def uinput(string):
    return input(string + " ")

def fitRequirements(question,type, typeName):
    req = uinput(question)
    canContinue = False
    while canContinue == False:
        try:
            req = type(req)
            canContinue = True
        except:
            req = uinput("Please enter a valid " + typeName + ". " + question)
    return req

def coinToString(coin, amt, money):
    money = math.floor(money*100)/100
    string = ""
    if amt > 1:
        if money > 0:
            string += f"{amt} {coin}s,\n"
        elif coin != "Penny":
            string += f"{amt} {coin}s."
        else:
            string += f"{amt} pennies."
    elif amt == 1:
        if money > 0:
            string += f"{amt} {coin},\n"
        else:
            string += f"{amt} {coin}."
    return string

def efficientChange(money):
    changeStr = f""
    hundreds = math.floor(money/100)
    money -= (hundreds*100)
    changeStr += coinToString("100", hundreds, money)
    fifties = math.floor(money/50)
    money -= (fifties*50)
    changeStr += coinToString("50", fifties, money)
    twenties = math.floor(money/20)
    money -= (twenties*20)
    changeStr += coinToString("20", twenties, money)
    tens = math.floor(money/10)
    money -= (tens*10)
    changeStr += coinToString("10", tens, money)
    fives = math.floor(money/5)
    money -= (fives*5)
    changeStr += coinToString("5", fives, money)
    dollars = math.floor(money/1)
    money -= (dollars*1)
    changeStr += coinToString("1", dollars, money)
    quarters = math.floor(money/0.25)
    money -= (quarters*0.25)
    changeStr += coinToString("Quarter", quarters, money)
    dimes = math.floor(money/0.1)
    money -= (dimes*0.1)
    changeStr += coinToString("Dime", dimes, money)
    nickels = math.floor(money/0.05)
    money -= (nickels*0.05)
    changeStr += coinToString("Nickel", nickels, money)
    pennies = math.floor(money*100)
    money = 0
    changeStr += coinToString("Penny", pennies, money)
    
    return changeStr

print("Welcome to Kalen and Sophia's ATM!")
enteredUsername = uinput("Please enter your username:")
enteredPin = uinput("Please enter your PIN:")
while enteredUsername != username or enteredPin != pin:
    print("Invalid username or PIN. Please try again.")
    enteredUsername = uinput("Please enter your username:")
    enteredPin = uinput("Please enter your PIN:")
print("Log-in successful.")
run = True
while run == True:
    choice = input("\n\nWhat would you like to do?\n\nA. Show my account balance\nB. Withdraw money\nC. Deposit money\nD. Cancel\n\n").upper()
    
    if choice == "A": # Show my account balance
        print(f"Account Balances:\n\nSpend Account: ${spend:.2f}\nGrowth Account: ${growth:.2f}\nReserve Account: ${reserve:.2f}")
        time.sleep(2)
    elif choice == "B": # Withdraw money
        account = input(f"What account would you like to withdraw from?\n\nA. Spend Account (${spend:.2f})\nB. Growth Account (${growth:.2f})\nC. Reserve Account (${reserve:.2f})\n\n").upper()
        while account != "A" and account != "B" and account != "C":
            account = input(f"Sorry, \"{account}\" is not an option.\nWhat account would you like to withdraw from?\n\nA. Spend Account (${spend:.2f})\nB. Growth Account (${growth:.2f})\nC. Reserve Account (${reserve:.2f})\n\n").upper()
        if account == "A": # Spend
            amt = fitRequirements("How much do you want to withdraw?", float, "float")
            if amt <= spend:
                spend -= amt
                print(f"${amt:.2f} withdrawn from your Spend account.\nMoney Withdrawn:\n\n{efficientChange(amt)}")
            else:
                print(f"Insufficient funds. (${spend:.2f})")
        elif account == "B": # Growth
            amt = fitRequirements("How much do you want to withdraw?", float, "float")
            if amt <= growth:
                growth -= amt
                print(f"${amt:.2f} withdrawn from your Growth account.\nMoney Withdrawn:\n\n{efficientChange(amt)}")
            else:
                print(f"Insufficient funds. (${growth:.2f})")
        elif account == "C": # Reserve
            amt = fitRequirements("How much do you want to withdraw?", float, "float")
            if amt <= reserve:
                reserve -= amt
                print(f"${amt:.2f} withdrawn from your Reserve account.\nMoney Withdrawn:\n\n{efficientChange(amt)}")
            else:
                print(f"Insufficient funds. (${reserve:.2f})")
    elif choice == "C": # Deposit money
        account = input(f"What account would you like to deposit to?\n\nA. Spend Account (${spend:.2f})\nB. Growth Account (${growth:.2f})\nC. Reserve Account (${reserve:.2f})\n\n").upper()
        while account != "A" and account != "B" and account != "C":
            account = input(f"Sorry, \"{account}\" is not an option.\nWhat account would you like to deposit to?\n\nA. Spend Account (${spend:.2f})\nB. Growth Account (${growth:.2f})\nC. Reserve Account (${reserve:.2f})\n\n").upper()
        if account == "A": # Spend
            amt = fitRequirements("How much do you want to deposit?", float, "float")
            spend += amt
            print(f"${amt:.2f} deposited to your Spend account.")
        elif account == "B": # Growth
            amt = fitRequirements("How much do you want to deposit?", float, "float")
            growth += amt
            print(f"${amt:.2f} deposited to your Growth account.")
        elif account == "C": # Reserve
            amt = fitRequirements("How much do you want to deposit?", float, "float")
            reserve += amt
            print(f"${amt:.2f} deposited to your Reserve account.")
    elif choice == "D": # Cancel
        run = False
    else: # Sophia
        print(f"Sorry, {username}. \"{choice}\" is not an option.")