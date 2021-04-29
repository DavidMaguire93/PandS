Iris Dataset Readme

1. Introduction
2. Analysis of Variables
3. Histograms
4. Other Analysis
5. Conclusion
6. References
7. Changelog

			1. Introduction

The primary goal of this project was to examine and analyse the Iris dataset. This is a dataset containing information about 150 Iris flowers. The information consists of the length and width (in cm) of the petals and sepals as well
as the specific species of Iris. The 3 species were 'Setosa', 'Versicolor' and 'Virginica'. The main tasks involved in this project was to produce a text file summarising each variable as well as outputting histograms and scatter plots
of the variables. This readme will cover the process and specific codoing techniques involved in the basic analysis of the variables (mean, median etc.), the plots used as well as any other analyses.

The Iris dataset contains data on 150 iris flowers of 3 different species. the length and width of the petals and sepals of each flower was measured. The Iris data was originally recorded by Edgar Anderson in 1935 and was used in data
analytics the following year by Ronal Fisher. Since then, it has become a broadly popular multivariate ample dataset in data analysis and data science.

Iris dataset origin: Anderson, E., 1935. The irises of the Gaspe Peninsula. Bull. Am. Iris Soc., 59, pp.2-5.
Iris dataset origin in data analytics: Fisher, R.A., 1936. The use of multiple measurements in taxonomic problems. Annals of eugenics, 7(2), pp.179-188.

Before writing any code, I first had to research other examples of analysis of the iris dataset. A lot of research was done on kaggle.com, which had many examples of other people analysing the data. One such example which had a lot of
useful graphs was by Aditya D Bhat (https://www.kaggle.com/adityabhat24/iris-data-analysis-and-machine-learning-python). Another good example that I found on GitHub was this one by RitRa: https://github.com/RitRa/Project2018-iris.
Out of all these plots, the one that seemed most clear and effective to me was what I later learned to be a seaborn pairplot. This was also originally seen (although not exactly the same) in this youtube video:


kaggle iris dataset examples:						https://www.kaggle.com/arshid/iris-flower-dataset/code
Aditya D Bhat iris analysis:						https://www.kaggle.com/adityabhat24/iris-data-analysis-and-machine-learning-python
RitRa iris analysis:							https://github.com/RitRa/Project2018-iris
seaborne iris examples:							https://www.kaggle.com/noelano/seaborn-visualization-on-iris-data-set
seaborne graph examples:						https://medium.com/@neuralnets/data-visualization-with-python-and-seaborn-part-1-29c9478a8700
Working with Iris.csv video:						https://www.youtube.com/watch?v=HXi9cl5Aq5w

This research gave me a basis to work on. To break the project down into smaller parts, I settled on 6 smaller tasks that would make up the project. These were:

Variables: 			Using pandas to make an iris dataframe and assigning variables to anything I would need in the future
Basic Analysis: 		Getting mean, median etc. of all variables and species specific variables
Histograms: 			Making the histograms
Scatter Plots:			Making the scatterplots
Correlations: 			Getting pearsons correlation of variables
Save and Write functions: 	Write code for saving plots and writing analyses to text file

With that plan, I set out to start writing my code. At each step, I would review and possibly add to the previous step. At various points, I came up with more ideas to add e.g. kurtosis and skewness in the basic variables section was only
added at the end. I will discuss each step in the sections below.



			2. Analysis of Variables

Before any code on analysis of the dataset is written, my first task was to assign a python variable to anything that would be used as a variable in analysis. Before doing this, several packages had to be imported. The use of each package
is detailed below:

matplotlib.pyplot: for use in creating of any non-seaborn plots and for showing and saving all plots
pandas: for creating of dataframe and many functions related to selecting specific rows/columns
seaborn: for creating of pairplot
os: for removing a temporary file
numpy: for a Pearson's correlation that was later commented out

Firstly, as the imported dataset did not have column headers, these were added using iris.columns (column names were taken from accompanying file iris.names). A variable was then assigned to each column. Each group of 50 flowers of each
species was assigned its own variable and each column of each species was also made into its own variable. In order to have a file to output to, a file called iristemp.txt was made in write mode. The reasoning for this was to overwrite
any other file that was present if the program was being ran multiple times. This file is a temporary file as a function will later be used to remove some lines that were outputted by default. A title was inserted into the file  which was
then closed.

Before testing for mean, etc., a test for null values was performed to ensure that there were no null values. If null values were present, they may need to have been removed before testing for mean, medians etc. This was done using a pandas function
called DataFrame.isnull().values.any(). This returns a boolean with true indicating the presence of null values and false indicating no null values present.
Using the appropriate pandas function, a variable for the mean, median, min, max, first and third quantile, standard deviation, kurtosis and skewness was obtained for each variable in the dataset. The same was done for each variable of each species using the
variables made earlier. For the first and third quantiles, the same function was used, but with a different parameter of q = 25 or 75. As the measurements of the flowers are rounded to 2 decimal places, the analyses that do not involve
division (all except mean, standard dev, kurtosis and skewness) were also rounded to 2 decimal places. To keep the output looking clean, I also rounded the mean, standard deviation, kurtosis and skewness to 2 decimal places using .round(2).

In order to output this analysis to a text file, I used the print function with the parameter file = f with f being a with open function, opening the temporary file in append mode so as to not overwrite what was made earlier. Titles and
line skips were also added to make the data look cleaner. I found that the first line made by this function had a space in it and was out of line with the lines below. Using a sep = '' parameter fixed this issue.

In the printouts of the analyses, the datatype (e.g. dtype = float64) was added to the bottom of each printout. I deemed this info not useful to the analysis being done and in order to make the data cleaner, I used a for loop and a .readlines()
function to scan the lines in the document and if the line did not contain the word "dtype", it was written to a new text document called iris.txt. This allowed me to remove all the unneccesary lines and make the text output a lot cleaner.
Finally, the temporary text file was deleted using an os.remove function.

When examining the analysis, several things are worthy of note. When looking at the dataset as a whole (not by species), iris flowers tend to have larger sepals than petals and both petals and sepals are longer than they are wider. This can be seen
in the means and medians. When comparing means and medians, the most significant difference is in petal length's mean (3.77) vs median (4.4). This would suggest that the data is quite unsymmetrical (as evident in the histograms seen later and that data
point are far quite dispersed from the mean (as evident in the standard deviation of 1.76). Another interesting point on the full dataset is the difference between the 1st and 3rd quartiles in petal length (1.6 - 5.1) and width (0.3 - 1.8) when
compared to sepal length (5.1 - 6.4) and width (2.8 - 3.3). This large difference can be explained when each species is examined and compared.

When comparing the flowers species by species, the Versicolor and Virginica species are quite similar, with differences of between 0.5 - 1.5cm between all the averages of variables. The biggest difference between species comes when comparing the
Setosa species with the other 2. The Setosa species, on average,  has a shorter sepal by about 1-1.5cm as well as a wider sepal by about 0.5-0.75cm. Its petal, however, is shorter by 3-4cm and narrower by 1-1.75cm while only having a mean
petal width of only 0.24cm. This large difference in petal size between the Setosa Species and the other 2 species is most likely the reason for the large difference in quartiles in petal length and width seen above. Setosa petals are far smaller
than the other 2 species, while the sepals are shorter and wider. When looking at each individual species, not much sticks out in the analysis, except for possibly the high skewness and kurtosis of the Setosa petal width.


References for the methods used in this section are as follows:

Test for null values:							https://datatofish.com/check-nan-pandas-dataframe/
Python variables:							https://www.w3schools.com/python/python_variables.asp
Python for loop:							https://www.w3schools.com/python/python_for_loops.asp
pandas.DataFrame and associated analysis (mean, median etc.): 		https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
pandas.DataFrame.round:							https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html
Files handing in Python: 						https://www.w3schools.com/python/python_file_handling.asp
									https://www.w3schools.com/python/python_file_open.asp
os.remove:								https://www.w3schools.com/python/python_file_remove.asp
print to file:								https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file
numpy:									https://numpy.org/doc/stable/user/absolute_beginners.html





			3. Plots

The 2 primary plots use to visualize this data are histograms and scatter plots. For the histograms the pandas DataFrame.hist function was used. This created a histogram of each of the quantitative variables of the entire iris dataset. Some parameters
were used. These were to set the number of bins (bars of data) to 30 to convey the data better. The colour of the histogram was also changed to a shade of purple for aesthetic purposes to match the flowers. Matplotlib.pyplot functions were used to
modify, save and show the plots. pyplot.suptitle was used to give a title to the image which was needed as the image consisted of 4 different histograms (1 for each quantitative variable). If the usual pyplot.title were used, only the 4th plot in the
image would be given a title. Titles for each individual plot were automatically generated based on the column titles given previously. A histogram was made for the whole dataset as well as each species. The only difference in the parameters was the removal
of the parameter bins = 30. This was done because the default number of bins is 10 and as each species consists of 1/3 of the whole dataset, using 1/3rd of the bins to represent them made sense. The plots were saved using the pyplot.savefig function.
The default format is PNG but a parameter can be used to save in different formats if needed. pyplot.show was used to display the plots.

Scatterplot were used on each pair of variables. As there were 4 different variables, this give 12 different combinations of variables when order is taken into account. In creating these scatter plots, I wanted to use colour to differentiate the data
points by species. Originally, I used a for loop to iterate over the class column of the dataset and create an array with the colours green, red, and blue in the same order that the species were in. I called this array classcols. This could then be
used in the 'c =' parameter of pyplot.scatter to create different colours for each species in the plot. I found with this, however, that I could not add a legend to the plot to display what colour is what species. In order to add a legend, I had to
create 3 different sets of data with each set being each species and assign them a label. I used the naming sequence as follows:splpw : (s)etosa (p)etal (l)ength (p)etal (w)idth. This allowed me to create a different label for every iteration of variables
for each species. I used the 'c =' parameter to assign a different colour to each group of datasets. I used the plyplot .xlabel, .ylabel and .title to label both axes and add a title. I used the pyplot.legend with a list of the labels used and the accompanying
legend label (each species). Finally, I used the pyplot .savefig and .show as above.  Where I could label the axes, I included a (cm) clarification. I did this 12 times for each pair of variables. Upon review, this was a lot of code, and it's possible that a function could be made to cut down on the code length.
The function would most likely have a lot of parameters and I'm not sure on how much code this would save.

In researching for this project, I came across a plot in a youtube video that I thought would be quite useful and brings together all the scatter plots made above. This is called a pairplot and is made using seaborn. It creates a 4x4 matrix which contains
all pairs of variables as well as 4 distribution graphs of each individual variable. This was made using seaborn.pairplot with the parameter of hue = class. This automatically colours the plots based on the class column. It also automatically includes
a legend taken from the data in that column. Due to the effectiveness of this graph and the simplicity of the code, I would definitely use this as an alternative to the individual scatter plots created above. Also included in this plot is distribution
plots for each individual variable.

When analysing all of these plots, what sticks out is the difference in variables between the Setosa species and the other 2 species, Versicolor and Virginica. When looking either the seaborn pairplot or the individual scatter plots, the Versicolor
and Virginica data points appear to be almost grouped together with at least some overlap in all variables. This is in contract to the Setosa datapoints which have almost no overlap with the other 2 species. This would account for the spikes in
distributions that can be seen in the total dataset histograms. This is further seen in the distribution plots in the seaborn pairplot. When looking at the histograms and distribution graphs of the individual species, the data is quite normally distributed.
The only distribution that stands out is the distribution of the Setosa petal width. This was also seen when looking at the text based analysis of the individual species, with a high skewness and kurtosis.

References for the methods used in this section are as follows:

matplotlib.pyplot:							https://matplotlib.org/stable/tutorials/introductory/pyplot.html#:~:text=pyplot%20is%20a%20collection%20of,the%20plot%20with%20labels%2C%20etc.
									https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
pyplot.hist:								https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
pyplot.scatter:								https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
pyplot.legend:								https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
pyplot.savefig:								https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
seaborne:								https://seaborn.pydata.org/introduction.html
seaborne.pairplot							https://seaborn.pydata.org/generated/seaborn.pairplot.html
Working with Iris.csv video (not specific pairplot but gave me the idea):	https://www.youtube.com/watch?v=HXi9cl5Aq5w
Forum with info on color array using for loop:				https://stackoverflow.com/questions/43949395/looping-scatter-plot-colors

			



			4. Other Analysis

Other analyses done on the dataset was Pearson's correlation. Originally, individual Pearsons correlations were created using the numpy function .corrcoef. This would have had to be done with every pair of variables with order not mattering. This was later commented out
as the pandas function DataFrame.corr() was used instead. This outputs much cleaner looking matrix of correlations among all variables. This was done for the whole dataset as well as each species. This was printed to a text file in the same process as the means,
medians etc.

When looking at the correlations of the variables, the most interesting correlation is the negative correlation among sepal width and all other variables in the full dataset. When looking at the whole dataset, the wider the sepal width is, the shorter and narrower
the other variables are likely to be. This is primarily due to the measurements of the Setosa species. A quick look at the pairplot as well as the means will show that the Setosa species has the widest sepals but are much smaller in the other 3 variables. The wider
a sepal is in the full dataset, the more likely it is to be the Setosa species, which would most likely mean smaller measurements in the other 3 variables, hence the negative correlation. Aside from this negative correlation, other correlations are as would be
expected: flowers that are longer tend to be wider and flowers with larger sepals (with the exception of sepal width) have larger petals as well. When looking at the correlations of each individual species, the Setosa species sepal length and width are more
correlated than the other variables (0.75). The same can be said for Versicolor petal length and width (0.75) and Virginica petal length and sepal length (0.86).

References for the methods used in this section are as follows:

numpy.corrcoef:								https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html
pandas.DataFrame.corr							https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html



			5. Conclusion

When looking at the analysis as a whole. It is best to first realise that this dataset can be said to contain 2 succinct groups. These are the Setosa species being 1 group and the Versicolor and Virginica species being the other group. This can be seen by the mean,
median and scatter plots of the dataset and individual species datapoints. This difference in groups explains some anomalies when looking at the data as a whole such as the negative correlation between sepal width and the other variables as well as the high skewness, 
kurtosis and the asymmetrical distribution of the datapoints. Within the individual species datasets, on the whole, the data points seem to have quite normal distribution, with the possible exception of Setosa petal width.

In doing this project, I learned a lot of techniques that I predict will be very useful my career. I specifically found the seaborn pairplot to be very useful when analysing the data as all scatter plots and distribution graph can be seen on one image. I also found
the ease of pandas when making correlations and basic analyses very good. One technique that I had not done before was the scanning of the text file and writing to a new file in order to remove unnecessary lines. This is something that I will use a lot in the future I
would imagine. 

Things that I feel I could have put more research into are making functions to cut down on code. I feel like there is a lot of code that might be confusing to other people than myself. Using functions, possibly located in a different file, might make things simpler. I 
could also have researched into ways to create tables in the text file where all means, medians etc. among all species could be seen on one table, which would reduce the need to scroll up and down through the data when comparing analyses. Originally, I wanted to add 
more graphs and considered things such as 3d histograms and pie charts. I did not feel like these were appropriate given the number of variables. I also feel that, in the future, I need to make smaller, more frequent commits to GitHub. If something were to happen
that made it difficult to complete this project, it would have been difficult to gauge my work done at the beginning. Overall, I am happy with the analyses done and I think that it serves as a good starting point for further analytical projects.



			6. References

Iris Dataset Origin: 							Anderson, E., 1935. The irises of the Gaspe Peninsula. Bull. Am. Iris Soc., 59, pp.2-5.
Iris Dataset Origin in data analysis: 					Fisher, R.A., 1936. The use of multiple measurements in taxonomic problems. Annals of eugenics, 7(2), pp.179-188.


Python variables:							https://www.w3schools.com/python/python_variables.asp
Python for loop:							https://www.w3schools.com/python/python_for_loops.asp
pandas.DataFrame and associated analysis (mean, median etc.): 		https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
pandas.DataFram.round:							https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html
Files handing in Python: 						https://www.w3schools.com/python/python_file_handling.asp
									https://www.w3schools.com/python/python_file_open.asp
Test for null values:							https://datatofish.com/check-nan-pandas-dataframe/
os.remove:								https://www.w3schools.com/python/python_file_remove.asp
print to file:								https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file
numpy:									https://numpy.org/doc/stable/user/absolute_beginners.html
matplotlib.pyplot:							https://matplotlib.org/stable/tutorials/introductory/pyplot.html#:~:text=pyplot%20is%20a%20collection%20of,the%20plot%20with%20labels%2C%20etc.
									https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html
pyplot.hist:								https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
pyplot.scatter:								https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
pyplot.legend:								https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
pyplot.savefig:								https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html
seaborne:								https://seaborn.pydata.org/introduction.html
seaborne.pairplot							https://seaborn.pydata.org/generated/seaborn.pairplot.html
Working with Iris.csv video (not specific pairplot but gave me the idea):	https://www.youtube.com/watch?v=HXi9cl5Aq5w
Forum with info on color array using for loop:				https://stackoverflow.com/questions/43949395/looping-scatter-plot-colors

numpy.corrcoef:								https://numpy.org/doc/stable/reference/generated/numpy.corrcoef.html
pandas.DataFrame.corr							https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.corr.html
kaggle iris dataset examples:						https://www.kaggle.com/arshid/iris-flower-dataset/code
Aditya D Bhat iris analysis:						https://www.kaggle.com/adityabhat24/iris-data-analysis-and-machine-learning-python
RitRa iris analysis:							https://github.com/RitRa/Project2018-iris
seaborne iris examples:							https://www.kaggle.com/noelano/seaborn-visualization-on-iris-data-set
seaborne graph examples:						https://medium.com/@neuralnets/data-visualization-with-python-and-seaborn-part-1-29c9478a8700
Working with Iris.csv video:						https://www.youtube.com/watch?v=HXi9cl5Aq5w




			7. Changelog

21.03.21 	- Downloaded Iris CSV from http://archive.ics.uci.edu/ml/machine-learning-databases/iris/
           	- Wrote code for simple row / column viewing for preliminary study, code researched from https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
26.03.21	- Used pandas to convert to dataframe. Wrote code to get mean, median, min and max of all quantitative variables
03.04.21	- Wrote code to get first and third quartile of quantitative variables. Code researched at https://pandas.pydata.org/docs/index.html
		- Made printing of these simple analyses more readable by adding description and line break in printout
		- Assigned variable to filter by species and wrote code for mean of each species
17/04/21	- Added code for individual scatter plots and Pearson's correlations. These were commented out
		- Added code for a Seaborn pairplot containing scatter plots for all variable relationships
		- Added code for numpy corr function, getting correlations of all variables across whole dataset and by class
26/04/21	- Added more individual histograms and added an output to PNG
27/04/21	- Added Code for print to txt file
		- Added St Dev for analysis
29/04/21	- Added skewness and kurtosis to analyses
		- Added cm measurements to axes labels
		- Added test for null values
		- Added more comments and references