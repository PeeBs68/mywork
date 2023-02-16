# Script to prompt the user to guess a number

num = 30
guess = int(input("Enter a number "))
while (guess!=num):
    guess = int(input("Wrong, try again "))

# Or use num += 2
print (f"That's correct - the number is {guess}")
