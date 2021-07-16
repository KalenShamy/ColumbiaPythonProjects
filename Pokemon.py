# Kalen Shamy - Pokemon

import random
import time
#
# random(attack-10,attack+15)
#

# moves = {
#     "Tackle": [],
#     "Thunderbolt": [],
#     "Vine Whip": [],
#     "Scratch": [],
#     "Fire Fang": [],
#     "Tail Whip": [],
#     "Water Gun": [],
#     "Growl": [],
#     "Gust": [],
#     "Quick Attack": [],
# }

def clearShell():
    print("\n"*998)
    print("""\n
                                  ,'\ 
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  / \ \    ,'   | \/ / ,`.|         /  / \ \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._   `|       |  | \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-. |       |.-'    '-.|     '-.| |   |
                               `'                             '-._|
""")

def uinput(string):
    return input(string + " ")

class Pokemon:
    def __str__(self):
        return self.Name
    def __init__(self, name, attack, defense, hp, accuracy, moves, pokeType):
        self.Name = name
        self.ATK = attack
        self.DEF = defense
        self.MAXHP = hp
        self.HP = hp
        self.ACC = accuracy
        self.Moves = moves
        self.Type = pokeType
        self.Fainted = False
        
emojis = {
    "Electric": "⚡",
    "Grass": "🌿",
    "Fire": "🔥",
    "Water": "🌊",
    "Normal": "🔘",
    "Flying": "🦇",
    "Fairy": "🧚",
    "Bug": "🐛",
    "Fighting": "👊",
    "Psychic": "✨",
    "Rock": "🗿",
    "Ground": "🌎"
}
        
pokemonPresets = {
#   "Name": Pokemon("Name", ATK, DEF, HP, ACC, ["move1", "move2"], "type"),
    "Pikachu": Pokemon("Pikachu", 55, 40, 235, 0.95, ["Tackle", "Thunderbolt"], "Electric"),
    "Bulbasaur": Pokemon("Bulbasaur", 49, 49, 245, 0.85, ["Tackle", "Vine Whip"], "Grass"),
    "Charmander": Pokemon("Charmander", 52, 243, 239, 0.8, ["Scratch", "Fire Fang"], "Fire"),
    "Squirtle": Pokemon("Squirtle", 48, 65, 244, 0.9, ["Tail Whip", "Water Gun"], "Water"),
    "Eevee": Pokemon("Eevee", 55, 50, 255, 0.85, ["Growl", "Tail Whip"], "Normal"),
    "Pidgey": Pokemon("Pidgey", 45, 40, 240, 0.75, ["Gust", "Quick Attack"], "Flying"),
    "Clefairy": Pokemon("Clefairy", 45, 48, 270, 0.7, ["Copycat", "Charm"], "Fairy"),
    "Caterpie": Pokemon("Caterpie", 30, 35, 245, 0.82, ["Tackle", "Bug Bite"], "Bug"),
    "Mankey": Pokemon("Mankey", 80, 35, 240, 0.71, ["Leer", "Karate Chop"], "Fighting"),
    "Abra": Pokemon("Abra", 20, 15, 225, 0.94, ["Confusion", "Telaport"], "Psychic"),
    "Geodude": Pokemon("Geodude", 60, 100, 240, 0.67, ["Sand Attack", "Rock Throw"], "Rock"),
    "Sandshrew": Pokemon("Sandshrew", 75, 85, 50, 0.83, ["Scratch", "Bulldoze"], "Ground"),
}

types = {
    "Electric": {"Adv": ["Water", "Flying"], "Dis": ["Electric", "Grass"], "Unt": ["Ground"]},
    "Grass": {"Adv": ["Water", "Ground", "Rock"], "Dis": ["Fire", "Grass", "Flying", "Bug"], "Unt": []},
    "Fire": {"Adv": ["Grass", "Bug"], "Dis": ["Fire", "Water", "Rock"], "Unt": []},
    "Water": {"Adv": ["Fire", "Ground", "Rock"], "Dis": ["Water", "Grass"], "Unt": []},
    "Normal": {"Adv": [], "Dis": [], "Unt": []},
    "Flying": {"Adv": ["Grass", "Fighting", "Bug"], "Dis": ["Electric", "Rock"], "Unt": []},
    "Fairy": {"Adv": ["Fighting"], "Dis": ["Fire"], "Unt": []},
    "Bug": {"Adv": ["Grass", "Psycic"], "Dis": ["Fire", "Fighting", "Flying", "Fairy"], "Unt": []},
    "Fighting": {"Adv": ["Normal", "Rock"], "Dis": ["Flying", "Psycic", "Bug", "Fairy"], "Unt": []},
    "Psychic": {"Adv": ["Fighting"], "Dis": ["Psycic"], "Unt": []},
    "Rock": {"Adv": ["Fire", "Flying", "Bug"], "Dis": ["Fighting", "Ground"], "Unt": []},
    "Ground": {"Adv": ["Fire", "Electric", "Rock"], "Dis": ["Grass", "Bug"], "Unt": ["Flying"]},
}


playersPokemon = [[],[]]
playersActivePokemon = [None, None]

# randomize pokemon into players decks
chosenPokemon = {}
for name in pokemonPresets.keys():
    chosenPokemon[name] = False

for player in range(1,3): # Randomize Players Decks
    for i in range(3):
        canAdd = False
        while canAdd == False:
            pokemonChosenI = random.randint(1,len(pokemonPresets))
            i_ = 0
            for name, pokemon in pokemonPresets.items():
                i_ += 1
                if pokemonChosenI == i_ and chosenPokemon[name] != True:
                    # this pokemon is the random one chosen and hasn't been chosen already.
                    playersPokemon[player-1].append(pokemon)
                    chosenPokemon[name] = True
                    canAdd = True
    playersActivePokemon[player-1] = playersPokemon[player-1][0]

def pokemonStats(player):
    deck = playersPokemon[player]
    deckStr = ""
    for pokemon in deck:
        deckStr += f"\t{pokemon.Name}:\n\t\tHP: {pokemon.HP}/{pokemon.MAXHP} ({int((pokemon.HP/pokemon.MAXHP)*100)}%)\n\t\tAttack: {pokemon.ATK}\n\t\tDefense: {pokemon.DEF}\n\t\tAccuracy: {int(100*pokemon.ACC)}%\n\n"
    return deckStr

def progressBar(percent):
    percent *= 10
    percent = int(percent)
    bar = "#"*percent + "0"*(10-percent)
    return bar

def printPokeHealth(player):
    plrNum = player
    opponentNum = player-1
    if opponentNum == 0:
        opponentNum = 2
    plrPokemon = playersActivePokemon[player-1]
    opponentPokemon = playersActivePokemon[player-2]
    tabs = "\t"*(4-int(len(f"|| P{plrNum}: {emojis[plrPokemon.Type]} {plrPokemon.Name} ({int((plrPokemon.HP/plrPokemon.MAXHP)*100)}%)")/8))
    print(f"|| P{plrNum}: {emojis[plrPokemon.Type]} {plrPokemon.Name} ({int((plrPokemon.HP/plrPokemon.MAXHP)*100)}%){tabs}P{opponentNum}: {emojis[opponentPokemon.Type]} {opponentPokemon.Name} ({int((opponentPokemon.HP/opponentPokemon.MAXHP)*100)}%)\n|| {progressBar(plrPokemon.HP/plrPokemon.MAXHP)} - {plrPokemon.HP} HP\t\t{progressBar(opponentPokemon.HP/opponentPokemon.MAXHP)} - {opponentPokemon.HP} HP\n")

def checkWin(opponent, opponentNum):
    win = True
    for pokemon in opponent:
        if pokemon.Fainted == False:
            win = False
            playersActivePokemon[opponentNum] = pokemon
    return win

def pokemonList(player):
    pokeList = ""
    pokeObjs = []
    num = 0
    for pokemon in playersPokemon[player-1]:
        if pokemon.Fainted == False and pokemon != playersActivePokemon[player-1]:
            num += 1
            pokeObjs.append(pokemon)
            if num == 1:
                pokeList = f"A. {pokemon.Name}"
            else:
                pokeList += f"\nB. {pokemon.Name}"
    if num == 0:
        pokeList = "A. Cancel"
    elif num == 1:
        pokeList += "\nB. Cancel"
    elif num == 2:
        pokeList += "\nC. Cancel"
    num += 1
    return num, pokeList, pokeObjs

def typeAdvantage(pokemon, target):
    mult = 1
    advList = types[pokemon.Type]
    for Type in advList["Adv"]:
        if Type == target.Type:
            mult = 2
    for Type in advList["Dis"]:
        if Type == target.Type:
            mult = 1/2
    for Type in advList["Unt"]:
        if Type == target.Type:
            mult = 0
    return mult

ranAway = False
winner = None

lastAction = ""

while winner == None:
    for player in range(1,3):
        clearShell()
        options = f"\n\tA. View Pokemon\t\tB. Attack ({typeAdvantage(playersActivePokemon[player-1], playersActivePokemon[player-2])}x)\n\tC. Switch Pokemon\tD. Defense\n\tE. Run away"
        if lastAction:
            print("\n"+lastAction+"\n\n")
        else:
            print("")
        printPokeHealth(player)
        hasRun = False
        choice = uinput(f"Player {player}:\n\nActive Pokemon: {playersActivePokemon[player-1].Name}\nWhat would you like to do?\n{options}\n>").upper()
        while (choice == "A") or (choice != "A" and choice != "B" and choice != "C" and choice != "D" and choice != "E") or hasRun == False:
            hasRun = True
            if choice != "A" and choice != "B" and choice != "C" and choice != "D" and choice != "E":
                choice = uinput(f"\nPlease enter any letter A through D.\n{options}\n>").upper()
                hasRun = False
                
            if choice == "A": # View Pokemon
                print(f"\nPlayer {player} Pokemon:\n{pokemonStats(player-1)}")
                choice = uinput(f"Player {player}:\n\nActive Pokemon: {playersActivePokemon[player-1].Name}\nWhat would you like to do?\n{options}\n>").upper()
                hasRun = False
            elif choice == "B": # Attack
                playersActive = playersActivePokemon[player-1]
                opponentActive = playersActivePokemon[player-2]
                opponentNum = player-1
                if opponentNum == 0:
                    opponentNum = 2
                hit = random.randint(1,100)/100 <= playersActive.ACC
                percent = random.randint(int(playersActive.ACC*100),int(100+(100-playersActive.ACC*100)))/100
                attackChosen = uinput(f"\n{playersActive}'s Moves:\n\nA. {playersActive.Moves[0]}\nB. {playersActive.Moves[1]}\n\n>").upper()
                while attackChosen != "A" and attackChosen != "B":
                    attackChosen = uinput(f"\nPlease enter any letter A through B.\n\n>").upper()
                if attackChosen == "A":
                    attackChosen = 0
                elif attackChosen == "B":
                    attackChosen = 1
                if hit == True:
                    lastAction = f"Player {player} uses {playersActive.Name}'s {playersActive.Moves[attackChosen]} against {opponentActive.Name}. It's a hit! Deals {round(typeAdvantage(playersActive, opponentActive)*percent*playersActive.ATK)} damage."
                    opponentActive.HP -= round(typeAdvantage(playersActive, opponentActive)*percent*playersActive.ATK)
                    if opponentActive.HP <= 0:
                        opponentActive.HP = 0
                        lastAction = f"Player {player} uses {playersActive.Name}'s {playersActive.Moves[attackChosen]} against {opponentActive.Name}. It's a hit! Deals {round(typeAdvantage(playersActive, opponentActive)*percent*playersActive.ATK)} damage. Player {opponentNum}'s {opponentActive.Name} has fainted."
                        opponentActive.Fainted = True
                        won = checkWin(playersPokemon[player-2], player-2)
                        if won == True:
                            lastAction = f"Player {opponentNum} has run out of Pokemon."
                            winner = player
                else:
                    lastAction = f"Player {player} uses {playersActive.Name}'s {playersActive.Moves[attackChosen]} against {opponentActive.Name}. It's a miss!"
            elif choice == "C": # Switch Pokemon
                num, pokeList, pokeObjs = pokemonList(player)
                if num == 1:
                    hasRun = False
                    print("\nNo Pokemon left to switch to.\n")
                    choice = uinput(f"Player {player}:\n\nActive Pokemon: {playersActivePokemon[player-1].Name}\nWhat would you like to do?\n{options}\n>").upper()
                else:
                    newActive = uinput(f"\nWhat pokemon do you want to switch to?\n\n{pokeList}\n\n>").upper()
                    if num == 2:
                        while newActive != "A" and newActive != "B":
                            newActive = uinput(f"\nPlease enter any letter A through B.\n\n>").upper()
                        if newActive == "B": # Cancel
                            hasRun = False
                            print("\nCanceled.\n")
                            choice = uinput(f"Player {player}:\n\nActive Pokemon: {playersActivePokemon[player-1].Name}\nWhat would you like to do?\n{options}\n>").upper()
                        else:
                            playersActivePokemon[player-1] = pokeObjs[0]
                            lastAction = f"\nPlayer {player} switched their active Pokemon to {playersActivePokemon[player-1].Name}."
                    elif num == 3:
                        while newActive != "A" and newActive != "B" and newActive != "C":
                            newActive = uinput(f"\nPlease enter any letter A through B.\n\n>").upper()
                        if newActive == "C": # Cancel
                            hasRun = False
                            print("\nCanceled.\n")
                            choice = uinput(f"Player {player}:\n\nActive Pokemon: {playersActivePokemon[player-1].Name}\nWhat would you like to do?\n{options}\n>").upper()
                        else:
                            if newActive == "A":
                                newActive = 0
                            else:
                                newActive = 1
                            playersActivePokemon[player-1] = pokeObjs[newActive]
                            lastAction = f"Player {player} switched their active Pokemon to {playersActivePokemon[player-1].Name}."
            elif choice == "D": # Defense / Heal
                playersActive = playersActivePokemon[player-1]
                success = random.randint(1,100)/100 <= round(playersActive.ACC*.75)
                percent = random.randint(round(playersActive.ACC*75),int(playersActive.ACC*75*1.25))/100
                heal = round(playersActive.DEF * percent)
                if success:
                    playersActive.HP += heal
                    if playersActive.HP >= playersActive.MAXHP:
                        playersActive.HP = playersActive.MAXHP
                        lastAction = f"Player {player} fully healed {playersActivePokemon[player-1].Name}."
                    else:
                        lastAction = f"Player {player} healed {playersActivePokemon[player-1].Name} by {int(10000*(heal/playersActive.MAXHP))/100}%"
                else:
                    lastAction = f"Player {player} attempted to heal {playersActivePokemon[player-1].Name}, but failed."
            elif choice == "E": # Run Away
                ranAway = True
                lastAction = f"Player {player} ran away."
                if player == 1:
                    winner = 2
                else:
                    winner = 1
                break
        if winner != None:
            break
clearShell()
print(f"\n\t\tPlayer {winner} has won because {lastAction}")