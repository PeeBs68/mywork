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
import numpy as np
import matplotlib.pyplot as plt

FILENAME = "analysis.txt" 

#Write an into to the output file
with open(FILENAME, 'a') as f:
     for_header = f.write("This fle shows the output of the analysis performd on the iris data set\n\n")

# reading the CSV file and add column names
#From here - https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas
col_names =  ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
iris_csv = pd.read_csv('iris.data', sep= ",", names=col_names, header=None)

#print (headers1)

#used later on
headers1 = col_names[0:4]

#Using describe() for summary stats and specifying what to show
#https://www.statology.org/pandas-describe-only-mean-std/
print("New Stuff")
#qqq = iris_csv.describe()
#print (qqq)
www = iris_csv.describe().loc[['min', 'max', 'mean', 'std']]
print (f"www = : {www}")
       
#To show summary stats using describe() for each Class - maybe call this for each iris type
#with open(FILENAME, 'a') as f:
#     for_header = f.write(str(iris_csv.groupby("Class").describe()))

#create a function to gather summary stats on the data set and write to the output file
def summary_stats():
     num_rows = len(iris_csv)
     num_cols = len(iris_csv.columns)
     print (num_rows, num_cols)
     with open(FILENAME, 'a') as f:
          for_summary = f.write(f"The iris data set contains {num_rows} rows and {num_cols} columns of data to analyse\n\n")

#call the summary_stats function
summary_stats()
     
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
      #use headers1 list
      x = 0
      while x < 4:
        print (headers1[x])
        Total = iris_csv[headers1[x]].sum()
        Mean = iris_csv[headers1[x]].mean()
        Max = iris_csv[headers1[x]].max()
        Min = iris_csv[headers1[x]].min()
        x = x+1
        print(f"Min: {Min}")
        return (headers1[x],Total, Mean, Max, Min)

for Class in unique_class:
        print (Class)
        x = 0
        with open(FILENAME, 'a') as f: #'a' for append
            headers1[x],Total, Mean, Max, Min = summary_data(Class)
            string1 = f.write(f"Iris Type : {Class}\n")
            string1 = f.write(f"Attribute : {headers1[x]}, Min : {Min}, Max : {Max}, Sum : {Total}, Mean : {Mean}\n")

#Testing - to be deleted
for Class in unique_class:
        print (Class)
        x = 0
        with open(FILENAME, 'a') as f: #'a' for append
            headers1[x],Total, Mean, Max, Min = summary_data(Class)
            print (headers1)
            print(f"headers1-0: {headers1[0]}")
            print(f"headers1-1: {headers1[1]}")
            print(f"headers1-2: {headers1[2]}")
            print(f"headers1-3: {headers1[3]}")
            string1 = f.write(f"Iris Type : {Class}\n")
            string1 = f.write(f"Attribute : {headers1[0]}, Min : {Min}, Max : {Max}, Sum : {Total}, Mean : {Mean}\n")
            string1 = f.write(f"Attribute : {headers1[1]}, Min : {Min}, Max : {Max}, Sum : {Total}, Mean : {Mean}\n")

#Histogram
sepal_l, sepal_w = [], []
for x in iris_csv['Sepal Length']:
    sepal_l.append(x)
sepal_l.sort()
print (sepal_l)
print (sepal_w)
plt.hist(sepal_l)
plt.show()


def plotting(header):
     for y in iris_csv[header]:
#        print (iris_csv[header])
        newlist.append(y)
        print (newlist)
#        print ("Hi")
#        plt.hist(sepal_l)
#        plt.show()
        return newlist

newlist = []
for header in headers1:
#     newlist = []
     header = plotting(header)
#print (newlist)


iris_setosa=iris_csv.loc[iris_csv["Class"]=="Iris-setosa"]
iris_virginica=iris_csv.loc[iris_csv["Class"]=="Iris-virginica"]
iris_versicolor=iris_csv.loc[iris_csv["Class"]=="Iris-versicolor"]

print (iris_setosa)

xxx= iris_setosa.describe().loc[['min', 'max', 'mean', 'std']]
print (f"www = : {www}")

ise_min = iris_setosa['Sepal Length'].min()
print(f"Min : {ise_min}")

unique_class = iris_csv.Class.unique()
print (unique_class)

def write_data():
    xxx = iris_setosa.describe().loc[['min', 'max', 'mean', 'std']]
    yyy = iris_versicolor.describe().loc[['min', 'max', 'mean', 'std']]
    zzz = iris_virginica.describe().loc[['min', 'max', 'mean', 'std']]
    print (unique_class[0])
    print (xxx)
    with open(FILENAME, 'a') as f:
         string1 = f.write(str(Class))
         string2 = f.write(str(xxx))
    print (unique_class[1])
    print (yyy)
    with open(FILENAME, 'a') as f:
         string1 = f.write(str(Class))
         string2 = f.write(str(yyy))
    print (unique_class[2])
    print (zzz)
    with open(FILENAME, 'a') as f:
         string1 = f.write(str(Class))
         string2 = f.write(str(zzz))

         
#         min = Class['Sepal Length'].min()
#        with open(FILENAME, 'wt') as f:
#            string1 = f.write(str(Class))

write_data()

#For some additional stats
'''print ("Newest STuff")
unique_class = iris_csv.Class.unique()
print (unique_class)
print (iris_csv.Class)
#print (iris_csv.Class())
for x in iris_csv.Class:
#    print(iris_csv['Class'].min)
    Min = unique_class.min()
    print (Min)
for x in csvFile['Sepal L']:
    print(x)'''


plt.clf()
for x in iris_csv.Class:
     plt.scatter(iris_csv['Sepal Length'], iris_csv['Sepal Width'])
#plt.title('Sepal Length | Sepal Width')
plt.xlabel('Sepal length [cm]')
plt.ylabel('Sepal Width [cm]')
plt.legend()
#plt.show()
#plt.savefig("Sepal Length | Sepal Width Scatterplot.png")
#with open(FILENAME, 'a') as f:
#     for_header = f.write("Scatter Plot saved as Sepal Length | Sepal Width Scatterplot.png\n")

#plt.clf()
    
#plt.savefig("Petal Length | Petal Width Scatterplot.png")
#with open(FILENAME, 'a') as f:
#     for_header = f.write("Scatter Plot saved as Petal Length | Petal Width Scatterplot.png\n\n")
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


#Everything below here is just for testing for now
'''

#Prnting Mean, Max, Min, Sun
#Total = iris_csv['Sepal L'].sum()
#Mean = iris_csv['Sepal L'].mean()

#playing with different print options
for x in iris_csv['Sepal L']:
    print(x)

for x in iris_csv.columns:
    print(iris_csv[x].unique())

#Prnting Mean, Max, Min, Sun
Total = iris_csv['Sepal L'].sum()
Mean = iris_csv['Sepal L'].mean()
Max = iris_csv['Sepal L'].max()
Min = iris_csv['Sepal L'].min()
print(f"Min : {Min}, Max : {Max}, Sum : {Total}, Mean : {Mean}")


#Create a function for appending results
def append_results():
     with open(FILENAME, 'a') as f:
          string1 = f.write("Some results...\n")

#stripping data from individual columns
unique_class = str(iris_csv.Class.unique())
class1 = iris_csv.Class[0]
class2 = iris_csv.Class[1]
class3 = iris_csv.Class[2]
print (class1)

print (unique_class)
with open(FILENAME, 'a') as f: #'a' for append
        string1 = f.write(f"Iris Types : {unique_class}\n")
        string1 = f.write(f"Min : {Min}, Max : {Max}, Sum : {Total}, Mean : {Mean}")

#Call the functions
#append_results()

#Or do the append normally
#with open(FILENAME, 'a') as f: #'a' for append
#        string1 = f.write("Some results...\n")'''