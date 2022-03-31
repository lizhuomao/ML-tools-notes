import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#plot data

data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()

data = pd.DataFrame(np.random.randn(1000, 4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data = data.cumsum()
print(data.head()) #输出前五行
data.plot()
#plot methods:
#'bar 'hist' 'box' 'kde' 'area' 'scatter' 'hexbin' 'pie'
#data.plot()
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1') #树状图
data.plot.scatter(x='A', y='C', color='DarkGreen', label='Class 2', ax=ax)
plt.show()
