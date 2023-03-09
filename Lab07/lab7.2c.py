#lab7.2c
import os.path

FILENAME = "counter9.txt"

def update_counter(newcounter):
    with open(FILENAME, 'wt') as f:
        counter = f.write(str(newcounter))
  
def read_number():
    with open(FILENAME, 'r') as f:
        counter = f.read()
        #counter = int(counter)
        return counter

#check that the file exists - assume in the current directory
if os.path.isfile(FILENAME):
    print ("The file exists!!!")
else:
    print ("The file is not there - I'll create one")
    f = open("counter9.txt", "x")
    counter = 0
    f.write(str(counter))

counter = read_number()
newcounter = int(counter)+1

update_counter(newcounter)

print (newcounter)