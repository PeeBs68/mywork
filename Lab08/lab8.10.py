#Lab8.10 - saving

import numpy as np
import matplotlib.pyplot as plt

start_num = 20000
end_num = 80000
count_num = 10

age_low = 21
age_high = 65
age_count = count_num

#use 'normal' below for a normal distribution - for totally random use 'randint'
salaries=np.random.randint(start_num,end_num,count_num)

ages = np.random.randint(age_low, age_high, count_num)

x = np.array(range(1, 100))
y = x * x

plt.plot(x, y, color = 'g', label='x , ySquared')
plt.scatter(ages, salaries, label='ages v salaries')

plt.title("Salaries v Ages")
plt.xlabel("Ages")
plt.ylabel("Salaries")
plt.legend()

plt.savefig("prettier-plot.png")

plt.show()