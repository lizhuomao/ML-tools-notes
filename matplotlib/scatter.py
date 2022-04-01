import matplotlib.pyplot as plt
import numpy as np

#散点图

n = 1024
X = np.random.normal(0, 1, n)#正态分布
Y = np.random.normal(0, 1, n)
T = np.arctan2(X, Y)

plt.figure()
plt.scatter(X, Y, s=75, c=T, alpha=0.5)

plt.xlim((-1.5, 1.5))
plt.ylim((-1.5, 1.5))
plt.xticks(())
plt.yticks(())

plt.figure()
plt.scatter(np.arange(5), np.arange(5))

plt.show()