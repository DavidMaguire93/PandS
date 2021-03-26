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


# Simple analysis
irismean = iris.mean()
irismedian = iris.median()
irismin = iris.min()
irismax = iris.max()

print(irismean)
print(irismedian)
print(irismin)
print(irismax)

# Simple histograph of all variables
iris.hist(bins = 30)
plt.show()