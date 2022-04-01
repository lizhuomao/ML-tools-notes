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
           [r'$really\ bad$', r'$bad\alpha$', 'normal', 'good', r'$really\ good$'])
#r'$ $' 特殊表达

#gca = 'get current axis'
#设置边框
ax = plt.gca()
ax.spines['right'].set_color('none') #消除右边框
ax.spines['top'].set_color('none')

#x轴与y轴进行绑定
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', -1)) #x轴绑定在y轴-1的位置

ax.spines['bottom'].set_position(('data', 0))  #参数‘outward’, 'axes'
ax.spines['left'].set_position(('data', 0))

plt.show()