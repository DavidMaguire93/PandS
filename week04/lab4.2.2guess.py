# Program that prompts the user to guess a number, the program should keep prompting the user to guess the number until the user gets the right on
# Author: David Maguire

# Assign value to correct answer
# Ask to enter guess, change to int
answer = 30
guess = int(input("Please guess the number: "))

# While loop, guess again if wrong
while guess != answer:
    print("Wrong")
    guess = int(input("Please guess again: "))

# Tell if correct
print("Well done! Yes the number was",answer)
