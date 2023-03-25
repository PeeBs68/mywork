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
FILENAME = "analysis.txt" 
# reading the CSV file
iris_csv = pd.read_csv('iris.data', sep= ",", header=None)
headers =  ["Sepal L", "Sepal W", "Petal L", "Petal W", "Class"]
iris_csv.columns = headers


unique_class = iris_csv.Class.unique()
#class1 = iris_csv.Class[0]
#class2 = iris_csv.Class[1]
#class3 = iris_csv.Class[2]
#print (class1)
#Total = iris_csv['Sepal L'].sum()
#Mean = iris_csv['Sepal L'].mean()
#Max = iris_csv['Sepal L'].max()
#Min = iris_csv['Sepal L'].min()
#print (unique_class)

def summary_data(Class):
      #need to loop through each attribute here
      Total = iris_csv['Sepal L'].sum()
      Mean = iris_csv['Sepal L'].mean()
      Max = iris_csv['Sepal L'].max()
      Min = iris_csv['Sepal L'].min()
      #print(Min)
      return (Total, Mean, Max, Min)

for Class in unique_class:
        print (Class)
        with open(FILENAME, 'a') as f: #'a' for append
            Total, Mean, Max, Min = summary_data(Class)
            string1 = f.write(f"Iris Type : {Class}\n")
            string1 = f.write(f"Min : {Min}, Max : {Max}, Sum : {Total}, Mean : {Mean}\n")
# displaying the contents of the CSV file
'''print(csvFile)
print(csvFile.to_string())
print (csvFile.loc[148])
print (csvFile.columns)

for x in csvFile['Sepal L']:
    print(x)
'''
#for x in csvFile.columns:
#    print(csvFile[x].unique())

#csvFile.nunique()
#unique_class = csvFile.Class.unique()
#print (unique_class)

#print(csvFile.Class.unique())
#print(csvFile.unique(csvFile['Class']))
'''
Total = csvFile['Sepal L'].sum()
print(f"Total : {Total}")

Mean = csvFile['Sepal L'].mean()
print(f"Mean : {Mean}")

Max = csvFile['Sepal L'].max()
print(f"Max : {Max}")

Min = csvFile['Sepal L'].min()
print(f"Min : {Min}")
'''