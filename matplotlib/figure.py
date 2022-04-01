import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2 * x + 1
y2 = x ** 2
plt.figure()
plt.plot(x, y1)

plt.figure(num=3, figsize=(8, 5)) #num序号， figsize 长宽比
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=10.0, linestyle='--') #颜色 宽度 线段格式

plt.show()