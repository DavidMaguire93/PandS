21.03.21 	- Downloaded Iris CSV from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
           	- Wrote code for simple row / column viewing for preliminary study, code researched from https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
26.03.21	- Used pandas to convert to dataframe. Wrote code to get mean, median, min and max of all quantitative variables
03.04.21	- Wrote code to get first and third quartile of quantitative variables. Code researched at https://pandas.pydata.org/docs/index.html
		- Made printing of these simple analyses more readable by adding description and line break in printout
		- Assigned variable to filter by species and wrote code for mean of each species
17/04/21	- Added code for individual scatter plots and Pearson's correlations. These were commented out
		- Added code for a Seaborn pairplot containing scatter plots for all varibale relationships
		- Added code for numpy corr function, getting correlations of all variables accross whole dataset and by class
Notes / Plans

I am just leaving this here is a 'project plan' and outline my thoughts and goals that I can come back to. I may leave this section or delete it before the final submission.

Premilinary analysis of the data data set will be standard analysis: mean, median, min, max, range, 25% and 75% quartile based on the different measurements of the different species.
Further analysis will involve getting corellations of the variables, possibly through different means of correlation.
I would also like to get ratio variables (sepal length: petal width etc.) and correlate those by species.

Visually, I would like to use a variety of bar charts, histograms, pie charts and some 3d charts that will have to be researched. While some may not end up being used, it would still be good to learn how to use them.
I imagine that I will end up using a compination of matplotlib and seaborn to get the desired charts and diagrams.

At some point, when my code gets bigger, I will create another program for a lot of my analytical functions and use if __Name__ = __Main__ to test the functions