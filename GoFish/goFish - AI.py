# Kalen & Sophia - 7/8/2021

import random
import time

ranks_original = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
suits_original = ['d','c','h','s']
emptyDeck = {"A": [], "K": [], "Q": [], "J": [], "10": [], "8": [], "7": [], "6": [], "5": [], "4": [], "3": [], "2": []}

playAgain = True

def uinput(string):
    return input(string + " ")

def wait_print(string):
    print(string)
    time.sleep(1)

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
    if deck == emptyDeck:
        return False
    rank = ranks_original[random.randint(0,len(ranks_original)-1)]
    while deck[rank] == []:
        rank = ranks_original[random.randint(0,len(ranks_original)-1)]
    try:
        suit, deck[rank] = pop(deck[rank],random.randint(0,len(deck[rank])-1))
    except:
        print(deck,rank)
    hand[rank].append(suit)
    return rank

def pickRandomRank(aiHand):
    botAskedRank = ""
    maxNumOfRanks = 0
    maxNumOfSuits = 0
    for rank,suits in aiHand.items(): # check ranks with most abundent num of cards
        if suits != []:
            # bot has rank
            maxNumOfRanks = 1
            if len(suits) > maxNumOfSuits:
                maxNumOfSuits = len(suits)
                maxNumOfRanks = 1
            elif len(suits) == maxNumOfSuits:
                maxNumOfRanks += 1
    totalNumOfRanks = 0
    numOfSuits = 0
    for rank,suits in aiHand.items(): # check ranks with least abundent num of cards
        if suits != []:
            # bot has rank
            totalNumOfRanks += 1
    useMax = random.randint(0,2)
    if useMax != 0:
        useMax = 1
    if maxNumOfRanks == 1:
        useMax = random.randint(0,1)
    if useMax == 1:
        numCard = random.randint(1,maxNumOfRanks)
        i = 0
        for rank,suits in aiHand.items():
            if suits != [] and len(suits) == maxNumOfSuits:
                # bot has rank
                i += 1
                if i == numCard:
                    botAskedRank = rank
    else:
        numCard = random.randint(1,totalNumOfRanks)
        i = 0
        for rank,suits in aiHand.items():
            if suits != []:
                # bot has rank
                i += 1
                if i == numCard:
                    botAskedRank = rank
    return botAskedRank

def ai(points, cardsLeft):
    botsAskedRank = ""
    for rank,suits in hands[1].items():
        if suits != []:
            # bot has rank
            if ranksAsked[rank] == True:
                botsAskedRank = rank
                break
    cardsLeft = True
    if botsAskedRank == "":
        cardsLeft = False
        for suits in hands[1].values():
            if suits != []:
                cardsLeft = True
        if cardsLeft == False:
            wait_print("The game ended because the bot ran out of cards.")
            if playerPoints[0] > playerPoints[1]:
                print(f"Congrats Player 1, you have won with {playerPoints[0]} sets!")
                AIWinRate(False)
            else: # the bot won because 13 isnt even so there cant be a tie
                print(f"Aww, the bot won. You lost by {playerPoints[1]-playerPoints[0]} set(s).")
                AIWinRate(True)
        else:
            botsAskedRank = pickRandomRank(hands[1])
    if cardsLeft == True:
        wait_print(f"-- Bot asked for {botsAskedRank}.")
        if hands[0][botsAskedRank] == []:
            wait_print(f"-- You have no {botsAskedRank}'s. Bot Go Fished.")
            rankFished = drawCard(deck, hands[1])
            if rankFished != False:
                if len(hands[1][rankFished]) == 4:
                    hands[1][rankFished] = []
                    sets.insert(ranks_original.index(rankFished), rankFished)
                    points[1] += 1
                    wait_print(f"-- Bot has gotten 4 {rankFished}'s. Bot now has {points[1]} set(s) created.")
            elif drawCards == True:
                drawCards = False
                print("No more cards in deck, couldn't go fish.")
        else:
            wait_print(f"-- You had {len(hands[0][botsAskedRank])} {botsAskedRank}'s. {botsAskedRank}'s added to bot's hand.")
            ranksAsked[botsAskedRank] = False
            for suit in hands[0][botsAskedRank]:
                hands[1][botsAskedRank].append(suit)
            if len(hands[1][botsAskedRank]) == 4:
                hands[1][botsAskedRank] = []
                sets.insert(ranks_original.index(botsAskedRank), botsAskedRank)
                playerPoints[1] += 1
                wait_print(f"-- Bot has gotten 4 {botsAskedRank}'s. Bot now has {points[1]} set(s) created.")
            hands[0][botsAskedRank] = []
    return points, cardsLeft

def AIWinRate(won):
    file = open("goFish - AI - WinRate.txt", "r")
    wls = file.read().split(" ")
    wins = int(wls[0])
    losses = int(wls[1])
    streak = int(wls[2])
    if won:
        wins += 1
        streak += 1
    else:
        losses += 1
        streak = 0
    file.close()
    file = open("goFish - AI - WinRate.txt", "w")
    file.write(f"{wins} {losses} {streak}")
    file.close()
    winRate = wins/(wins+losses)
    print(f"\n-- Bot has new win rate of {int(winRate*100)}%, and streak of {streak}.")

while playAgain == True:
    deck = {}
    hands = [{},{}]
    sets = []
    ranksAsked = {
        'A': False,
        'K': False,
        'Q': False,
        'J': False,
        '10': False,
        '9': False,
        '8': False,
        '7': False,
        '6': False,
        '5': False,
        '4': False,
        '3': False,
        '2': False,
    }
    drawCards = True
    playerPoints = [0,0]

    for rank in ranks_original:
        deck[rank] = suits_original
        hands[0][rank] = [] # Player 1     -- Index = Player# - 1
        hands[1][rank] = [] # Player 2
        
    for i in range(7): # Give player cards
        drawCard(deck, hands[0])
    for i in range(7):
        drawCard(deck, hands[1])
        
    for rank in hands[0]:
        if len(hands[0][rank]) == 4:
            hands[0][rank] = []
            sets.insert(ranks_original.index(rank), rank)
            playerPoints[0] += 1
            print(f"You drawed 4 {rank}'s. Removed from your hand. You now have {playerPoints[0]} sets created.")
    
    for rank in hands[1]:
        if len(hands[1][rank]) == 4:
            hands[1][rank] = []
            sets.insert(ranks_original.index(rank), rank)
            playerPoints[1] += 1
            print(f"-- Bot drawed 4 {rank}'s. Removed from bot's hand. Bot now has {playerPoints[1]} set(s) created.")

    while len(sets) != 13:
        cardsLeft = False
        for suits in hands[0].values():
            if suits != []:
                cardsLeft = True
        if cardsLeft == False:
            wait_print("The game ended because you ran out of cards.")
            if playerPoints[0] > playerPoints[1]:
                print(f"Congrats Player 1, you have won with {playerPoints[0]} sets!")
                AIWinRate(False)
            else: # the bot won because 13 isnt even so there cant be a tie
                print(f"Aww, the bot won. You lost by {playerPoints[1]-playerPoints[0]} set(s).")
                AIWinRate(True)
            break
        print("Your deck:")
        viewCards(hands[0])
        rankToAsk = uinput("What card rank do you want to ask for?").upper()
        while True:
            try:
                if hands[0][rankToAsk] == []:
                    raise Exception
                break
            except:
                rankToAsk = input(f"You can only ask for a card that you have. What card rank do you want to ask for? Ranks:\n{listOfRanks(hands[0])}\n").upper()
        ranksAsked[rankToAsk] = True
        suitsTargetHas = hands[1][rankToAsk]
        if len(suitsTargetHas) != 0:
            hands[1][rankToAsk] = []
            print(f"Bot has {len(suitsTargetHas)} {rankToAsk}'s. {rankToAsk}'s added to your hand.")
            for suit in suitsTargetHas:
                hands[0][rankToAsk].append(suit)
            if len(hands[0][rankToAsk]) == 4:
                hands[0][rankToAsk] = []
                sets.insert(ranks_original.index(rankToAsk), rankToAsk)
                playerPoints[0] += 1
                ranksAsked[rankToAsk] = False
                print(f"You have gotten 4 {rankToAsk}'s. Removed from your hand. You now have {playerPoints[0]} set(s) created.")
        else:
            print(f"Bot does not have any {rankToAsk}'s. Go fish!")
            rankFished = drawCard(deck, hands[0])
            if rankFished != False:
                if len(hands[0][rankFished]) == 4:
                    hands[0][rankFished] = []
                    sets.insert(ranks_original.index(rankFished), rankFished)
                    playerPoints[0] += 1
                    ranksAsked[rankFished] = False
                    print(f"You have gotten 4 {rankFished}'s. Removed from your hand. You now have {playerPoints[0]} set(s) created.")
            elif drawCards == True:
                drawCards = False
                print("No more cards in deck, couldn't go fish.")
            
        print("")
        playerPoints, cardsLeft = ai(playerPoints, cardsLeft)
        print("")
        if cardsLeft == False:
            break
        if len(sets) == 13:
            if playerPoints[0] > playerPoints[1]:
                print(f"Congrats Player 1, you have won with {playerPoints[0]} sets!")
                AIWinRate(False)
            else: # the bot won because 13 isnt even so there cant be a tie
                print(f"Aww, the bot won. You lost by {playerPoints[1]-playerPoints[0]} set(s).")
                AIWinRate(True)
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