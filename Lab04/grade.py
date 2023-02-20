# Script to calculate grades

import math

# Extra bit to deal with percentages
val1 = float(input("Enter the grade "))
# Remember round will only round to the nearest EVEN number if the percentage value == .5!!! 
# It works in this case but be careful using it
value = round(val1)

if value > 100 or value <0:
    print ("Invalid grade")
elif value <40:
    print ("You failed")
elif value >=40 and value <50:
    print ("You got a Pass")
elif value >=50 and value <60:
    print ("You got a Merit 2")
elif value >=60 and value <70:
    print ("You got a Merit 1")
else:
    print ("You got a Distinction")
