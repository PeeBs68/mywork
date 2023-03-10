#lab7.2c
import os.path

FILENAME = "counter.txt"

def update_counter(newcounter):
    with open(FILENAME, 'wt') as f:
        counter = f.write(str(newcounter))
  
def read_number():
    with open(FILENAME, 'r') as f:
        counter = f.read()
        return counter

#check that the file exists - assume in the current directory
if os.path.isfile(FILENAME):
    print ("The file exists!!!")
    counter = read_number()
    counter = int(counter)
    newcounter = int(counter)+1
    update_counter(newcounter)
    print (f"Counter is now: {newcounter}")
else:
    print ("The file is not there - I'll create one and add a 1 for the first time running")
    f = open("counter.txt", "x")
    counter = 1
    f.write(str(counter))
    print (f"Counter is now: {counter}")
