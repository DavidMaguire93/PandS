# weekday.py
# Program that outputs whether or not today is a weekday
# strftime researched at https://www.programiz.com/python-programming/datetime/strftime
# Author: David Maguire

# Import datetime for today's date function
import datetime

# Use strftime to get a string of today's date
# Use datetime.today() gets today's date. strf converts date to specific format depending on % directive
# %A is a string format for the name of the day of the given date (Long version of day e.g. Monday, %a is short version e.g. Mon)
today = datetime.datetime.today().strftime('%A')

# Create list of weekdays and weekend (weekend is not actually needed)
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"] 
weekend = ["Saturday", "Sunday"]

# If today is in list of weekdays print weekday response
if today in weekdays:
    print("Yes, unfortunately today is a weekday.")

# Otherwise, print other response
else:
    print("It is the weekend, yay!")