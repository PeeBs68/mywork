#Temp file for working on stuff related to the project

#Project Plan: maybe like this???
#Goals - It might help to suppose that your manager has asked you to investigate the data set, 
#with a view to explaining it to your colleagues. Imagine that you are to give a presentation on 
#the data set in a few weeks’ time, where you explain what investigating a data set entails and 
#how Python can be used to do it
#Objectives - 
#Tasks - ???
#Probably need to look at due dates etc also

'''Usefull Links
#https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
[1] Python Software Foundation. Welcome to python.org. https://www.python.org/. 
[3] UC Irvine Machine Learning Repository. Iris data set. https://archive.ics.uci.edu/ml/datasets/iris
UCI Machine Learning 
Repository: Iris Data Set http://archive.ics.uci.edu/ml/datasets/Iris
'''

'''
#Task suggestions
1. Research the data set online and write a summary about it in your README.
2. Download the data set and add it to your repository.
3. Write a program called analysis.py that:
1. Outputs a summary of each variable to a single text file, use statistical analysis - mean, max, min etc.
2. Saves a histogram of each variable to png files, and
3. Outputs a scatter plot of each pair of variables.
4. Performs any other analysis you think is appropriate
'''

''' Useful link here
https://www.youtube.com/watch?v=vmEHCJofslg&start=1068
'''

'''data file attributes
Attribute Information:

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
-- Iris Setosa
-- Iris Versicolour
-- Iris Virginica'''


import pandas as pd
 
# reading the CSV file
csvFile = pd.read_csv('iris.data', sep= ",", header=None)
headers =  ["Sepal L", "Sepal W", "Petal L", "Petal W", "Class"]
csvFile.columns = headers
#csvFile.columns = ["Sequence", "Start", "End", "Coverage", "ddd"]
#csvFile2 = pd.DataFrame(csvFile, index = ["day1", "day2", "day3", "day4", "day5"])
# displaying the contents of the CSV file
print(csvFile)
print(csvFile.to_string())
print (csvFile.loc[148])
#Cov = pd.read_csv("path/to/file.txt", 
#                  sep='\t', 
#                  names=["Sequence", "Start", "End", "Coverage"])