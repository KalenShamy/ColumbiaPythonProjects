# Kalen & Maria - 7/6/2021

# Take turns having the players target locations onthe grid.
# If miss, display “It’s a miss.”
# If hit, display “It’s a hit.”
# If sunk, display “You sunk a battleship”
# End game if one player loses both battleships

water = "~"
boat = "0"
hit = "|"
sunk = "X"
fired = "_"

player1Grid = [[water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water]]
player2Grid = [[water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water]]

player1VisibleGrid = [[water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water]]
player2VisibleGrid = [[water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water], [water, water, water, water, water, water, water, water]]

def uinput(string):
    return input(string + " ")

# 0 0 ~ ~
# ~ ~ ~ ~
# ~ ~ ~ ~
# ~ 0 0 ~

# Player 1                       Player 2
# ~ ~ ~ ~ ~ ~ ~ ~                ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~                ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~                ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~                ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~                ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~                ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~                ~ ~ ~ ~ ~ ~ ~ ~
# ~ ~ ~ ~ ~ ~ ~ ~                ~ ~ ~ ~ ~ ~ ~ ~

def printGrid(grid):
    returnGrid = ""
    for row in grid:
        for column in row:
            returnGrid += str(column) + " "
        returnGrid += "\n"
    print(returnGrid)

def printBothGrids(player1Grid, player2Grid):
    grids = "Player 1                       Player 2\n" # 23 spaces
    for rowI in range(8):
        for columnI in range(8):
            grids += player1Grid[rowI][columnI] + " "
        grids += "               " # 15 spaces
        for columnI in range(8):
            grids += player2Grid[rowI][columnI] + " "
        grids += "\n"
    print(grids)

def checkWin(grid):
    won = True
    for row in grid:
        for column in row:
            if column == boat or column == hit:
                won = False
    return won

print(f"Welcome to battleship! Here is something you need to know:\nOn a grid,\n{water} is water\n{boat} is a boat\n{hit} is a hit part of a boat\n{sunk} is a part of a sunken ship\n{fired} is a spot on the board that has been fired at, and is empty")

for player in range(1,3):
    print(f"\nPlayer {player} Boats:\n")
    for ship in range(1,3):
        canContinue = False
        column1 = 0
        row = 0
        while canContinue == False:
            try:
                column1 = int(uinput(f"Boat {ship} column (1-8):"))
                if column1 > 8 or column1 < 1:
                    Error # Throws an error if ran, successfully parses
                row = int(uinput(f"Boat {ship} row (1-8):"))
                if row > 8 or row < 1:
                    Error # Throws an error if ran, successfully parses
                if column1 == 8:
                    column2 = 7
                else:
                    column2 = column1+1
                if player == 1:
                    if player1Grid[row-1][column1-1] == boat or player1Grid[row-1][column2-1] == boat:
                        Error # Throws an error if ran, successfully parses
                else:
                    if player2Grid[row-1][column1-1] == boat or player2Grid[row-1][column2-1] == boat:
                        Error # Throws an error if ran, successfully parses
                canContinue = True
            except:
                print("Sorry, please enter a number from 1-4 for the boat's column and row, and don't create overlapping boats.")

        if column1 == 8:
            column2 = 7
        else:
            column2 = column1+1

        if player == 1:
            player1Grid[row-1][column1-1]=boat
            player1Grid[row-1][column2-1]=boat
        else:
            player2Grid[row-1][column1-1]=boat
            player2Grid[row-1][column2-1]=boat
    print("Here is your grid!")
    if player == 1:
        printGrid(player1Grid)
    else:
        printGrid(player2Grid)
while True:
    if checkWin(player2Grid) == True or checkWin(player1Grid) == True:
        break
    for player in range(1,3):
        print(f"Player {player}'s turn:\nWhat position would you like to fire at?")
        canContinue = False
        column = 0
        row = 0
        while canContinue == False:
            try:
                column = int(uinput(f"Firing column (1-8):"))
                if column > 8 or column < 1:
                    Error # Throws an error if ran, successfully parses
                row = int(uinput(f"Firing row (1-8):"))
                if row > 8 or row < 1:
                    Error # Throws an error if ran, successfully parses
                canContinue = True
            except:
                print("Sorry, please enter a number from 1-8 for the firing point's column and row.")
        if player == 1:
            position = player2Grid[row-1][column-1]
            if position == water:
                player2Grid[row-1][column-1] = fired
                player2VisibleGrid[row-1][column-1] = fired
                print("It's a miss! Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
            elif position == boat:
                player2Grid[row-1][column-1] = hit
                player2VisibleGrid[row-1][column-1] = hit
                print("It's a hit! Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
            elif position == hit:
                player2Grid[row-1][column-1] = sunk
                player2VisibleGrid[row-1][column-1] = sunk
                print("It's a hit! You sunk part of a battleship! Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
            elif position == fired:
                player2Grid[row-1][column-1] = fired
                player2VisibleGrid[row-1][column-1] = fired
                print("You already fired here! You loose a turn :( Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
            elif position == sunk:
                player2Grid[row-1][column-1] = sunk
                player2VisibleGrid[row-1][column-1] = sunk
                print("You already sunk this ship! You loose a turn :( Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
        else:
            position = player1Grid[row-1][column-1]
            if position == water:
                player1Grid[row-1][column-1] = fired
                player1VisibleGrid[row-1][column-1] = fired
                print("It's a miss! Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
            elif position == boat:
                player1Grid[row-1][column-1] = hit
                player1VisibleGrid[row-1][column-1] = hit
                print("It's a hit! Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
            elif position == hit:
                player1Grid[row-1][column-1] = sunk
                player1VisibleGrid[row-1][column-1] = sunk
                print("It's a hit! You sunk part of a battleship! Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
            elif position == fired:
                player1Grid[row-1][column-1] = fired
                player1VisibleGrid[row-1][column-1] = fired
                print("You already fired here! You loose a turn :( Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
            elif position == sunk:
                player1Grid[row-1][column-1] = sunk
                player1VisibleGrid[row-1][column-1] = sunk
                print("You already sunk this ship! You loose a turn :( Here's the current boards:\n")
                printBothGrids(player1VisibleGrid, player2VisibleGrid)
        if checkWin(player1Grid) == True or checkWin(player2Grid) == True:
            print(f"Congrats, Player {player}! You won!")
            break