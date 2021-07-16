# Kalen Shamy - 07/13/2021

from time import sleep
import random
import math
import string

testing = False

paperWidth = 50
recieptPaperPercentWidth = 0.75
tip = 0.20
tax = 0.08

def testingSleep(arg):
    pass

if testing == True:
    sleep = testingSleep

def uinput(string):
    return input(string+" ")

def replaceStrAtIndex(string, replaceVal, index): # workaround for string[index] = replaceVal
    returnString = ""
    for i in range(len(string)):
        if i != index:
            returnString += string[i]
        else:
            returnString += replaceVal
    return returnString

def capitalize(string):
    returnStr = ""
    for i in range(len(string.split(" "))):
        if i == len(string.split(" "))-1:
            returnStr += string.split(" ")[i].capitalize()
        else:
            returnStr += string.split(" ")[i].capitalize() + " "
    
    return returnStr

def normalize(string_):
    returnStr = ""
    validChars = string.ascii_lowercase + string.digits + " "
    for char in string_:
        if char.lower() in validChars:
            returnStr += char
    returnStr = capitalize(returnStr)
    
    return returnStr

def oClock_hundred(clock):
    try:
        time = clock
        if " " in clock:
            time = clock.split(" ")[0]
        apm = "AM"
        if clock != time and len(clock.split(" ")) > 1:
            apm = clock.split(" ")[1].upper()
        hours = int(time.split(":")[0])
        minutes = 0
        if hours != time and len(time.split(":")) > 1:
            minutes = int(time.split(":")[1])
        hours += minutes//60
        minutes %= 60
        if hours == 24:
            hours = 0
        if apm == "PM" and hours != 12:
            hours += 12
        elif apm == "AM" and hours == 12:
            hours = 0
        if minutes < 10:
            minutes = "0" + str(minutes)
        return int(f"{hours}{minutes}")
    except:
        return "INVALID TIME GIVEN"

class restaurant:
    def __str__(self):
        return f"{self.name}, established in {self.year_established}."
    waiters = ["Sam", "Sophia", "Aiden", "Kathleen", "Eric", "Olivia"]
    def __init__(self, name, owner, year_established, location, open_time, close_time, menu):
        self.name = name
        self.owner = owner
        self.year_established = year_established
        self.location = location
        self.open = open_time
        self.close = close_time
        self.menu = menu
        self.parent = self
    def welcome(self):
        question = f"Hello, this is {random.choice(self.waiters)} from {self.name}, what time will you be coming? (eg: \"7:00 PM\")"
        open_time = oClock_hundred(self.open)
        close_time = oClock_hundred(self.close)
        m_time = 0
        while True:
            time = uinput(question)
            try:
                m_time = int(time)*100
            except:
                m_time = oClock_hundred(time)
            if m_time == "INVALID TIME GIVEN":
                question = f"Sorry, that's not a valid time. Our hours are from {self.open} to {self.close}."
                continue
            if open_time > close_time:
                if open_time >= m_time > close_time:
                    break
            elif open_time < close_time:
                if open_time <= m_time < close_time:
                    break
            else:
                raise Exception(f"Open and Close times are equal: {open_time} == {close_time} OR {self.open} == {self.close}")
            question = f"Sorry, we're not open at {time}. We open at {self.open} and close at {self.close}."
        timeOfDay = ""
        if 400 <= m_time < 1200: # 4 am - 12 pm
            timeOfDay = "morning"
        elif 1200 <= m_time < 1800: # 12 pm - 6 pm
            timeOfDay = "afternoon"
        elif 1800 <= m_time < 2100: # 6 pm - 9 pm
            timeOfDay = "evening"
        elif 2100 <= m_time < 400: # 9 pm - 4 am
            timeOfDay = "night"
        return timeOfDay
    
    def get_menu(self):
        nameSpaces = " "*int((paperWidth - len(self.name))/2)
        returnMenu = f"{nameSpaces}{self.name}\n"
        for mType, foods in menu.items():
            returnMenu += f"{mType}\n"
            for food, price in foods.items():
                dashs = " " + "- "*math.ceil((paperWidth-(4+len(food)+len(f"${price:.2f}")))/2)
                returnMenu += f"    {food}{dashs}${price:.2f}\n"
            returnMenu += "\n"
        
        return returnMenu
    
    def meal(self, name):
        foods = self.menu[capitalize(name)+"s"]
        foodsStr = ""
        for food in foods.keys():
            foodsStr += f"{food},\n"
        foodsStr = replaceStrAtIndex(foodsStr, "", len(foodsStr)-1)
        foodsStr = replaceStrAtIndex(foodsStr, "", len(foodsStr)-1)
        
        food = ""
        question = f"What would you like for a {name.lower()}? "
        while True:
            food = input(question)
            cost = 0
            try:
                valid = False
                for food_ in foods.keys():
                    if normalize(food) in normalize(food_):
                        valid = True
                        food = food_
                        break
                if valid == True:
                    break
                else:
                    raise Exception
            except:
                question = f"Sorry, we dont have the {name.lower()}: \"{capitalize(food)}\". We have:\n{foodsStr}\n"
        return capitalize(food)
    def chef(self, food):
        print(f"\nChef is preparing your {food}.")
        for i in range(7):
            sleep(1)
            print(f"{i+1}...")
        print(f"\nWaiter is bringing your {food}.")
        for i in range(3):
            sleep(1)
            print(f"{i+1}...")
        print(f"\nEating {food}.")
        for i in range(5):
            sleep(1)
            print(f"{i+1}...")
    def goodbye(self, reciept):
        recieptStr = ""
        recieptWidth = int(paperWidth*recieptPaperPercentWidth)
        nameSpaces = " "*((recieptWidth-(len(self.name)+4))//2)
        orderNum = random.randint(1,9999)
        recieptStr += f"{nameSpaces}~ {self.name} ~\n"
        orderNumSpaces = " "*((recieptWidth-11)//2)
        if 100 <= orderNum < 1000:
            orderNum = "0" + orderNum
        elif 10 <= orderNum < 100:
            orderNum = "00" + orderNum
        elif 1 <= orderNum < 10:
            orderNum = "000" + orderNum
        recieptStr += f"{orderNumSpaces}Order #{orderNum}\n\n"
        totalPrice = 0.00
        for i in range(len(reciept)):
            food = reciept[i]
            foodType = {}
            if i == 0:
                foodType = self.menu["Drinks"]
            elif i == 1:
                foodType = self.menu["Starters"]
            elif i == 2:
                foodType = self.menu["Entres"]
            elif i == 3:
                foodType = self.menu["Desserts"]
            for food_, price in foodType.items():
                if food == normalize(food_):
                    foodDashes = " "*(recieptWidth-(len(food_)+len(f"${price:.2f}")))
                    recieptStr += f"{food_}{foodDashes}${price:.2f}\n"
                    totalPrice += price
        tipSpaces = " "*(recieptWidth-(len(f"Tip ({int(tip*100)}%):")+len(f"${tip*totalPrice:.2f}")))
        recieptStr += f"\n\nTip ({int(tip*100)}%):{tipSpaces}${tip*totalPrice:.2f}\n"
        totalPrice *= (1-tip)
        taxSpaces = " "*(recieptWidth-(len("Tax:")+len(f"${tax*totalPrice:.2f}")))
        recieptStr += f"Tax:{taxSpaces}${tax*totalPrice:.2f}\n\n"
        totalPrice *= (1-tax)
        totalPrice = math.ceil(totalPrice*100)/100
        totalSpaces = " "*(recieptWidth-(len("Total:")+len(f"${totalPrice:.2f}")))
        recieptStr += f"Total:{totalSpaces}${totalPrice:.2f}"
        print(f"Thank you for eating at {self.name}! Here is your reciept:\n\n{recieptStr}")

menu = {
    "Drinks": {
        "Lebanese Coffee": 4.00,
        "Pot Of Mint Tea": 6.50,
    },
    "Starters": {
        "Hummus": 6.25,
        "Labneh": 5.50,
        "Baba Ghanoush": 6.25,
        "The Pickle Plate": 6.25,
    },
    "Entres": {
        "Fattoush": 11.25,
        "Falafel": 10.50,
        "Tabbouleh": 10.75,
        "Man\'ousheh": 8.75,
    },
    "Desserts": {
        "Maamoul": 5.25,
        "Baklava": 6.50,
        "Kunafah": 6.25,
    }
}

specialMenu = menu
specialMenu["Drinks"]["Arak (alcoholic)"] = 12.50
specialMenu["Starters"]["Mutabal"] = 6.50
specialMenu["Entres"]["Kibbeh"] = 9.25
specialMenu["Desserts"]["Meghli"] = 7.25

class sister_restaurant(restaurant):
    def __init__(self, name, owner, year_established, location, open_time, close_time, menu, parent):
        self.name = name
        self.owner = owner
        self.year_established = year_established
        self.location = location
        self.open = open_time
        self.close = close_time
        self.menu = menu
        self.parent = parent

faisal_eats = restaurant("Faisal Eats", "Kalen", 1992, "Manhattan-Inwood", "6:00 AM", "10:00 PM", menu)
faisal_eats_midtown = sister_restaurant("Faisal Eats", "Kalen", 1992, "Manhattan-Midtown", "7:00 AM", "6:00 PM", specialMenu, faisal_eats)
question = "Which restaurant would you like to visit? Inwood or Midtown?"
while True:
    restaurant_visiting = capitalize(uinput(question))
    if restaurant_visiting == "Inwood":
        restaurant_visiting = faisal_eats
        break
    elif restaurant_visiting == "Midtown":
        restaurant_visiting = faisal_eats_midtown
        break
    else:
        question = f"Sorry, we only have locations at Inwood and Midtown. Which one would you like to visit?"
time = restaurant_visiting.welcome()
print(f"Welcome! Here is our menu:\n\n{faisal_eats.get_menu()}")
reciept = []
reciept.append(restaurant_visiting.meal("Drink"))
reciept.append(restaurant_visiting.meal("Starter"))
reciept.append(restaurant_visiting.meal("Entre"))
reciept.append(restaurant_visiting.meal("Dessert"))
print("\nOkay, your food will be here in a minute.")
for food in reciept:
    sleep(1)
    restaurant_visiting.chef(food)
restaurant_visiting.goodbye(reciept)
