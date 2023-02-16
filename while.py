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

# Use this to print the list nicely
#list1 = [1,2,3,4,5,6,7,8,9,10] 
#print(*list1, sep = ', ')