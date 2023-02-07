# sample for taking in input and printing to the console

# Adding int takes the input as an integer rather than string
age = int(input("What is your age? "))
#age = age/100
# print(age)
# Preferable way to print
ageoutput = "Your age is {} years"
print(ageoutput.format(age))

# print ("Your age is", age) this would also work but use the above format

myname = input("What is your name? ")
#age = age/100
print(myname)
# Preferable way to print
#ageoutput = "Your age is {} years"
#print(ageoutput.format(age))