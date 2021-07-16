# Kalen Shamy - 6/29/2021

partner1Item = "chocolate chip cookies"
partner1Quantity = 3
partner1ItemCost = 1
partner2Item = "glazed donuts"
partner2Quantity = 2
partner2ItemCost = 2

def uinput(string):
    return input(string + " ")

print(f"Partner 1: Hello, how much do {partner1Item} cost?")
print(f"Pastry Chef: They cost ${partner1ItemCost}.")
print(f"Partner 1: Can we have {partner1Quantity} cookies?")
print(f"Pastry Chef: Sure! That'll be ${partner1ItemCost*partner1Quantity}.")
print(f"Partner 2: Okay, and how much do {partner2Item} cost?")
print(f"Pastry Chef: They cost ${partner2ItemCost}.")
print(f"Partner 2: Can we have {partner2Quantity} cookies?")
print(f"Pastry Chef: Sure! That'll be ${partner2ItemCost*partner2Quantity}.")
print(f"Pastry Chef: The total will be ${(partner1ItemCost*partner1Quantity)+(partner2ItemCost*partner2Quantity)}")