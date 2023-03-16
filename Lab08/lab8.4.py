#Lab8.4

import numpy as np

salaries = []
start_num = 20000
end_num = 80000
count_num = 10

#np.random.seed(1)
numbers=np.random.randint(start_num,end_num,count_num)
new_numbers=numbers * 1.05
#Could also have used floor() here to get rid of the decimal
new_numbers = new_numbers.astype(int)
print ("Numbers", numbers)
print ("Numbers", new_numbers)