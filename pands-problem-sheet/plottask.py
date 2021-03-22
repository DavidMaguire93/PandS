# plottask.py
# Program called plottask.py that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes
# Author: David Maguire

# Import numpy and matplotlib.pyplot
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#import pandas as pd

# Assign range to x
# Assign fuctions to variables
x = np.array(range(0,4))
fx = x
gx = x * x 
hx = x ** 3

"""

sns.lineplot(x = x,y = fx, hue = "function")
sns.lineplot(x = x,y = gx)
sns.lineplot(x = x,y = hx)
plt.show()

"""

# Plot functions, label and style with points, line dashes and colours
plt.plot(x,fx,'.--b', label="f(x)", )
plt.plot(x,gx,'.--r', label="g(x)")
plt.plot(x,hx,'.--g', label="h(x)")

# Add legend, grid and title
plt.legend(fontsize = 'large')
plt.grid()
plt.title("Functions of X")

# Edit axes ticks (comment out / edit if range of x changes)
plt.yticks(np.arange(0, 31, step = 3))
plt.xticks(np.arange(0,4, step = 1))

# Show plot
plt.show()

