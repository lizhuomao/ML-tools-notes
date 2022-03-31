import numpy as np

a = np.arange(4)
print(a)
b = a
c = a
d = b
a[0] = 11
print(a)
print(b is a, b)
print(d is a, d)
d[1:3] = [22, 33]
print(d, a)
b = a.copy() #deepcopy
print(b)
a[3] = 44
print(a, b)