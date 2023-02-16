
#While loops are counter controlled or sentinel controlled
#Countger is for example "while count < 10"
#Sentinel is for example "while input val != 'Hi"
b = []
number = int(input("?"))
#isCorrect = False
#print (number)
while number != 10:
   b.append(number)
   number += 1
#   print (number)
print (*b)
#   if int(number) == 1:
#        isCorrect = True
#        print ('Yep, thats right, well done')
#        print ('You tried...' + str(b))
#        print (f"You tried...{b}")
#    elif (number % 2) == 0:
#        newnum=(number/2)
#    else:
#        newnum=(number*3)+1

# Use this to print the list nicely
# taken from https://stackoverflow.com/questions/62901226/howto-print-list-without-brackets-and-comma-python
#list1 = [1,2,3,4,5,6,7,8,9,10] 
#print(*list1, sep = ', ')