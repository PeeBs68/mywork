# Script to read numbers until the user enters a 0. Then print the average

numbers = []
num = int(input("Please enter a number "))
while num != 0:
    numbers.append(num)
    num = int(input("Please enter another number "))
for num in numbers:
    print (num)
# get the average - as of time of writing we haven't done this bit so copied from the solution
# sum of the list divided by the lenght of the list
average = float(sum(numbers))/len(numbers)
print(f"The average is: {average}")