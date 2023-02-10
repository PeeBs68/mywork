# Script to read in tow numbers, divide the first by the second and give the result as
# 1) the integer amount and 2) the remainder

num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))
print (num1, num2)
answer_whole = int(num1//num2)
answer_remainder = (num1 % num2)
print(f"{num1} divided by {num2} is {answer_whole} remainder {answer_remainder}")