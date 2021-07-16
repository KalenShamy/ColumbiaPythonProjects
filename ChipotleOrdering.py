# Kalen Shamy - 6/28/2021

import random

def uinput(string):
    return input(string + " ")

print("Welcome to Chipotle, how may I help you today?")

order = ""
price = 0

food = uinput("Would you like a Burrito or Taco?")
while food != "Burrito" and food != "Taco":
    food = uinput("Sorry, we dont have that. Would you like a Burrito or Taco?")

order = order + food

protein = uinput("Okay, what would you like for your protein? We have Chicken, Barbacoa, Sofritas, Steak, and Carnitas.")
while protein != "Chicken" and protein != "Barbocoa" and protein != "Sofritas" and protein != "Steak" and protein != "Carnitas":
    protein = uinput("Sorry we dont have that. We have Chicken, Barbacoa, Sofritas, Steak, and Carnitas.")

order = order + "\n" + protein
if protein == "Chicken":
    order = order + " - $9.65"
    cost = 9.65
elif protein == "Barbaoa":
    order = order + " - $10.75"
    cost = 10.75
elif protein == "Sofritas":
    order = order + " - $9.65"
    cost = 9.65
elif protein == "Steak":
    order = order + " - $10.75"
    cost = 10.75
elif protein == "Carnitas":
    order = order + " - $10.15"
    cost = 10.15

rice = uinput("Okay, White or Brown Rice?")
while rice != "White Rice" and rice != "Brown Rice":
    rice = uinput("Sorry, we only have White and Brown Rice. Which would you like?")

order = order + "\n" + rice

beans = uinput("Okay, would you like Black Beans or Pinto Beans?")
while beans != "Black Beans" and beans != "Pinto Beans":
    beans = uinput("Sorry, we only have Black Beans and Pinto Beans. Which would you like?")

order = order + "\n" + beans

salsa = uinput("To top it off, would you like salsa? (y/n)")
while salsa != "y" and salsa != "n":
    salsa = uinput("To top it off, would you like salsa? (y/n)")

if salsa == "y":
    order = order + "\nSalsa"

paymentMethod = uinput("\nOkay, your total is $" + str(cost) + ". Would you like to use Cash or Credit?")
while paymentMethod != "Cash" and paymentMethod != "Credit":
    paymentMethod = uinput("Sorry, we don't accept that. Would you like to use Cash or Credit?")

print("Thank you, have a nice day! Here is your receipt.")

print("\n\n\nRECEIPT\nOrder# " + str(random.randrange(1000,9999,1)) + "\n\n" + order + "\n\nTotal - $" + str(cost) + "\n" + paymentMethod + " - $" + str(cost))