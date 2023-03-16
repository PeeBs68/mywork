#Lab8.6 - histogram

import numpy as np
import matplotlib.pyplot as plt

salaries = []
start_num = 20000
end_num = 80000
count_num = 1000

#use 'normal' below for a normal distribution - for totally random use 'randint'
salaries=np.random.normal(start_num,end_num,count_num)

plt.hist(salaries)
plt.show()