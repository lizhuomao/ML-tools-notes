import matplotlib.pyplot as plt
import numpy as np

#柱状图

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n) #均匀分布
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#66ccff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#9999ff', edgecolor='white')

for x, y in zip(X, Y1):
    #ha:horizontal alignment横向对齐 va纵向
    plt.text(x + 0.4, y + 0.05, '%.2f' % y, ha='center', va='bottom')
for x, y in zip(X, Y2):
    #ha:horizontal alignment横向对齐 va纵向
    plt.text(x + 0.4, -y - 0.05, '-%.2f' % y, ha='center', va='top')
#plt.xlim(-5, n)
plt.xticks(())
#plt.ylim(-1.25, 1.25)
plt.yticks(())

plt.show()