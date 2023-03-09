FILENAME = "count.txt"

def update_counter(newcounter):
    with open(FILENAME, 'wt') as f:
        counter = f.write(str(newcounter))
  
def read_number():
    with open(FILENAME, 'r') as f:
        counter = f.read()
        counter = int(counter)
        return counter

counter = read_number()
newcounter = counter+1

update_counter(newcounter)

print (newcounter)