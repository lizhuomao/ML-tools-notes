import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2, 1, 1) #两行两列 索引
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 4) #两行两列
plt.plot([0, 2], [0, 2])

plt.subplot(2, 3, 5) #两行两列
plt.plot([0, 3], [0, 3])

plt.subplot(2, 3, 6) #两行两列
plt.plot([0, 4], [0, 4])

plt.show()