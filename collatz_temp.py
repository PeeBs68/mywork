# collatz.py
# Author: Phelim Barry
# Purpose: input any positive integer, output the values after some calculations
# If the number is odd, multiple by 3 and add 1, if even, divide by 2. And so on until the number is 1

# define a list to hold the results
list_of_nums = []
# Input a number
number = int(input("Please enter a positive integer: "))

#Check that the number is indeed positive
while number < 1:
    number = int(input("Not a positive integer, enter another number: "))

# Add the input number to the list for later output
list_of_nums.append(number)

# While the number is not equal to 1 do the below until it is
while number != 1:
# Check if it is divisible by 2 with no remainder, if so then it is Even
    if (number % 2) == 0:
        number = (number/2)
        # Add the calculated number to the list for later output        
        list_of_nums.append(int(number))
    else: 
        # If not divisible by 2 then it must be odd
        number=(number*3)+1
        # Add the input number to the list for later output        
        list_of_nums.append(int(number))
        # Exit the loop and print the list of numbers formatted on one line with the brackets removed using the end= " " seperator

for num in list_of_nums:
    print (num, end = " ")

#Add a blank line just to make it visually better
print ("\n")

