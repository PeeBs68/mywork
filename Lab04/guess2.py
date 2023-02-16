# Script to prompt the user to guess a number and indicate if it is too high or too low

num = 30
guess = int(input("Enter a number "))
while (guess!=num):
    if guess > num:
        print("Too High")
    else:
# IF it's not too high then it must be too low so no need to check as such
        print("Too low")
    guess = int(input("Try again "))

# Or use num += 2
print (f"That's correct - the number is {guess}")
