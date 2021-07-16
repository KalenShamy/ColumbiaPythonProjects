# Kalen Shamy - 7/1/2021

import math

def uinput(string):
    return input(string + " ")

cookieCost = 2.50

currencies = {"EUR": 0.84,
              "CAD": 1.24,
              "JPY": 111.39,
              "CNY": 6.46,
              "GBP": 0.73,
              "CHF": 0.93,
              "AUD": 1.34,
              "HKD": 7.77,
              "NZD": 1.43,
              "BTC": 0.00003,
              "ETH": 0.00005,
              "LTC": 0.00732,
              "BCH": 0.00311,
              "ADA": 0.7425}

numOfCurrencies = len(currencies)

def strOfCurrencies(connector):
    i = 0
    string = ""
    for sym, conv in currencies.items():
        i+=1
        if i == numOfCurrencies:
            string += f"{connector} {sym}"
        else:
            string += f"{sym}, "
    return string

def coinToString(coin, amt, money):
    money = math.floor(money*100)/100
    string = ""
    if amt > 1:
        if money > 0:
            string += f"{amt} {coin}s, "
        elif coin != "penny":
            string += f"{amt} {coin}s."
        else:
            string += f"{amt} pennies."
    elif amt == 1:
        if money > 0:
            string += f"{amt} {coin}, "
        else:
            string += f"{amt} {coin}."
    return string

def efficientChange(money):
    changeStr = f""
    dollars = math.floor(money/1)
    money -= (dollars*1)
    changeStr += coinToString("dollar", dollars, money)
    quarters = math.floor(money/0.25)
    money -= (quarters*0.25)
    changeStr += coinToString("quarter", quarters, money)
    dimes = math.floor(money/0.1)
    money -= (dimes*0.1)
    changeStr += coinToString("dime", dimes, money)
    nickels = math.floor(money/0.05)
    money -= (nickels*0.05)
    changeStr += coinToString("nickel", nickels, money)
    pennies = math.floor(money*100)
    money -= (pennies*0.01)
    changeStr += coinToString("penny", pennies, money)
    
    return(changeStr)

currency = uinput(f"Which currency do you have? We accept {strOfCurrencies('and')}.")
canContinue = False
while canContinue == False:
    for sym, conv in currencies.items():
        if currency.upper() == sym:
            canContinue = True
    if canContinue == False:
        currency = uinput(f"Sorry, we only accept {strOfCurrencies('and')}. Which would you like to use?")
amt = uinput(f"How much {currency} do you have? (Decimals accepted)")
canContinue = False
while canContinue == False:
    try:
        amt = float(amt)
        if amt < currencies[currency]:
            print(f"Sorry, the minimum payment is {currencies[currency]*cookieCost} {currency} (${cookieCost} USD). Please come again next time!")
            break
        canContinue = True
    except ValueError:
        amt = uinput(f"Please enter a valid number. How much {currency} do you have?")
if canContinue == True:
    usd = math.floor((amt/currencies[currency])*100)/100
    print(f"{amt} {currency} converted to USD is ${usd:.2f}.")
    cookies = uinput(f"How many cookies do you want? You can buy {math.floor(usd/cookieCost)}.")
    canContinue = False
    while canContinue == False:
        try:
            cookies = int(cookies)
            if math.floor(usd/cookieCost) < cookies:
                cookies = uinput(f"You don't have enough money to buy {cookies}. The most you can buy is {math.floor(usd/cookieCost)}. How many do you want to buy?")
            else:
                print(f"You have purchased {cookies} cookies! Your change of ${math.floor((usd-(cookieCost*cookies))*100)/100:.2f} will be given to you in {efficientChange(usd-(cookieCost*cookies))}")
                canContinue = True
        except ValueError:
            cookies = uinput(f"Please enter a valid number. How many cookies do you want? You can buy {math.floor(usd/cookieCost)}.")
