# For general testing of anything...

# Input a number and stop when it is -1
#num = int(input("Enter a number "))
#while num != -1:
#    if (num %2 == 0):
#        print ("num is Even")
#    else:
#        print ("num is odd")
#    num = int(input("Enter a number "))
#print ("Finished")

#For assignment5 - day of the week
# Getting the day - NOTE Monday = 1, Tuesday = 2, etc
#import datetime
#now = datetime.datetime.now()
#print (now)
#today = datetime.datetime.today()
#print (today)
#from https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
#day = datetime.datetime.today().weekday()
#print (day) # use this one
#now, 2 options to know what to print out
#1 create a list ("monday", "Tuesday" etc)
# then match the day with the position in the list
#days = ["Monday", "Tuesday", "Wednesday", "thursday", "Friday", "Saturday", "Sunday"]
# print (days[1])
#Or if day number between 0 and 4 then its a weekday else is a weekend
#if day >=0 and day <5:
#    print (f"Today is a weekday, it's only {days[day]}")
#else:
#    print (f"Today is {days[day]} so its the weekend!!!")
#print (f"Today is: {days[day]}")

# This is very short, maybe add the actual day from the list as well - something like
#if day >=0 and day <5:
#    print (f"Today is a weekday - it's only {days[day]}")
#else:
#    print ("Its the weekend")

#Sample code for squareroot task
#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#def squareRoot(n, l) :
# Assuming the sqrt of n as n only
#    x = n
    # To count the number of iterations
#    count = 0
#    while (1) :
#        count += 1
        # Calculate more closed x
#        root = 0.5 * (x + (n / x))
        # Check for closeness
#        if (abs(root - x) < l) :
#            break
        # Update root
#        x = root
#    return root
# Driver code
#if __name__ == "__main__" :
#    n = 327
#    l = 0.00001
#    print(squareRoot(n, l))
#root=0

'''def sqrt(num):
        tempnum = num
        while abs(tempnum - num * num) > tolerence_level:
#                print (abs(tempnum - num * num))
                num = (num+(tempnum/num))/2
                print (num)
                root = num
#                print (root)
        return root

# the actual code
#We can set these two if we want or just ignore them
num_of_iterations = 10
tolerence_level = .000001
num = int((input("Enter a number:  ")))
#Run the funtion with arguements if need be
root = sqrt(num)
#print (f"Answer = {newnumber}")
print (f"Root of {num} = {root} using Newtons method")
'''

'''
#Import the sys module
import sys

#get the filename from the command line
FILENAME = sys.argv[1]

#Note this will be an exact search - i.e. lowercase e only
letter_to_find = "r"
with open(FILENAME, 'r') as f:
        string1 = f.read()

#count the number of e's (or whatever the variable letter_to_fine is set to)
num_of_e = string1.count(letter_to_find)
print (f"The number of {letter_to_find}'s in {FILENAME} is {num_of_e}")

#https://www.geeksforgeeks.org/command-line-arguments-in-python/
'''

#Testing cleaning up accounts.py

# accounts.py
# Author: Phelim Barry
# Purpose: Part1 is to read in a 10 character account number and output the 
# number with the last 4 digits showing as input and the others replaced with XXXXXX
# Part2 is to do likewise with an account number (string) of any length

# Part1: read in the 10 digit account number as a string
'''acc_num = input("Please enter the 10 digit account number: ")
while len(acc_num) != 10:
    acc_num = input("Incorrect entry - please enter a 10 digit account nnumber: ")

#acc_num = input("Please enter the 10 digit account number: ")

# strip out and store the last 4 digits to be used in the result
last_4_digits = acc_num[6:]
# Note: This is a simplistic way of replacing the first 6 characters with an X. 
# Note: And only works if the account number is in fact 10 characters

# Replace the 1st 6 characters with 'X' and append to the last_4_digits and store in a new string
acc_num_masked = 6*"X"+last_4_digits
# Print the result
print (f"\nThe account number in masked format is {acc_num_masked}")

# Part2: read in the account number, which could be any length
# Note: if 4 or less characters are entered then the code will output the number without changes
acc_num2 = input("Please enter the account number (of any length): ")
# get the length of the account number
acc_num2_len = len(acc_num2)
# get the amount of the account number needing to be masked i.e. length-4 
first_part = (acc_num2_len-4)*"X"
# strip out the last 4 digits into a new variable to be used in the output
last_4_digits2 = acc_num2[-4:]
# Combine the part to be masked with the last 4 digits and print the result
acc_num2_masked = first_part+last_4_digits2
print (f"\nThe account number in masked format is {acc_num2_masked}")'''

#testing - cleaning up bank.py

# bank.py
# Author: Phelim Barry
# Purpose: Receive two inputs in cents, add them together and output the result in euros

# input section 
# input the 1st input as an integer
first_number = input("\nInput the first number in Cents: ")
while True:
        try:
                first_number = int(first_number)
        except ValueError: 
                print("Error - Your number must be an integer!") 
                first_number = input("\nAgain: ")
         
        else:
                print ("All good")
                second_number = input("\nSecond: ")

# Add a new line and output the input value in Cents 
print (f"\nThe first amount in Cent is: {first_number}")
# input the 2nd input as an integer
second_number = int(input("\nInput the second number in Cents: "))
# Add a new line and output the input value in Cents 
print (f"\nThe second amount in Cent is: {second_number}")

# calculations
# define a new variable, numtotal as an int, add the two numbers and divide the total by 100 to convert to euros
numtotal = int(first_number + second_number)/100

# output section
# Add a new line and print the output formatted to 2 decimal places
print (f"\nThe total in Euros and Cents is: €{numtotal:.2f}")
