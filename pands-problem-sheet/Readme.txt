Programming and Scripting Weekly Task Readme

Contents

1. 	Introduction
2. 	Resources
3.	Submissions
	3.1 	Week 1 - Introduction & GitHub Account Creation
	3.2 	Week 2 - bmi.py
	3.3 	Week 3 - secondstring.py
	3.4 	Week 4 - collatz.py
	3.5 	Week 5 - weekday.py
	3.6 	Week 6 - squareroot.py
	3.7 	Week 7 - es.py
	3.8 	Week 8 - plottask.py
4.	Changelog

				1. Introduction

				2. Resources

				3. Submissions

			3.1 Week 1 - Introduction & GitHub Account Creation

The Weekly task for week 1 involved downloading the required software, pulling sample code from GitHub creating a GitHub account and adding, commiting and push an initial GitHub depository.

Required software was installed form the following locations:

cmder: https://cmder.net/
Notepad++: http://notepad-plus-plus.org/
Anaconda: https://www.anaconda.com/products/individual
VS Code: https://code.visualstudio.com/Download
Git: https://git-scm.com/downloads

GitHub account was created at: https://github.com/

			3.2 Week 2 - bmi.py
A program that calculates bmi.
The second weekly task and the first coding task was to write a program that calculated BMI. BMI (Body Mass Index), is a formula developed in 1972 in the Journal of Chronic Diseases as an indicator of obesity. The formula
is BMI = weight(kg) / (height (m))^2. This formula was obtained from https://www.calculatorsoup.com/calculators/health/bmi-calculator.php. 
Variables for the formula were obtained using an input command. Because the program asks for height in cm, it had to be converted to meters before being used in the formula. Other obstacles involved converting the inputted answers from a string format into a float format so as to be 
able to be used by the formula. When testing the program, answers were compared to a calculator found at https://www.calculator.net/bmi-calculator.html to ensure the accuracy from the program. Further elaborating on this 
program could involve the option to use imperial measurements (There is a different BMI formula for this) and indicating the range that the user falls into.

BMI Origin: Keys A, Fidanza F, Karvonen MJ, Kimura N, Taylor HL (July 1972). "Indices of relative weight and obesity". Journal of Chronic Diseases. 25 (6): 329–343.

			3.3 Week 3 - secondstring.py
A program that takes asks a user to input a string and outputs every second letter in reverse order. 
Initially, my code for this was quite long and involved a for loop that would create move elements in the string from the 
beginning to the end. I also experimented with using a reverse function. Upon further reading into NumPy array slicing, this seemed much cleaner and I ended up going with this.

Array slicing: https://www.w3schools.com/python/numpy/numpy_array_slicing.asp#:~:text=Slicing%20arrays,start%3Aend%3Astep%5D%20.
For loops: https://www.w3schools.com/python/python_for_loops.asp
Reverse function: https://www.w3schools.com/python/ref_func_reversed.asp

			3.4 Week 4 - collatz.py
Program that asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one
Have the program end if the current value is one.
This program introduce while loops and if / else functions. These were researched at https://www.w3schools.com/python/python_while_loops.asp.

			3.5 Week 5 - weekday.py
Program that outputs whether or not today is a weekday. This program involved arrays and extra research into specific functions was needed. The strftime and datetime functions were researched at https://www.programiz.com/python-programming/datetime/strftime.
The datetime.today funtions gets the current date. This is then converted to a specific format by the strftime function. In this case, adding the directive of %A converts the date to the full name of the day of the week. Other directive for different formats
can be found in the link above.
	
			3.6 Week 6 - squareroot.py
Program that takes a positive floating-point number as input and outputs an approximation of its square root. This could not be done with the built in Python funtion and therefore required some research into the algorithm required to get the square root of
a number. The equation to do so was acquired from https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/#:~:text=Let%20N%20be%20any%20number,correct%20square%20root%20of%20N. The equation is applied to the original number as a first guess.
The answer to this equation is then used as the next guess, which is inputted into the equation again to get the next guess and so on. Originally, I used a for loop with an arbitrary number of iterations that was large enough to work and any non-massive number.
After some advice, I changes the program to iterate through the equation using a while loop until a certain precision criteria was met. The precision chosen was within 0.01 as the answer was being rounded down to .1.

			3.7 Week 7 - es.py
Program that reads in a text file and outputs the number of e's it contains. This program required some research into the sys function, specifically the sys.argv function. This was researched at https://www.knowledgehut.com/blog/programming/sys-argv-python-examples.
Also new in this program was the introduction of the with statement in python, using with open to read the file and assign it to a variable. This was researched at https://www.geeksforgeeks.org/with-statement-in-python/

			3.8 Week 8 - plottask.py

A program that that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes. I had experimented with some Seaborn functions, but preffered the simplicity of the matplotlib code

Information on the different plot elements were obtained primarily from matplotlib.org:

Axis ticks - 			https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
Legend - 			https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html
Grid - 				https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html
Points, styles and colours - 	https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

Seaborn fuctions were researced at https://seaborn.pydata.org/generated/seaborn.lineplot.html



4. Changelog

20/01/21 - Creation and upload of GitHub Repository
28/01/21 - Creation and upload of bmi.py
04/02/21 - Creation and upload of secondstring.py
10/02/21 - Creation and upload of collatz.py
17/02/21 - Creation and upload of weekday.py
25/02/21 - Creation and upload of squareroot.py
04/03/21 - Creation and upload of es.py
10/03/21 - Creation and upload of plottask.py
	 - Changed the title of collatz.py from pythonCollatz.py to collatz.py
11/03/21 - Fixed error in secondString.py function name
22/03/21 - Messed around with Seaborn graphs in plottask.py. Commented out as may add to later on.
11/04/21 - Included more comments and references in bmi.py and secondstring.py
14/04/21 - Included more comments and references in collatz.py and weekday.py
15/04/21 - Included more comments and referneces in squareroot.py, es.py
	 - Changed code in squareroot.py to iterate until precision was met


