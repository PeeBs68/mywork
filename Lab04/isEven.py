# Script to check if a number is even or not

number = int(input("Enter a nnumber "))

if (number % 2) == 0:
    evenodd = "Even"
else:
    evenodd = "Odd"
print (f"{number} is an {evenodd} number")