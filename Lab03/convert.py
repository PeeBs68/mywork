# Script to take in avalue in dollars and cents and outputs the cents value
# Note, the input may be negative as well as positive

num1 = float(input("Enter the amount in dollars and cents: "))
# abs will give a positive number
abs_num = abs(num1)
# convert back to an int
final_num = int(abs_num*100)
print (f"The amount in cent is: {final_num}")
