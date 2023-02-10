# Script to read in in a float and outputs an int rounded down
# Need to import the math module

import math

float1 = float(input("Enter a float value: "))
final_num = math.floor(float1)
print(f"float value is: {float1} and floored value is: {final_num}")
print(type(final_num))

