# Exploring Iris
# Author: David Maguire
# Data obtained from https://datahub.io/machine-learning/iris#data
# Code taken from https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
# Also taken from https://datahub.io/machine-learning/iris#data


# Import packages

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

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

# Creating of text file to append
# Open in write mode to overwrite anything that was there before
# Opening a temporary file which will be cleaned for a new file and then later deleted
f = open("iristemp.txt", "w")
f.write("Iris Dataset Variable Analysis\n\n*******************************")
f.close()

# Mean, median, min, max, first and third quartile of all quantitative variables
# Mean and stdev are rounded to be more in line with the other results
irismean = iris.mean().round(2)
irismedian = iris.median()
irismin = iris.min()
irismax = iris.max()
iris25 = iris.quantile(q = 0.25)
iris75 = iris.quantile(q = 0.75)
irisstdev = iris.std().round(2)
iriskurt = iris.kurt().round(2)
irisskew = iris.skew().round(2)

setosamean = setosa.mean().round(2)
setosamedian = setosa.median()
setosamin = setosa.min()
setosamax = setosa.max()
setosa25 = setosa.quantile(q = 0.25)
setosa75 = setosa.quantile(q = 0.75)
setosastdev = setosa.std().round(2)
setosakurt = setosa.kurt().round(2)
setosaskew = setosa.skew().round(2)

versicolormean = versicolor.mean().round(2)
versicolormedian = versicolor.median()
versicolormin = versicolor.min()
versicolormax = versicolor.max()
versicolor25 = versicolor.quantile(q = 0.25)
versicolor75 = versicolor.quantile(q = 0.75)
versicolorstdev = versicolor.std().round(2)
versicolorkurt = versicolor.kurt().round(2)
versicolorskew = versicolor.skew().round(2)

virginicamean = virginica.mean().round(2)
virginicamedian = virginica.median()
virginicamin = virginica.min()
virginicamax = virginica.max()
virginica25 = virginica.quantile(q = 0.25)
virginica75 = virginica.quantile(q = 0.75)
virginicastdev = virginica.std().round(2)
virginicakurt = virginica.kurt().round(2)
virginicaskew = virginica.skew().round(2)

# Assigning functions for correlation of full dataset as well as by class
iriscorr = iris.corr()
setosacorr = setosa.corr()
versicorr = versicolor.corr()
virginicacorr = virginica.corr()


# Using with open and opening the file in append mode so as not to overwrite what is was already written
with open("iristemp.txt", "a") as f:

# Printout to file out of analysis of full dataset with titles and line spaces
# Removing separators with sep = '' to remove space at start of printout
    print("\nFull Iris Dataset", file = f)
    print("\nVariable Means\n", irismean, sep = '',file = f)
    print("\nVariable Medians\n", irismedian, sep = '', file = f)
    print("\nVariable Min\n", irismin, sep = '', file = f)
    print("\nVariable Max\n", irismax, sep = '', file = f)
    print("\nVariable First Quartiles\n", iris25, sep = '', file = f)
    print("\nVariable Third Quartiles\n", iris75, sep = '', file = f)
    print("\nVariable Standard Deviation\n", irisstdev, sep = '', file = f)
    print("\nVariable Kurtosis\n", iriskurt, sep = '', file = f)
    print("\nVariable Skewness\n", irisskew, sep = '', file = f)

# Printout to file of same analysis but just on Setosa Species

    print("\n\n*******************************\nSetosa Dataset", file = f)
    print("\nVariable Means\n", setosamean, sep = '',file = f)
    print("\nVariable Medians\n", setosamedian, sep = '', file = f)
    print("\nVariable Min\n", setosamin, sep = '', file = f)
    print("\nVariable Max\n", setosamax, sep = '', file = f)
    print("\nVariable First Quartiles\n", setosa25, sep = '', file = f)
    print("\nVariable Third Quartiles\n", setosa75, sep = '', file = f)
    print("\nVariable Standard Deviation\n", setosastdev, sep = '', file = f)
    print("\nVariable Kurtosis\n", setosakurt, sep = '', file = f)
    print("\nVariable Skewness\n", setosaskew, sep = '', file = f)
    
# Printout to file of same analysis but just on Versicolor Species

    print("\n\n*******************************\nVersicolor Dataset", file = f)
    print("\nVariable Means\n", versicolormean, sep = '',file = f)
    print("\nVariable Medians\n", versicolormedian, sep = '', file = f)
    print("\nVariable Min\n", versicolormin, sep = '', file = f)
    print("\nVariable Max\n", versicolormax, sep = '', file = f)
    print("\nVariable First Quartiles\n", versicolor25, sep = '', file = f)
    print("\nVariable Third Quartiles\n", versicolor75, sep = '', file = f)
    print("\nVariable Standard Deviation\n", versicolorstdev, sep = '', file = f)
    print("\nVariable Kurtosis\n", versicolorkurt, sep = '', file = f)
    print("\nVariable Skewness\n", versicolorskew, sep = '', file = f)

# Printout to file of same analysis but just on Virginica Species

    print("\n\n*******************************\nVirginica Dataset", file = f)
    print("\nVariable Means\n", virginicamean, sep = '',file = f)
    print("\nVariable Medians\n", virginicamedian, sep = '', file = f)
    print("\nVariable Min\n", virginicamin, sep = '', file = f)
    print("\nVariable Max\n", virginicamax, sep = '', file = f)
    print("\nVariable First Quartiles\n", virginica25, sep = '', file = f)
    print("\nVariable Third Quartiles\n", virginica75, sep = '', file = f)
    print("\nVariable Standard Deviation\n", virginicastdev, sep = '', file = f)
    print("\nVariable Kurtosis\n", virginicakurt, sep = '', file = f)
    print("\nVariable Skewness\n", virginicaskew, sep = '', file = f)

# Printout to file of correlations with some titles
    print("*******************************\nIris Correlation\n", iriscorr, "\n", sep = '',file = f)
    print("Setosa Correlation\n", setosacorr, "\n", sep = '',file = f)
    print("Versicolor Correlation\n", versicorr, "\n", sep = '',file = f)
    print("Virginica Correlation\n", virginicacorr, "\n", sep = '',file = f)

with open("iristemp.txt", "r") as f:
    lines = f.readlines()

with open("iris.txt", "w") as f:
    for line in lines:
        if "dtype" not in line:
            f.write(line)
os.remove("iristemp.txt")

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




# Individual Pearsons correlations, commented out as numpy corr function shows correlation for multiple variables
#pearsons = np.corrcoef(petalwidth,petallength)
#print(pearsons)




# Simple histograph of all quantitative variables
# Using bins = 30 to give a more detailed view (default is 10)
# Colored to be similar to color of iris, colors can be found at https://matplotlib.org/2.0.2/examples/color/named_colors.html
# Using suptitle to give a title to the whole image. using .title only gives a title to the 4th plot only
iris.hist(bins = 30, color = 'darkorchid')
plt.suptitle("Iris Histograms")
plt.savefig("Iris Histogram")
plt.show()

# Histogram of Setosa variables
# Taking out bins = 30 as the default is 10 and this keeps the number to 5 data points per bin on average
setosa.hist(color = 'darkorchid')
plt.suptitle("Setosa Histograms")
plt.savefig("Setosa Histogram")
plt.show()

# Histogram of Versicolor Variables
versicolor.hist(color = 'darkorchid')
plt.suptitle("Versicolor Histograms")
plt.savefig("Versicolor Histogram")
plt.show()

# Histogram of Virginica Variables
virginica.hist(color = 'darkorchid')
plt.suptitle("Virginica Histograms")
plt.savefig("Virginica Histogram")
plt.show()



# Scatter plots using pyplot, can uncomment if individual scatter plots are needed but seaborn pairplot has all relationships
# In order to have legend that labels species by color, 3 separate scatter plots must be used in one graph, which can be labelled separately
# classcols (below) can be used in a single scatter plot to label species by color but a legend is more difficult to implement
# Save plots to PNG using plt.savefig (PNG is the default format)
# Naming sequence of splpw : (s)etosa (p)etal (l)ength (p)etal (w)idth

splpw = plt.scatter(setosapetallength, setosapetalwidth, c = "green")
vsplpw = plt.scatter(versicolorpetallength, versicolorpetalwidth, c = "red")
vgplpw = plt.scatter(virginicapetallength, virginicapetalwidth, c = "blue")
plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend([splpw, vsplpw, vgplpw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Petal Length vs Petal Width")
plt.show()

splsl = plt.scatter(setosapetallength, setosasepallength, c = "green")
vsplsl = plt.scatter(versicolorpetallength, versicolorsepallength, c = "red")
vgplsl = plt.scatter(virginicapetallength, virginicasepallength, c = "blue")
plt.title("Petal Length vs Sepal Length")
plt.xlabel("Petal Length")
plt.ylabel("Sepal Length")
plt.legend([splsl, vsplsl, vgplsl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Petal Length vs Sepal Length")
plt.show()

splsw = plt.scatter(setosapetallength, setosasepalwidth, c = "green")
vsplsw = plt.scatter(versicolorpetallength, versicolorsepalwidth, c = "red")
vgplsw = plt.scatter(virginicapetallength, virginicasepalwidth, c = "blue")
plt.title("Petal Length vs Sepal Width")
plt.xlabel("Petal Length")
plt.ylabel("Sepal Width")
plt.legend([splsw, vsplsw, vgplsw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Petal Length vs Sepal Width")
plt.show()

sslpl = plt.scatter(setosasepallength, setosapetallength, c = "green")
vsslpl = plt.scatter(versicolorsepallength, versicolorpetallength, c = "red")
vgslpl = plt.scatter(virginicasepallength, virginicapetallength, c = "blue")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend([sslpl, vsslpl, vgslpl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Sepal Length vs Petal Length")
plt.show()

sslpw = plt.scatter(setosasepallength, setosapetalwidth, c = "green")
vsslpw = plt.scatter(versicolorsepallength, versicolorpetalwidth, c = "red")
vgslpw = plt.scatter(virginicasepallength, virginicapetalwidth, c = "blue")
plt.title("Sepal Length vs Petal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Width")
plt.legend([sslpw, vsslpw, vgslpw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Sepal Length vs Petal Width")
plt.show()

sslsw = plt.scatter(setosasepallength, setosasepalwidth, c = "green")
vsslsw = plt.scatter(versicolorsepallength, versicolorsepalwidth, c = "red")
vgslsw = plt.scatter(virginicasepallength, virginicasepalwidth, c = "blue")
plt.title("Sepal Length vs Sepal Width")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend([sslsw, vsslsw, vgslsw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Sepal Length vs Sepal Width")
plt.show()

spwpl = plt.scatter(setosapetalwidth, setosapetallength, c = "green")
vspwpl = plt.scatter(versicolorpetalwidth, versicolorpetallength, c = "red")
vgpwpl = plt.scatter(virginicapetalwidth, virginicapetallength, c = "blue")
plt.title("Petal Width vs Petal Length")
plt.xlabel("Petal Width")
plt.ylabel("Petal Length")
plt.legend([spwpl, vspwpl, vgpwpl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Petal Width vs Petal Length")
plt.show()

spwsl = plt.scatter(setosapetalwidth, setosasepallength, c = "green")
vspwsl = plt.scatter(versicolorpetalwidth, versicolorsepallength, c = "red")
vgpwsl = plt.scatter(virginicapetalwidth, virginicasepallength, c = "blue")
plt.title("Petal Width vs Sepal Length")
plt.xlabel("Petal Width")
plt.ylabel("Sepal Length")
plt.legend([spwsl, vspwsl, vgpwsl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Petal Width vs Sepal Length")
plt.show()

spwsw = plt.scatter(setosapetalwidth, setosasepalwidth, c = "green")
vspwsw = plt.scatter(versicolorpetalwidth, versicolorsepalwidth, c = "red")
vgpwsw = plt.scatter(virginicapetalwidth, virginicasepalwidth, c = "blue")
plt.title("Petal Width vs Sepal Width")
plt.xlabel("Petal Width")
plt.ylabel("Sepal Width")
plt.legend([spwsw, vspwsw, vgpwsw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Petal Width vs Sepal Width")
plt.show()

sswpl = plt.scatter(setosasepalwidth, setosapetallength, c = "green")
vsswpl = plt.scatter(versicolorsepalwidth, versicolorpetallength, c = "red")
vgswpl = plt.scatter(virginicasepalwidth, virginicapetallength, c = "blue")
plt.title("Sepal Width vs Petal Length")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Length")
plt.legend([sswpl, vsswpl, vgswpl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Sepal Width vs Petal Length")
plt.show()

sswpw = plt.scatter(setosasepalwidth, setosapetalwidth, c = "green")
vsswpw = plt.scatter(versicolorsepalwidth, versicolorpetalwidth, c = "red")
vgswpw = plt.scatter(virginicasepalwidth, virginicapetalwidth, c = "blue")
plt.title("Sepal Width vs Petal Width")
plt.xlabel("Sepal Width")
plt.ylabel("Petal Width")
plt.legend([sswpw, vsswpw, vgswpw],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Sepal Width vs Petal Width")
plt.show()

sswsl = plt.scatter(setosasepalwidth, setosasepallength, c = "green")
vsswsl = plt.scatter(versicolorsepalwidth, versicolorsepallength, c = "red")
vgswsl = plt.scatter(virginicasepalwidth, virginicasepallength, c = "blue")
plt.title("Sepal Width vs Sepal Length")
plt.xlabel("Sepal Width")
plt.ylabel("Sepal Length")
plt.legend([sswsl, vsswsl, vgswsl],["Iris Setosa", "Iris Versicolor", "Iris Virginica"])
plt.savefig("Scatter Sepal Width vs Sepal Length")
plt.show()


"""
# Assigning a variable to represent colours for each class to use in plots if needed
# This is needed in single pyplot scatter graphs (below) but is not for Seaborne scatter plots
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
# suptitle is used to give a title to the whole plot. y is y coordinates, with 1 being the top of the plot. In some cases, y can be more than 1
# but I found the title would go beyond the scope fo the image
sns.pairplot(iris, hue = "class")
plt.suptitle("Iris Pairplot - Scatter and Distribution", y = 1)
plt.savefig("Pairplot - Scatter Plots and Distribution Plots")
plt.show()