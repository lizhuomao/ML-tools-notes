import numpy as np
#numpy 基于矩阵运算
array = np.array([[1, 2, 3],
                  [2, 3, 4]])
print(array)
print('number of dim:', array.ndim) #维数
print('shape:', array.shape) #形状
print('size:', array.size) #元素数量

#创建数组

a = np.array([2, 3, 4], dtype=np.float32)#定义type
print(a.dtype)

a = np.array([[2, 3, 4],
             [2, 2, 2]])
print(a.shape)

a = np.zeros((3, 4)) #生成全部为0
print(a)

a = np.ones((3, 4)) #生成全部为1
print(a)
a = np.empty((3, 4)) #生成完全为空
print(a)

a = np.arange(10, 20, 2) #起始，终止，步长
print(a)

a = np.arange(12).reshape((3, 4)) #重定义形状
print(a)

a = np.linspace(1, 10, 20).reshape((4, 5)) #起始，终止，分段
print(a)