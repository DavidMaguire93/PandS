# Program that prompts the user to guess a number, the program should keep prompting the user to guess the number until the user gets the right on
# Also tells user if guess is too high or low
# Author: David Maguire

# Import randint
from random import randint

# Assign random value to correct answer
# Ask to enter guess, change to int
answer = randint (1, 100)
guess = int(input("Please guess the number: "))

# While loop, guess again if wrong
while guess != answer:

# If guess is greater than answer, print too high, otherwise, print too low
    if guess > answer:
        print( "too high")
    else:
        print ("too low")
    guess = int(input("Please guess again: "))

# Tell if correct
print("Well done! Yes the number was",answer)
