# pythonCollatz.py
# Program that asks the user to input any positive integer and outputs the successive values of the following calculation
# At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one
# Have the program end if the current value is one
# While loops researched at https://www.w3schools.com/python/python_while_loops.asp
# Author: David Maguire

# Assign input to number
# Convert input from string (default for input) to int for use in formulae
number = int(input("Please enter a positive integer: "))

# Print number
print(number)

# If number is not equal to one, apply correct calculation and assign to new number
# Using a while loop and if / else so calulation repeats itself if the number is not 1
while number !=1:
    if number % 2 == 0:
        newNumber = int(number / 2)
    else:
        newNumber = (number * 3) + 1

# Print new number
    print(newNumber)

# Assign number as value of new number so while loop restarts with check for equals one
    number = newNumber