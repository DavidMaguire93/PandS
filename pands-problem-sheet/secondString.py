# secondString.py
# Program that takes asks a user to input a string and outputs every second letter in reverse order
# Author: David Maguire
# Array slicing code obtained from https://www.w3schools.com/python/numpy/numpy_array_slicing.asp#:~:text=Slicing%20arrays,start%3Aend%3Astep%5D%20.

# Ask for sentence
rawString = input("Please enter a sentence: ")

# Reverse string by starting from end and going backwards every 2nd char
# Format of [x:y:z] in below code is x = first element, y = last element and z = direction / every nth element (or [start:end:step])
# [::-1] would indicate a normal revers of string, while [::-2] skips every 2nd element
reverseSkip = rawString[::-2]

# Print result
print(reverseSkip)