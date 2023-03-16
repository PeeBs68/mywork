#Lab8.5 - plotting

import numpy as np
import matplotlib.pyplot as plt

#plot y = x squared

x = np.array(range(1, 100))
y = x * x

plt.plot(x, y)
plt.show()
