import matplotlib.pyplot as plt
import pandas as pd
#import seaborn as sns
#iris = sns.load_dataset("iris.data")
col_names =  ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]
iris = pd.read_csv('iris.data', sep= ",", names=col_names, header=None)

ratio = iris["Sepal Length"]/iris["Sepal Width"]
print (ratio)

for name, group in iris.groupby("Class"):
    plt.scatter(group.index, ratio[group.index], label=name)

plt.legend()
plt.show()