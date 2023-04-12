# es.py
# Author: Phelim Barry
# Purpose: Write a program that reads in a text file and outputs the number of e's it contains

#Import the sys module
import sys

#get the filename from the command line - argv[1] contains the 1st arguement passed to the script (i.e. filename)
FILENAME = sys.argv[1]

#define the letter we want to find and count
letter_to_find = "e"

#Open the file in read mode and read in the contents as a string
with open(FILENAME, 'r') as f:
        string1 = f.read()

#var1=0
#with open(FILENAME) as r:
#    for line in r:
#        var1 = var1+line.count(letter_to_find)

#print (f"The number of {letter_to_find}'s in {FILENAME} is {var1}")

#count the number of e's (or whatever the variable letter_to_find is set to) and print the result
var1 = string1.count(letter_to_find)
print (f"The number of {letter_to_find}'s in {FILENAME} is {var1}")

#https://www.geeksforgeeks.org/command-line-arguments-in-python/ - for the command line arguements
# use this link - https://www.w3schools.com/python/python_file_open.asp
# this will also be useful - https://realpython.com/read-write-files-python/