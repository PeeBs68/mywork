# Script to generate a random number
# Need to import the random module first

import random

number1 = random.randint(1,10)
print(f"random Number generated is {number1}")

#Part2
start = int(input("enter number range start: "))
end = int(input("enter number range end: "))
number2 = random.randint(start,end)
print(f"random Number generated is {number2}")