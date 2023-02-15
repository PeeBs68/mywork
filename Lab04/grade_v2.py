# script using a while loop to ask for an input and stop when it equals -1

int1=0
while int1 != -1:
    int1 = int(input("Enter a number: "))
    print ("Try again")
    continue
print (f"You enter it {int1}")
