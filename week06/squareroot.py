# Program that takes a positive floating-point number as input and outputs an approximation of its square root
# Author: David Maguire

# Based on Newton Square Root Method: Root = 0.5 * (X + (N / X)) 
# where N is the number given and X is a guess of the square root

# Define function
def sqrt(num):

    # Define max number of guesses (Needs to be higher for accuracy with much larger numbers)
    x = 500

    # Assign first guess to number given
    guess = float(num)

    # Run first guess through equation, then replace guess with result
    for count in range(1, x):
        root = (guess + (num / guess)) / 2
        guess = root

    # Print message and round result down to one decimal place
    print("The square root of ", num, "is approx", round(guess, 1))


# Ask for positive number and apply fuction to answer
var = float(input("Please enter a positive number: "))
sqrt(var)
