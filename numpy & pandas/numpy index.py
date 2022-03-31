import numpy as np

A = np.arange(3, 15).reshape((3, 4))
print(A)
print(A[2])
print(A[1][1])
print(A[2, 1])
print(A[:,1])
print(A[1, 1:3])
for row in A:
    print(row)
for column in A.T:
    print(column)
print(A.flatten()) #返回一个一位列表
for item in A.flat:#A.flat返回一个迭代器
    print(item)