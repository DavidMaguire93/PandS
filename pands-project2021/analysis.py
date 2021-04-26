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

# Convert to dataframe using pandas and add columns (columns names according to iris.names)
# This makes it easier to select individual columns
iris = pd.DataFrame(iris)
iris.columns = ["sepallength","sepalwidth","petallength","petalwidth","class"]

# Assigning variables to columns using dataframe and []
sepallength = iris["sepallength"]
sepalwidth = iris["sepalwidth"]
petallength = iris["petallength"]
petalwidth = iris["petalwidth"]
irisclass = iris["class"]

# Assigning variable to filter of data by species
setosa = iris.loc[iris["class"] == "Iris-setosa"]
versicolor = iris.loc[iris["class"] == "Iris-versicolor"]
virginica = iris.loc[iris["class"] == "Iris-virginica"]


# Grouping variables by species in order to differentiate by color in scatterplots
setosasepallength = setosa["sepallength"]
setosasepalwidth = setosa["sepalwidth"]
setosapetallength = setosa["petallength"]
setosapetalwidth = setosa["petalwidth"]

versicolorsepallength = versicolor["sepallength"]
versicolorsepalwidth = versicolor["sepalwidth"]
versicolorpetallength = versicolor["petallength"]
versicolorpetalwidth = versicolor["petalwidth"]

virginicasepallength = virginica["sepallength"]
virginicasepalwidth = virginica["sepalwidth"]
virginicapetallength = virginica["petallength"]
virginicapetalwidth = virginica["petalwidth"]


# Full print of dataframe. Comment out when not needed
#print(iris)


# Mean, median, min, max, first and third quartile of all quantitative variables
irismean = iris.mean()
irismedian = iris.median()
irismin = iris.min()
irismax = iris.max()
iris25 = iris.quantile(q = 0.25)
iris75 = iris.quantile(q = 0.75)
irisstdev = iris.std()


# Printout analysis with descriptions for readability
print("mean\n", irismean)
print("median\n", irismedian)
print("min\n", irismin)
print("max\n", irismax)
print("first quartile\n", iris25)
print("third quartile\n", iris75)
print("standard dev\n", irisstdev)


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

# Simple histograph of all quantitative variables
iris.hist(bins = 30)
plt.show()


# Scatter plots using pyplot, can uncomment if individual scatter plots are needed but seaborn pairplot has all relationships
# In order to have legend that labels species by color, 3 separate scatter plots must be used in one graph, which can be labelled separately
# classcols (above) can be used in a single scatter plot to label species by color but a legend is more difficult to implement
# To do this, simply use c = classcols
# Naming sequence of splpw : (s)etosa (p)etal (l)ength (p)etal (w)idth

splpw = plt.scatter(setosapetallength, setosapetalwidth, c = "green")
vsplpw = plt.scatter(versicolorpetallength, versicolorpetalwidth, c = "red")
vgplpw = plt.scatter(virginicapetallength, virginicapetalwidth, c = "blue")
plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend([splpw, vsplpw, vgplpw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

splsl = plt.scatter(setosapetallength, setosasepallength, c = "green")
vsplsl = plt.scatter(versicolorpetallength, versicolorsepallength, c = "red")
vgplsl = plt.scatter(virginicapetallength, virginicasepallength, c = "blue")
plt.title("Petal Length vs Sepal Length")
plt.xlabel("Petal Length")
plt.ylabel("Sepal Length")
plt.legend([splsl, vsplsl, vgplsl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

splsw = plt.scatter(setosapetallength, setosasepalwidth, c = "green")
vsplsw = plt.scatter(versicolorpetallength, versicolorsepalwidth, c = "red")
vgplsw = plt.scatter(virginicapetallength, virginicasepalwidth, c = "blue")
plt.title("Petal Length vs Sepal Width")
plt.xlabel("Petal Length")
plt.ylabel("Sepal Width")
plt.legend([splsw, vsplsw, vgplsw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

sslpl = plt.scatter(setosasepallength, setosapetallength, c = "green")
vsslpl = plt.scatter(versicolorsepallength, versicolorpetallength, c = "red")
vgslpl = plt.scatter(virginicasepallength, virginicapetallength, c = "blue")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend([sslpl, vsslpl, vgslpl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

sslpw = plt.scatter(setosasepallength, setosapetalwidth, c = "green")
vsslpw = plt.scatter(versicolorsepallength, versicolorpetalwidth, c = "red")
vgslpw = plt.scatter(virginicasepallength, virginicapetalwidth, c = "blue")
plt.title("Sepal Length vs Petal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.legend([sslpw, vsslpw, vgslpw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

sslsw = plt.scatter(setosasepallength, setosasepalwidth, c = "green")
vsslsw = plt.scatter(versicolorsepallength, versicolorsepalwidth, c = "red")
vgslsw = plt.scatter(virginicasepallength, virginicasepalwidth, c = "blue")
plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend([sslsw, vsslsw, vgslsw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

spwpl = plt.scatter(setosapetalwidth, setosapetallength, c = "green")
vspwpl = plt.scatter(versicolorpetalwidth, versicolorpetallength, c = "red")
vgpwpl = plt.scatter(virginicapetalwidth, virginicapetallength, c = "blue")
plt.title("Petal Width vs Petal Length")
plt.xlabel("Petal Width")
plt.ylabel("Petal Length")
plt.legend([spwpl, vspwpl, vgpwpl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

spwsl = plt.scatter(setosapetalwidth, setosasepallength, c = "green")
vspwsl = plt.scatter(versicolorpetalwidth, versicolorsepallength, c = "red")
vgpwsl = plt.scatter(virginicapetalwidth, virginicasepallength, c = "blue")
plt.title("Petal Width vs Sepal Length")
plt.xlabel("Petal Width")
plt.ylabel("Sepal Length")
plt.legend([spwsl, vspwsl, vgpwsl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

spwsw = plt.scatter(setosapetalwidth, setosasepalwidth, c = "green")
vspwsw = plt.scatter(versicolorpetalwidth, versicolorsepalwidth, c = "red")
vgpwsw = plt.scatter(virginicapetalwidth, virginicasepalwidth, c = "blue")
plt.title("Petal Width vs Sepal Width")
plt.xlabel("Petal Width")
plt.ylabel("Sepal Width")
plt.legend([spwsw, vspwsw, vgpwsw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

sswpl = plt.scatter(setosasepalwidth, setosapetallength, c = "green")
vsswpl = plt.scatter(versicolorsepalwidth, versicolorpetallength, c = "red")
vgswpl = plt.scatter(virginicasepalwidth, virginicapetallength, c = "blue")
plt.title("Sepal Width vs Petal Length")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Length")
plt.legend([sswpl, vsswpl, vgswpl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

sswpw = plt.scatter(setosasepalwidth, setosapetalwidth, c = "green")
vsswpw = plt.scatter(versicolorsepalwidth, versicolorpetalwidth, c = "red")
vgswpw = plt.scatter(virginicasepalwidth, virginicapetalwidth, c = "blue")
plt.title("Sepal Width vs Petal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.legend([sswpw, vsswpw, vgswpw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()

sswsl = plt.scatter(setosasepalwidth, setosasepallength, c = "green")
vsswsl = plt.scatter(versicolorsepalwidth, versicolorsepallength, c = "red")
vgswsl = plt.scatter(virginicasepalwidth, virginicasepallength, c = "blue")
plt.title("Sepal Width vs Sepal Length")
plt.xlabel("Sepal Width")
plt.ylabel("Sepal Length")
plt.legend([sswsl, vsswsl, vgswsl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.show()


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

# Testing array is appended properly
#print(classcols)

# This format can be used but no legend can be inserted
plt.scatter(petallength, petalwidth, c = classcols)
plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.show()
"""


# Seaborn pairplot, containing scatter plots of all variable relationships as well as class distribution of individual variables
# I find this far more simple and effective that the individual scatter pyplots above and this is what I would use if only one method was allowed
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
print("Iris Correlation\n", iriscorr, "\n")
print("Setosa Correlation\n", setosacorr, "\n")
print("Versicolor Correlation\n", versicorr, "\n")
print("Virginica Correlation\n", virginicacorr, "\n")