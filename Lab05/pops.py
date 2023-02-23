# Script to generate 10 random numbers and print
# Then remove one number at a time, printing each new list

import random

counter = 0
numbers = []
top_range = 100

while counter <10:
    number = random.randint(1,top_range)
    numbers.append(number)
    counter += 1
print (f"Queue is {numbers}")


while (len(numbers) > 0):
    num_before_pop = numbers[0]
    numbers.pop(0)
    print (f"Current number is {num_before_pop} and the queue is now {numbers}")
print ("Queue is now empty")