import matplotlib.pyplot as plt
import numpy as np

# 1 row, 2 colums, first plot
plt.subplot(1, 2, 1)
x = np.random.normal(0.0, 1.0, 10000)
plt.hist(x)

# 1 row, 2 colums, second plot
plt.subplot(1, 2, 2)
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x)

plt.show()