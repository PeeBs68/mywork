# Script to generate 10 random numbers (0-100) prints them and then prints the top three

import random

numbers = []
count=0
while count <10:
    number = random.randint(0,100)
    numbers.append(number)
    count+=1

sorted = sorted(numbers)
print (f"Ten random numbers are: {sorted}")

#for num in numbers:
#    print (num)
# get the average - as of time of writing we haven't done this bit so copied from the solution
# sum of the list divided by the lenght of the list
#average = float(sum(numbers))/len(numbers)
#print(f"The average is: {average}")

