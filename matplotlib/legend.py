import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2

plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=10.0, linestyle='--')

#设置坐标轴范围
plt.xlim((-1, 2))
plt.ylim((-2, 3))

#坐标轴描述
plt.xlabel('I am x')
plt.ylabel('I am y')

#更换坐标轴的ticks
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3,],
           [r'$really\ bad$', r'$bad', 'normal', 'good', r'$really\ good$'])

l1, = plt.plot(x, y2, label='up')
l2, = plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--', label='down')
plt.legend(handles=[l1, l2,], labels=['aaa', 'bbb'], loc='best') # loc='upper right'

plt.show()
