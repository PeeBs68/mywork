# Make the input a string (not int/float)

#Maybe use len for the 2nd part of the assignment to get the lenght of the string 
#so we know how many characters to X out

#Always use print(f...)

#Ipput and check the length
number1 = input("Enter a value: ")
length = (len(number1))
print (length)

# all the below references from the video - Fun with Numbers
# to get the last x characters use slicing - W3 schools python_strings_slicing
# to replace a string - W3 schools python_strings_modify

input = "edfr45ee89"
print(input[-2:]) #Means from the 2nd last digit to the end
print(input[0:4]) #Means from the 1st last digit to the 4th
print(input[2:5]) #Means from the 2nd last digit to the 5th

# Would need to capitalise before replacing
print (input)
print(input.replace("e", "X"))
print (input)