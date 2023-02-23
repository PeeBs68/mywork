# For general playing around

# Andrews solution to lab 5.2 using pop
import random
queue = []
numberOfNumbers=10
rangeTo=100

for n in range (0, numberOfNumbers):
    queue.append(random.randint(0,rangeTo))
    
print (f"queue is {queue}")

while len(queue) != 0:
    currentNumber = queue.pop(0)
    print (f"current num is {currentNumber} and the queue is {queue}")
print ("the queue is now empty")

