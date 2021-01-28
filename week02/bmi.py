# bmi.py
# Programme that calculates bmi
# Author: David Maguire

# Ask for weight in kg and convert to float
weight = float(input("Enter your weight in kg: "))

# Ask for height in cm and convert to float
# Also convert from cm to m for calculation
height = (float(input("Enter your height in cm: "))) / 100

# Calculate bmi using W / H^2
bmi = weight / (height**2)

print ('Your bmi is {}'.format(bmi))