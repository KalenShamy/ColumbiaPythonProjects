# Kalen Shamy - 6/29/2021

import random

def uinput(string):
    return input(string + " ")

def _th(n):
    if n == 1:
        return "1st"
    elif n == 2:
        return "2nd"
    elif n == 3:
        return "3rd"
    elif n < 10:
        return f"{n}th"
    else:
        return "last"

secretNumber = random.randrange(1,50)
guesses = 1
lastLength = 0
closestNumber = 0

print(f"The object of the game is to guess my secret number. You have 10 guesses.\n")

while guesses <= 10:
    guess = uinput(f"What is your {_th(abs(guesses))} guess?")
    canContinue = False
    while canContinue == False:
        try:
            guess = int(guess)
            canContinue = True
        except ValueError:
            guess = uinput(f"Come on, don't try to waste guesses. What is your {_th(guesses)} guess?")
    if abs(guess - secretNumber) == 0:
        print(f"Spot on! You got my number, {secretNumber} on your {_th(abs(guesses))} guess!")
        break
    elif lastLength < abs(secretNumber - guess) and guesses != 1:
        lastLength = abs(secretNumber - guess)
        print("Colder!")
    elif lastLength > abs(secretNumber - guess) and guesses != 1:
        lastLength = abs(secretNumber - guess)
        print("Hotter!")
    elif guesses != 1:
        print("Equally hot as last time, the number is in between the two!")
    else:
        print("Nope, guess again!")
        closestNumber = guess
    if lastLength < abs(secretNumber - closestNumber):
        closestNumber = guess
    guesses += 1
    if guesses == 10:
        print(f"Unfortunately you didn't guess my number. It was {secretNumber}. The closest you got was {closestNumber} :(")