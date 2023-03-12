# For general testing of anything...

# Input a number and stop when it is -1
#num = int(input("Enter a number "))
#while num != -1:
#    if (num %2 == 0):
#        print ("num is Even")
#    else:
#        print ("num is odd")
#    num = int(input("Enter a number "))
#print ("Finished")

#For assignment5 - day of the week
# Getting the day - NOTE Monday = 1, Tuesday = 2, etc
#import datetime
#now = datetime.datetime.now()
#print (now)
#today = datetime.datetime.today()
#print (today)
#from https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
#day = datetime.datetime.today().weekday()
#print (day) # use this one
#now, 2 options to know what to print out
#1 create a list ("monday", "Tuesday" etc)
# then match the day with the position in the list
#days = ["Monday", "Tuesday", "Wednesday", "thursday", "Friday", "Saturday", "Sunday"]
# print (days[1])
#Or if day number between 0 and 4 then its a weekday else is a weekend
#if day >=0 and day <5:
#    print (f"Today is a weekday, it's only {days[day]}")
#else:
#    print (f"Today is {days[day]} so its the weekend!!!")
#print (f"Today is: {days[day]}")

# This is very short, maybe add the actual day from the list as well - something like
#if day >=0 and day <5:
#    print (f"Today is a weekday - it's only {days[day]}")
#else:
#    print ("Its the weekend")

#Sample code for squareroot task
#https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/
#def squareRoot(n, l) :
# Assuming the sqrt of n as n only
#    x = n
    # To count the number of iterations
#    count = 0
#    while (1) :
#        count += 1
        # Calculate more closed x
#        root = 0.5 * (x + (n / x))
        # Check for closeness
#        if (abs(root - x) < l) :
#            break
        # Update root
#        x = root
#    return root
# Driver code
#if __name__ == "__main__" :
#    n = 327
#    l = 0.00001
#    print(squareRoot(n, l))
#root=0

'''def sqrt(num):
        tempnum = num
        while abs(tempnum - num * num) > tolerence_level:
#                print (abs(tempnum - num * num))
                num = (num+(tempnum/num))/2
                print (num)
                root = num
#                print (root)
        return root

# the actual code
#We can set these two if we want or just ignore them
num_of_iterations = 10
tolerence_level = .000001
num = int((input("Enter a number:  ")))
#Run the funtion with arguements if need be
root = sqrt(num)
#print (f"Answer = {newnumber}")
print (f"Root of {num} = {root} using Newtons method")
'''

import sys
FILENAME = sys.argv[1]
#Note this will be an exact search - i.e. lowercase e only
letter_to_find = "r"
with open(FILENAME, 'r') as f:
        string1 = f.read()
num_of_e = string1.count(letter_to_find)
print (f"The number of {letter_to_find}'s in {FILENAME} is {num_of_e}")

#https://www.geeksforgeeks.org/command-line-arguments-in-python/