#lab7.2 - storing a countrt in a file

#part a - read from the file

FILENAME = "count.txt"

def read_number():
    with open(FILENAME, 'r') as f:
        counter = f.read()
        return counter

def write_number():
    newnum = int(input("Enter a number to store : "))
    with open(FILENAME, 'wt') as f:
        counter = f.write(str(newnum))

#def update_counter():
#    with open(FILENAME, 'wt') as f:
#        counter = f.write(str(counter))
  
write_number()
counter = read_number()
#update_counter()
print (f"Counter = {counter}")

