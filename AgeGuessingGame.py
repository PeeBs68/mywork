b = []
print ('What is Sarahs age?')
isCorrect = False
while isCorrect == False:
    response = int(input("?"))
    b.append(response)
    if int(response) == 21:
        isCorrect = True
        print ('Yep, thats right, well done')
        print ('You tried...' + str(b))
        print (f"You tried...{b}")
    else:
        print ('Nope, try again')