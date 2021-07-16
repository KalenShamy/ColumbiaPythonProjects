# Kalen & Sophia - 7/8/2021

import random

ranks_original = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits_original = ['d','c','h','s']

playAgain = True

def uinput(string):
    return input(string + " ")

def replaceStrAtIndex(string, replaceVal, index): # workaround for string[index] = replaceVal
    returnString = ""
    for i in range(len(string)):
        if i != index:
            returnString += string[i]
        else:
            returnString += replaceVal
    return returnString

def listOfRanks(hand):
    returnStr = ""
    for rank,suits in hand.items():
        hasCard = suits != []
        if hasCard == True:
            returnStr += rank + ", "
    returnStr = replaceStrAtIndex(returnStr, "", len(returnStr)-1)
    returnStr = replaceStrAtIndex(returnStr, "", len(returnStr)-1)
    return returnStr

def viewCards(hand):
    printStr = ""
    for rank, suits in hand.items():
        if suits != []:
            printStr += rank + ": "
            for suit in suits:
                printStr += suit + " "
            printStr += "\n"
    print(printStr)

def pop(list_, position):
    item = list_[position]
    newList = []
    for i in range(len(list_)):
        if i != position:
            newList.append(list_[i])
    return item, newList

def drawCard(deck, hand):
    rank = ranks_original[random.randint(0,len(ranks_original)-1)]
    while deck[rank] == []:
        rank = ranks_original[random.randint(0,len(ranks_original)-1)]
    try:
        suit, deck[rank] = pop(deck[rank],random.randint(0,len(deck[rank])-1))
    except:
        print(deck,rank)
    hand[rank].append(suit)
    return rank

for i in range(1,51):
    print(f"{i}.")

while True:
    try:
        shellLines = int(uinput("How many lines tall is your shell?"))
    except:
        pass
    else:
        break

while playAgain == True:
    deck = {}
    hands = [{},{}]
    sets = []
    playerPoints = [0,0]

    for rank in ranks_original:
        deck[rank] = suits_original
        hands[0][rank] = [] # Player 1     -- Index = Player# - 1
        hands[1][rank] = [] # Player 2
        
    for i in range(7): # Give player cards
        drawCard(deck, hands[0])
    for i in range(7):
        drawCard(deck, hands[1])
        
    for player in range(2):
        for rank in hands[player]:
            if len(hands[player][rank]) == 4:
                hands[player][rank] = []
                sets.insert(ranks_original.index(rank), rank)
                playerPoints[player] += 1
                print(f"Player {player + 1} drawed 4 {rank}'s. Removed from your hand. You now have {playerPoints[player]} set(s) created.")

    while len(sets) != 13:
        for player in range(1,3):
            target = 0
            if player == 1:
                target = 2
            else:
                target = 1
            cardsLeft = False
            for suits in hands[0].values():
                if suits != []:
                    cardsLeft = True
            if cardsLeft == False:
                print(f"The game ended because Player {player} ran out of cards.")
                print(f"Congrats, Player {player}, you have won with {playerPoints[player-1]} sets!")
                sets = range(13)
                break
            print(f"Player {player}:\n\nYour deck:")
            viewCards(hands[player-1])
            
            rankToAsk = uinput(f"What card rank do you want to ask for?").upper()
            while True:
                try:
                    if hands[player-1][rankToAsk] == []:
                        raise Exception
                    break
                except:
                    rankToAsk = input(f"You can only ask for a card that you have. What card rank do you want to ask for? Ranks:\n{listOfRanks(hands[player-1])}\n").upper()
            suitsTargetHas = hands[target-1][rankToAsk]
            if len(suitsTargetHas) != 0:
                hands[target-1][rankToAsk] = []
                print(f"Player {target} has {len(suitsTargetHas)} {rankToAsk}'s. {rankToAsk}'s added to your hand.")
                for suit in suitsTargetHas:
                    hands[player-1][rankToAsk].append(suit)
                if len(hands[player-1][rankToAsk]) == 4:
                    hands[player-1][rankToAsk] = []
                    sets.insert(ranks_original.index(rankToAsk), rankToAsk)
                    playerPoints[player-1] += 1
                    print(f"You have gotten 4 {rankToAsk}'s. Removed from your hand. You now have {playerPoints[player-1]} set(s) created.")
            else:
                print(f"Player {target} does not have any {rankToAsk}'s. Go fish!")
                rankFished = drawCard(deck, hands[player-1])
                if len(hands[player-1][rankFished]) == 4:
                    hands[player-1][rankFished] = []
                    sets.insert(ranks_original.index(rankFished), rankFished)
                    playerPoints[player-1] += 1
                    print(f"You have gotten 4 {rankFished}'s. Removed from your hand. You now have {playerPoints[player-1]} set(s) created.")
            if len(sets) == 13:
                print(f"Congrats, Player {player}, you have won with {playerPoints[player-1]} sets!")
            else:
                uinput(f"\nPress enter when you are going to give control to Player {target}")
                for i in range(shellLines-4):
                    print("")
                uinput(f"Press enter when Player {target} is in control.")
    paA = "Would you like to play again? (y/n)"
    while True:
        pa = uinput(paA).lower()
        if pa == "n":
            playAgain = False
            break
        elif pa == "y":
            playAgain = True
            print("\n"*1000)
            break
        else:
            paA = "Invalid Input. " + paA