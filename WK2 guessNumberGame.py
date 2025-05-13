""" A program that takes user guess of number in a range between 1 - 10 """

import random

def guessNumber():
    numberToGuess = random.randint(1, 10)
    guess = None

    while guess != numberToGuess:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < numberToGuess:
            print("Too low")
        elif guess > numberToGuess:
            print("Too high")

    print("congratulations! ")

guessNumber()
