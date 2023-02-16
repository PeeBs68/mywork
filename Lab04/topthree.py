# Script to generate 10 random numbers (0-100) prints them and then prints the top three

import random

numbers = []
count=0
while count <10:
    number = random.randint(0,100)
    numbers.append(number)
    count+=1

# Sorts low to high
sorted = sorted(numbers)
topthree = sorted[7:10]
print (f"Ten random numbers are: {numbers}")
print (f"Ten random numbers sorted are: {sorted}")
print (f"The top three are: {topthree}")

# Alternative method using FOR loop

print ("\nNew Stuff")   
numbers = []
for i in range (0, 10):
    number = random.randint(0,100)
    numbers.append(number)
newlist=numbers.copy()
newlist.sort(reverse = True)
topthree = newlist[0:3]
print (f"Ten new random numbers are: {numbers}")
print (f"Ten new random numbers sorted are: {newlist}")
print (f"The new top three are: {topthree}")