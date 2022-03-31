import numpy as np

A = np.arange(2, 14).reshape(3,4)

print(A)
print(np.argmin(A)) #最小值的索引
print(np.mean(A)) #平均值
print(A.mean()) #同上
print(np.average(A)) #同上
print(np.median(A)) #中位数
print(np.cumsum(A)) #累加 斐波那契数列
print(np.diff(A)) #后项与前项的差
print(np.nonzero(A)) #找出非零的数，输出索引
A = np.arange(14, 2, -1).reshape((3, 4))
print(np.sort(A))#逐行排序
print(np.transpose(A)) #矩阵的转置
print(A.T) #矩阵的转置
print(np.clip(A, 5, 9)) #过滤小于5和大于9的值
