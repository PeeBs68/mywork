b = []
number = int(input("?"))
isCorrect = False
while isCorrect == False:
#    number = int(input("?"))
    b.append(number)
    if int(number) == 1:
        isCorrect = True
#        print ('Yep, thats right, well done')
#        print ('You tried...' + str(b))
        print (f"You tried...{b}")
    elif (number % 2) == 0:
        newnum=(number/2)
    else:
        newnum=(number*3)+1

