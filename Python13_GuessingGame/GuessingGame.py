# Random number selected by program
# User will guess number and program will give hint
# When guessed correctly user will succeed with step taken

import random

# generate random number
jackpot = random.randint(1, 100)

guess = int(input("Enter your guess : "))
counter = 1

while guess != jackpot:
    if guess < jackpot:
        print("Guess Higher")
    else:
        print("Guess Lower")

    guess = int(input("Enter your guess : "))
    counter+=1
print("Correct Answer!!")
print("You took : ", counter, "attempts")