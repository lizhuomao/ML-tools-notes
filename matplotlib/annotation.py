import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure(num=1, figsize=(8, 5))
plt.plot(x, y,)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='b')#点
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5) #k--黑色的虚线

#method 1
#内容 位置 基于（数据） 偏移量 字体大小 箭头（格式 弧度）
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0,y0), xycoords='data', xytext=(+30, -30), textcoords='offset points',
             fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

#method 2
#位置 内容 字体格式
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size':16, 'color':'r'})

plt.show()
