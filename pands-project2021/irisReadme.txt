Iris Dataset Readme

1. Introduction
2. Analysis of Variables
3. Histograms
4. Other Analysis
5. References
6. Changelog

			1. Introduction
The primary goal of this project was to examine and analyse the Iris dataset. This is a dataset containing information about 150 Iris flowers. The information consists of the length and width (in cm) of the petals and sepals as well
as the specific species of Iris. The 3 species were 'Setosa', 'Versicolor' and 'Virginica'. The main tasks involved in this project was to produce a text file summarising each variable as well as outputting histograms and scatter plots
of the variables. This readme will cover the process and specific codoing techniques involved in the basic analysis of the variables (mean, median etc.),  the plots used as well as any other analyses.

The Iris dataset contians data on 150 iris flowers of 3 different species. the length and width of the petals and sepals of each flower was measured. The Iris data was originally recorded by Edgar Anderson in 1935 and was used in data
analytics the following year by Ronal Fisher. Since then, it has become a broadly popular sample multivariate dataset in data analysis and data science.

Iris dataset origin: Anderson, E., 1935. The irises of the Gaspe Peninsula. Bull. Am. Iris Soc., 59, pp.2-5.
Iris dataset origin in data analytics: Fisher, R.A., 1936. The use of multiple measurements in taxonomic problems. Annals of eugenics, 7(2), pp.179-188.



			2. Analysis of Variables

Before any code on analyis of the dataset is written, my first task was to assign a python variables to anything that would be used as a variable in analysis. Before doing this, several packages had to be imported. The use of each package
is detailed below:

matplotlib.pyplot: for use in creating of any non-seaborn plots and for showing and saving all plots
pandas: for creating of dataframe and many functions related to selecting specific rows/columns
seaborn: for creating of pairplot
os: for removing a temporary file

Firstly, as the imported dataset did not have column headers, they were added using iris.columns (column names were taken from accompanying file iris.names). A variable was then assigned to each column. Each group of 50 flowers of each
species was assigned it's own variable and each column of each species was also made into its own variable. In order to have a file to output to, a file called iristemp.txt was made in write mode. The reasoning for this was to overwrite
any other file that was present if the program was being ran multiple times. This file is a temporary files as a function will later be used to remove some lines that were outputted by default. A title was inserted into the file  which was
then closed.
using the appropriate pandas function, a variable for the mean, median, min, max, first and third quantile and standard deviation was obtained for each variable in the dataset. The same was done for each variable of each species using the
variables made earlier. For the first and third quantiles, the same function was used, but with a different parameter of q = 25 or 75. As the measurements of the flowers are rounded to 2 decimal places, the analyses that do not involve
division (all except mean and standard dev) were also rounded to 2 decimal places. To keep the output looking clean, I also rounded the mean and standard deviation to 2 decimal places using .round(2).

In order to output this analysis to a text file, I used the print function with the parameter file = f with f being a with open function, opening the temporary file in append mode so as to not overwrite what was made earlier. Titles and
line skips were also added to make the data look cleaner. I found that the first line made by this function had a space in it and was out of line with the lines below. Using a sep = '' parameter fixed this issue.

In the printouts of the analyses, the datatype (e.g. dtype = float64) was added to the bottom of each printout. I deemed this info not useful to the analysis being done and in order to make the data cleaner, I used a for loop and a .readlines()
function to scan the lines in the document and if the line did not contain the word "dtype", it was written to a new text document called iris.txt. This allowed my to remove all the unneccesary lines and make the text output a lot cleaner.
Finally, the temporary text file was deleted using an os.remove function.

References for the methods used in this section are as follows:

Python variables:							https://www.w3schools.com/python/python_variables.asp
Python for loop:							https://www.w3schools.com/python/python_for_loops.asp
pandas.DataFrame and associated analysis (mean, median etc.): 		https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
pandas.DataFram.round:							https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html
Files handing in Python: 						https://www.w3schools.com/python/python_file_handling.asp
									https://www.w3schools.com/python/python_file_open.asp
os.remove:								https://www.w3schools.com/python/python_file_remove.asp
print to file:								https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file

			3. Plots

			4. Other Analysis

			5. References

Iris Dataset Origin: 							Anderson, E., 1935. The irises of the Gaspe Peninsula. Bull. Am. Iris Soc., 59, pp.2-5.
Iris Dataset Origin in data analysis: 					Fisher, R.A., 1936. The use of multiple measurements in taxonomic problems. Annals of eugenics, 7(2), pp.179-188.


Python variables:							https://www.w3schools.com/python/python_variables.asp
Python for loop:							https://www.w3schools.com/python/python_for_loops.asp
pandas.DataFrame and associated analysis (mean, median etc.): 		https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
pandas.DataFram.round:							https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html
Files handing in Python: 						https://www.w3schools.com/python/python_file_handling.asp
									https://www.w3schools.com/python/python_file_open.asp
os.remove:								https://www.w3schools.com/python/python_file_remove.asp
print to file:								https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file

			6. Changelog

21.03.21 	- Downloaded Iris CSV from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
           	- Wrote code for simple row / column viewing for preliminary study, code researched from https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
26.03.21	- Used pandas to convert to dataframe. Wrote code to get mean, median, min and max of all quantitative variables
03.04.21	- Wrote code to get first and third quartile of quantitative variables. Code researched at https://pandas.pydata.org/docs/index.html
		- Made printing of these simple analyses more readable by adding description and line break in printout
		- Assigned variable to filter by species and wrote code for mean of each species
17/04/21	- Added code for individual scatter plots and Pearson's correlations. These were commented out
		- Added code for a Seaborn pairplot containing scatter plots for all varibale relationships
		- Added code for numpy corr function, getting correlations of all variables accross whole dataset and by class
26/04/21	- Added more individual histograms and added an output to PNG
27/04/21	- Added Code for print to txt file
		- Added St Dev for analysis