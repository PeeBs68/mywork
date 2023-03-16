#Lab8.1

import numpy as np

salaries = []
start_num = 20000
end_num = 80000
count_num = 10

numbers=np.random.randint(start_num,end_num,count_num)
salaries = np.array(numbers)
print ("Numbers", numbers)
print ("Salaries", salaries)
