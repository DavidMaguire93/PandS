# Exploring Iris
# Author: David Maguire
# Data obtained from https://datahub.io/machine-learning/iris#data
# Code taken from https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# Also taken from https://datahub.io/machine-learning/iris#data


# Import packages

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load csv
iris = pd.read_csv("iris.csv") 

# Convert to dataframe and add columns (columns names according to iris.names)
iris = pd.DataFrame(iris)
iris.columns = ["sepallength","sepalwidth","petallength","petalwidth","class"]

# Assigning variables to columns
sepallength = iris["sepallength"]
sepalwidth = iris["sepalwidth"]
petallength = iris["petallength"]
petalwidth = iris["petalwidth"]
irisclass = iris["class"]


# Full print of dataset. Comment out when not needed
#print(iris)


# Mean, median, min, max, first and third quartile of all quantitative variables
irismean = iris.mean()
irismedian = iris.median()
irismin = iris.min()
irismax = iris.max()
iris25 = iris.quantile(q = 0.25)
iris75 = iris.quantile(q = 0.75)

"""
# Printout analysis with descriptions for readability
print("mean\n", irismean)
print("median\n", irismedian)
print("min\n", irismin)
print("max\n", irismax)
print("first quartile\n", iris25)
print("third quartile\n", iris75)
"""

"""
Name of 3 species for reference
Iris-setosa
Iris-versicolor
Iris-virginica

Name of variables for reference
Sepal Length
Sepal Width
Petal Length
Petal Width
Class
"""

# Assigning variable to filter of data by species
setosa = iris.loc[iris["class"] == "Iris-setosa"]
versicolor = iris.loc[iris["class"] == "Iris-versicolor"]
virginica = iris.loc[iris["class"] == "Iris-virginica"]

# Mean of each species
setosamean = setosa.mean()
versicolormean = versicolor.mean()
virginicamean = virginica.mean()

"""
# Printouts of mean
print("setosa mean\n", setosamean)
print("versicolor mean\n", versicolormean)
print("virginica mean\n", virginicamean)
"""
"""
# Simple histograph of all quantitative variables
iris.hist(bins = 30)
plt.show()
"""
"""
# Assigning a variable to represent colours for each class to use in plots if needed
# This is needed in pyplot scatter graphs but is not for Seaborne scatter plots
classcols = []
for element in irisclass:
    if element == "Iris-setosa":
        classcols.append("green")
    elif element == "Iris-versicolor":
        classcols.append("red")
    elif element == "Iris-virginica":
        classcols.append("blue")
"""
# Testing array is appended properly
#print(classcols)

"""
Scatter plots using pyplot, can uncomment if individual scatter plots are needed but seaborn pairplot has all relationships

plt.scatter(petalwidth, sepalwidth, c = classcols)
plt.scatter(petallength, sepallength, c = classcols)
plt.show()
"""

# Seaborn pairplot, containing scatter plots of all variable relationships as well as class distribution of individual variables
sns.pairplot(iris, hue = "class")
plt.show()

# Individual Pearsons correlations, commented out as numpy corr function shows correlation for multiple variables
#pearsons = np.corrcoef(petalwidth,petallength)
#print(pearsons)


# Assigning functions for correlation of full dataset as well as by class
iriscorr = iris.corr()
setosacorr = setosa.corr()
versicorr = versicolor.corr()
virginicacorr = virginica.corr()

# Printout of correlations with some titles
print("Iris Correlation\n", iriscorr)
print("Setosa Correlation\n", setosacorr)
print("Versicolor Correlation\n", versicorr)
print("Virginica Correlation\n", virginicacorr)