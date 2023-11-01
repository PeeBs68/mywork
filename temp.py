'''a = 1
b = 2
list = (a, b)
print (list)
a = 3
list.append(a)
print (list)
'''

'''
#Import required modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# reading the CSV file and add column names
# Information on how to add column names during the import taken from https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas
col_names =  ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
iris_csv = pd.read_csv(data/'iris.data', sep= ",", names=col_names, header=None)'''

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng()
n, p = 1, .5  # number of trials, probability of each trial
s = rng.binomial(n, p, 10)
print (s)

