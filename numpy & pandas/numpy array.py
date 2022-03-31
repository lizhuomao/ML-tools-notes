import numpy as np

#合并
A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
C = np.vstack((A,B))
print(C) #vertical stack 向下合并
print(A.shape, C.shape)
D = np.hstack((A,B)) #左右合并
print(D)
print(A[np.newaxis, :].shape) #开辟一个新的维度
print(A[:, np.newaxis]) #将a变为纵向
A = A[:,np.newaxis]
B = B[:,np.newaxis]

C = np.concatenate((A, B, B, A), axis=0)
print(C.shape)
C = np.concatenate((A, B, B, A), axis=1) #多个array的合并 axis = 0纵向合并
print(C)

#分割
A = np.arange(12).reshape((3, 4))
print(A)
#等量分割
print(np.split(A, 2, axis=1)) #纵向切割
print(np.split(A, 3, axis=0)) #横向分割
#不等量分割
print(np.array_split(A, 3, axis=1))
print(np.vsplit(A, 3)) #横向
print(np.hsplit(A, 2)) #纵向