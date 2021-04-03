# Exploring Iris
# Author: David Maguire
# Data obtained from https://datahub.io/machine-learning/iris#data
# Code taken from https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# Also taken from https://datahub.io/machine-learning/iris#data



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load csv
iris = pd.read_csv("iris.csv") 

# Convert to dataframe and add columns
iris = pd.DataFrame(iris)
iris.columns = ["sepallength","sepalwidth","petallength","petalwidth","class"]

# Comment out when not needed
#print(iris)


# Mean, median, min, max, first and third quartile of all quantitative variables
irismean = iris.mean()
irismedian = iris.median()
irismin = iris.min()
irismax = iris.max()
iris25 = iris.quantile(q = 0.25)
iris75 = iris.quantile(q = 0.75)


# Printout analysis with descriptions for readability
print("mean\n", irismean)
print("median\n", irismedian)
print("min\n", irismin)
print("max\n", irismax)
print("first quartile\n", iris25)
print("third quartile\n", iris75)


"""
Name of 3 species for reference
Iris-setosa
Iris-versicolor
Iris-virginica
"""


# Assigning variable to filter of data by species
setosa = iris.loc[iris["class"] == "Iris-setosa"]
versicolor = iris.loc[iris["class"] == "Iris-versicolor"]
virginica = iris.loc[iris["class"] == "Iris-virginica"]

# Mean of each species
setosamean = setosa.mean()
versicolormean = versicolor.mean()
virginicamean = virginica.mean()

# Printouts of mean
print("setosa mean\n", setosamean)
print("versicolor mean\n", versicolormean)
print("virginica mean\n", virginicamean)

# Simple histograph of all quantitative variables
iris.hist(bins = 30)
#plt.show()