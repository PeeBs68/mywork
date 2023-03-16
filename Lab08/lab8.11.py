#Lab8.11 - pie chart

import numpy as np
import matplotlib.pyplot as plt

#This is basic and just about works
'''counties = np.array(["Cork", "Wicklow", "Clare", "Limerick", "Kerry"])
count = np.array([1,2,3,4,5])

plt.pie(count, labels = counties)

plt.show()'''

#Real method used by Andrew - random number for choice of county
possible_counties = np.array(["Cork", "Wicklow", "Clare", "Limerick", "Kerry"])
#Generates a random sample from a given 1-D array
counties = np.random.choice(possible_counties, p=[0.1, 0.2, 0.3, 0.12, 0.28], size = (100))
unique, counts = np.unique(counties, return_counts = True)
plt.pie(counts, labels = unique)
plt.show()

#Useful Link
#https://www.geeksforgeeks.org/numpy-random-choice-in-python/