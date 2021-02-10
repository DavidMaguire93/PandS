# Program that keeps reading numbers until the user enters a 0 
# The program then prints out each of the numbers entered and the average of them
# Author: David Maguire

# Assign numbers to list
numbers = []

# Ask for number
number = int(input("Enter a number (0 to quit): "))

# While number is not 0, add to list, ask for another
while number != 0:
    numbers.append(number)

    number = int(input("Enter another number (o to quit): "))

# Print all numbers entered
for value in numbers:
    print (value)

# Print average of numbers
average = float(sum(numbers)) / len(numbers)
print ("This average is",average)
