# secondString.py
# Program that takes asks a user to input a string and outputs every second letter in reverse order
# Author: David Maguire

# Ask for sentance
rawString = input("Please enter a sentance: ")

# Reverse string by starting from end and going backwards every 2nd char
reverseSkip = rawString[::-2]

# Print result
print(reverseSkip)