import numpy as np
a = np.array([10, 20, 30, 40])
b = np.arange(4)

#基本运算
print(a, b)
c = a - b
print(c)
c = a + b
print(c)
c = b**2
print(c)
#三角函数
c = 10*np.sin(a)
print(c)
#判断
print(b < 3)

a = np.array([[1, 1],
              [0, 1]])
b = np.arange(4).reshape((2, 2))

c = a * b #逐个相乘
c_dot = np.dot(a, b) #矩阵乘法
c_dot_2 = a.dot(b) #等与上式

print(c)
print(c_dot)
print(c_dot_2)

a = np.random.random((2,4))#随机的2，4的矩阵
print(a)

np.sum(a)#求和
np.min(a)#最小值
np.max(a)#最大值

print(np.sum(a, axis=1)) #在行上求和 axis = 0:在列上求和


