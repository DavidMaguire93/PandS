# Exploring Iris
# Author: David Maguire
# Data obtained from https://datahub.io/machine-learning/iris#data
# Code taken from https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# Also taken from https://datahub.io/machine-learning/iris#data



import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load csv
iris = pd.read_csv("iris_csv.csv") 

# Printout of data (Comment out when not needed)

#print(iris)
#print(iris.head())
#print(iris.sample(10))

specificCols = iris[["sepallength", "class"]]

#print(specificCols.head(10))

# Some info about columns and shape (rows, columns) of dataset
#print(iris.columns)
#print(iris.shape)

# Print complete info of specific row
print(iris.iloc[5])

# Print row by search
print(iris.loc[iris["class"] == "Iris-setosa"])
