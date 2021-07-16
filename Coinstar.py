# Kalen Shamy - 6/29/2021

def uinput(string):
    return input(string + " ")
def floor(number):
    return number//1

totalValue = 0

coinDollarValues = {"pennies": 0.01,
                    "nickels": 0.05,
                    "dimes": 0.1,
                    "quarters": 0.25,
                    "dollar coins": 1,
                    "dollar bills": 1,
                    "two dollar bills": 2,
                    "five dollar bills": 5,
                    "ten dollar bills": 10,
                    "twenty dollar bills": 20,
                    "fifty dollar bills": 50,
                    "hundred dollar bills": 100}

for name, value in coinDollarValues.items():
    quantity = uinput(f"How many {name} do you have?")
    canContinue = False
    while canContinue == False:
        try:
            quantity = int(quantity)
            canContinue = True
        except ValueError:
            quantity = uinput(f"Please enter an integer number. How many {name} do you have?")
    totalValue += value*quantity

print(f"I have exchanged all your coins for ${floor((totalValue*1-(0.119))*100)/100}, including 11.9% fee. Have a nice day!")