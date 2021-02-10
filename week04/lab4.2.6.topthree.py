#  Program that generates 10 random numbers (0-100), prints them out then prints out the top three
# Author: David Maguire

# Import randint
from random import randint

# Assign list to numbers
numbers = []

# Assign random number to number
number = randint(0,100)

# Add random number to list and get new random number while list is less than or equal to 10 numbers long
while len(numbers) <= 10:
    numbers.append(number)
    number = randint(0,100)

# Print 10 random numbers in list
print("10 random numbers")
print(numbers)

# Sort list decending
numbers.sort(reverse=True)

# Print first 3 elements of list
print("The top 3 are")
print(numbers[:3])