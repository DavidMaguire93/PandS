# Program that reads in a text file and outputs the number of e's it contains
# Author: David Maguire

# Import sys module to take filename from command line argument
import sys

# Assign target filename to filename in program (sys.argv[0] is this program script, sys.argv[1] is first command line argument)
filename = sys.argv[1]

# Assign a count to 0 to add as e's are encountered
eCount = 0

# Open and read file
with open (filename,'r') as fileECount:
    data = fileECount.read()

# For every character in file, if character is 'e', raise count by one
    for char in data:
        if char == "e":
            eCount += 1

# Print resulting count
    print(eCount)