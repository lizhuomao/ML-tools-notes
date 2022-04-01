import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

#第i帧
def animate(i):
    line.set_ydata(np.sin(x + i/10))
    return line,
def init():
    line.set_ydata(np.sin(x))
    return line,

#frames 100帧 interval update的频率 blit是否更新整张图片
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100, init_func=init, interval=20, blit=True)

plt.show()
