# Program that reads in a students percentage mark andprints out corresponding the grade
# Author: David Maguire

percent = int(input("Enter the percentage: "))

# Check for invalid number first
if percent < 0 or percent > 100:
    print("Please enter a valid number")

# Then check high mar, then go down from there
# I could also go up from low mark
elif percent >= 70:
    print("Distinction")
elif percent >= 60:
    print("Merit 1")
elif percent >= 50:
    print("Merit 2")
elif percent >= 40:
    print("Pass")
else:
    print("Fail")
