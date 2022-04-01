import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape((3,3))

#origin='lower'翻转图片
#interpolation check: http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
plt.imshow(a, interpolation='nearest', cmap='bone', origin='upper')
plt.colorbar(shrink=0.9) #压缩颜色树状图到%90

plt.xticks(())
plt.yticks(())
plt.show()