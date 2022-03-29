# print()

```python
print(1)
```

`print 1`不带括号的语法在python2.7以下的版本使用

```python
print("")#输入中含有单引号时使用
print('\'')#使用转义字符\可以达到同样的效果
#字符串的连接
print('apple' + 'car')
print('apple' + str(4))
print(int('1') + 2) #out:3
```

# 数学

```python
2**2 #2的平方 
9//4 #9除以4取整
```



# 自变量variable

```python
apple = 10
print(apple)
a = 1
b = 2
c = 3
print(a, b, c)
a, b, c = 1,2,3
print(a, b, c)
del a
del b, c #删除单个或多个对象
```

# 循环

```python
condition = 1
while condition < 10:
    print(condition)
    condition++;
exlist = [1,2,3,4]
for i in exlist:
    print(i)
print(exlist)
for i in range(1, 10):
    print(i)
for i in range(1, 10, 2):#步长
    print(i)

```

## 调整结构：

**for** windows : control + [

**for** mac : command + [

# 条件

```python
if x > y:
	print('.')
if x > y:
    print(1)
elif y > x:
    print(2)
else:
    print(3)

```

# 函数

```python
def function(a, b):
    c = a + b
    return c
function(1, 2)
def fun(a, b = 'red', c = True):#函数默认参数，没有默认参数的值要放在前面
    print(a, b, c)
print(a)
X = 100 #全局变量
a = None #需要提前定义
def fun():
    global a #全局变量
    a = 10 #局部变量
    print(a)

```

sudo pip3 install -U name 升级

# 文件

```python
text = "This is my first test.\nThis is last line."
append_text = "\nThis is appended file"
my_file = open('my file.txt', 'w')#打开形式w:write r:read a:append(追加)
my_file.write(text)
my_file.close()
my_file = open('my file.txt', 'a')#append
my_file.write(append_text)
my_file.close()
file = open('my file.txt', 'r')
content = file.read()#读取内容
content = file.readline() #读取一行
content = file.readlines()#全部读取，按list存储
python_list = [1, 2, 3, 4, 5, 'dahi', 'fuiq']
print(content)
```

# 面向对象

```python
class Calculator:
    def __init__(self, name, price, hight = 2):
        self.name = name
        self.price = price
        self.h = hight
    def add(self, x, y): #self代表的是类的实例
        print(self.name)
        result = x + y
        print(result)
calcul = Calculator()
calcul.name
calcul.add(1, 2)
c = Calculator('Bad Calculator', 1, 2)
```

# 输入

```python
a_input = input('Please give a number:') #return a string
print("this input number is :", a)
a_input = int(input('please give a number:'))
```

