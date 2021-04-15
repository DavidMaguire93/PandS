# squareroot.py
# Program that takes a positive floating-point number as input and outputs an approximation of its square root
# Author: David Maguire

# Based on Newton Square Root Method: Root = 0.5 * (X + (N / X))
# where N is the number given and X is a guess of the square root
# Method obtained from https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N

# Define function
def sqrt(num):

    # This equation iterates through a series of guessing and uses the answer as the new guess
    # The first guess must be the same as the number you are trying to get the square root from
    # Assign first guess to number given
    guess = float(num)
    
    # Using a while loop instead of a set number of iterations so the equation will go through more iterations for larger numbers but less for smaller numbers
    # As the answer is being rounded to 0.1, I used the next order of 10 down as a precision
    # For a 100% correct square number, num / guess = guess
    while (num / guess) < (guess - 0.01):

        # Applying formula and assigning it to a new variable called root
        root = (guess + (num / guess)) / 2

        # assigning the answer to the equation to the guess variable
        guess = root

        # This is for testing how many iterations are done
        #print(guess)
    

    # After specified precision is achieved, the while loop breaks and the next step is done
    # Print message and round result down to one decimal place
    print("The square root of ", num, "is approx", round(guess, 1))


# Ask for positive number and apply function to answer
var = float(input("Please enter a positive number: "))
sqrt(var)
