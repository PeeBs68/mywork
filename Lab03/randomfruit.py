# Script to generate a random 

import random

# Using a list - square brackets
fruits = ["apple", "banana", "melon", "strawberry", "orange"]
index = random.randint(0,len(fruits)-1)
fruit = fruits[index]
print (f"A random fruit is: {fruit}")

# Using a tuple - round brackets
fruits2 = ("apple", "banana", "melon", "strawberry", "orange")
index = random.randint(0,len(fruits2)-1)
fruit2 = fruits2[index]

print (f"A random fruit is: {fruit2}")