import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    #the height function
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x**2-y**2)

#等高线图

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X,Y=np.meshgrid(x, y); #将数据绑定为网格

# 等高线颜色设置 x, y, z轴, 8种颜色 透明度 对应颜色
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)

#画等高线 8段 颜色 线宽
C = plt.contour(X, Y, f(X, Y), 16, colors='black', linewidths=.5)

#数字描述 inline=True放在线里面
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
plt.show()

