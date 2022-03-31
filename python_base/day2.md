# 元组 列表

```python
# truple list
a_truple = (1, 2, 3)
an_tuple = 2, 4, 6
a_list = [1, 2, 3]

for i in range(len(a_list)):
    print(a_list[i])
a = [1, 2, 3, 4, 5, 6, 7]
a.append(0) #在a后追加0
a.insert(1, 0)#在1的位置添加0
a.remove(2) #删除第一个2的值
print(a[-1]) #索引-1是最后一位
print(a[0:3])#从0到第2位的值
print(a[5:])#从第5位到最后一位
print(a[-3:])
print(a.index(2))#返回2的索引
print(a.count(4))#返回4的数量
a.sort()#排序
a.sort(reverse = True)#从大到小排序
print(a)
multi_dim_a = [[1, 2, 3],
               [2, 3, 4],
               [3, 4, 5]]
print(multi_dim_a[2][2])

```

# 字典

```python
d = {'apple': 1, 'pear': 2, 'orange': 3}
d2 = {1 : 'a', 'c': 'b'}
print(d['apple'])
del d['pear'] #删除元素
d = {'apple':[1, 2, 3], 'pear':{1 : 3, 3 : 'a'}}#复合
print(d['pear'][3])

```

# 载入模块

```python
import time
import time as t
from time import time, loacltime
from time import *
print(time.loacltime())
print(t.loacltime())
print(localtime())
print(gettime())
```

## 自定义模块

```python
#m1.py
def printdata(data):
    print(date)
#p1.py 与m1.py处于同一目录下 或将m1.py置于site-packages(默认外部模块)目录下
import m1
m1.printdata('i')
```

# 错误处理

  ```python
try:
	file = open('eeee', 'r+')
except Exception as e:
    print('there is no file named as eeee')
    response = input('do you want to create a new file')
    if response == 'y':
        file = open('eeee', 'w')
    else:
        pass
else: 
    file.write('ssss')
file.close()
    
  ```

# zip lambda map

```python
a = [1, 2, 3]
b = [4, 5, 6]
zip(a, b) #返回object
list(zip(a, b))
for i, j in zip(a, b):
    print(i, j)
def fun1(x, y):
    return (x + y)
fun2 = lambda x, y: x + y#fun2等价于fun1
map(fun1, [1], [2])
list(map(fun1, [1], [2])) #out: [3]
list(map(fun1, [1, 3], [2, 5])) #out: [3, 8]
```

# 浅复制&深复制

```python
import copy
a = [1, 2, 3]
b = a
id(a) #硬盘中得索引
id(b)#同a的索引
b[0] = 11
a #同样改变
c = copy.copy(a) #浅拷贝
a = [1,3,[3,4]]
d = copy.copy(a)
id(a) == id(d) #False
id(a[2]) == id(d[2]) #True
e = copy.deepcopy(a)#深拷贝
id(a[2]) == id(e[2]) #False
```

