# bmi.py
# Programme that calculates bmi
# Author: David Maguire
# Output was compared against calculator from https://www.calculator.net/bmi-calculator.html

# Ask for weight in kg and convert to float
# This is required because the input will give the number in a string format
weight = float(input("Enter your weight in kg: "))

# Ask for height in cm and convert to float (Same reason as for weight)
# Also convert from cm to m for calculation by dividing by 100
height = (float(input("Enter your height in cm: "))) / 100

# Calculate bmi using W / H^2
# Formula taken from https://www.calculatorsoup.com/calculators/health/bmi-calculator.php
bmi = weight / (height**2)

# Print out result using {} and .format
# An alternative would be to convert back into string using str function
print ('Your bmi is {}'.format(bmi))