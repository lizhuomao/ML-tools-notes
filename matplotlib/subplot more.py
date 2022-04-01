import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.figure()

#method 1: subplot2grid
#网格大小 索引 跨度
ax1 = plt.subplot2grid((3, 3), (0,0), colspan=3, rowspan=1)
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title')
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2,)
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2,)
ax2 = plt.subplot2grid((3, 3), (2, 0))
ax2 = plt.subplot2grid((3, 3), (2, 1))

#method 2: gridspec
plt.figure(num=2)
gs = gridspec.GridSpec(3, 3)
ax4 = plt.subplot(gs[0,:])
ax5 = plt.subplot(gs[1,:2])
ax6 = plt.subplot(gs[1:,2])
ax7 = plt.subplot(gs[-1,0])
ax8 = plt.subplot(gs[-1,-2])

#method 3: easy to define structure
plt.figure(num=3)
#figure的object 所有的axis
f, ((ax11,ax12),(ax21,ax22)) = plt.subplots(2, 2, sharex=True,sharey=True)
ax11.scatter([1, 2], [1, 2])
plt.tight_layout()
plt.show()