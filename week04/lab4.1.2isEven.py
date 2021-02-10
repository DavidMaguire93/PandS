# Asks the user to enter in a number, and the program will tell the user if the number is even or odd.
# Author: David Maguire

# Ask for number
number = int(input("Enter a number: "))

# Check if even or odd by getting modulus
if (number % 2) == 0:
    print(number, "is an even number")
else:
    print(number, "is an odd number")