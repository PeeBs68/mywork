# Script to generate 10 random numbers and print
# Then remove one number at a time, printing each new list

import random

counter = 0
numbers = []
top_range = 100

while counter <10:
    number = random.randint(1,top_range)
#    print(f"random Number generated is {number}")
    numbers.append(number)
    counter += 1
print (f" Queue is {numbers}")

for x in numbers:
    numbers.pop()
    print (x)
    print (f" Queue is now {numbers}")

