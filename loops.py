answer = 7
isCorrect = False
print ("guess a number between 1 and 9")
while isCorrect == False:
    response = int(input("? "))
    if int(response) == answer:
        isCorrect = True
        print ('Yep, thats right, well done')
    else:
        print ('Nope, try again')