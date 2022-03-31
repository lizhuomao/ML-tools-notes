import pandas as pd
import numpy as np

#concatenating

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=['a','b','c','d'])
print(df1, df2, df3)
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True) #合并 0按行合并 ignore_index=TRUE重新排序索引
print(res)

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['b','c','d','e'])

print(df1)
print(df2)
res = pd.concat([df1, df2]) #默认join='outer' 外连接 并 inner 交
print(res)
res = pd.concat([df1, df2] , join='inner', ignore_index=True)
print(res)
#res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])
#python现在已经取消join_axes参数
res = df1.append(df2, ignore_index=True) #追加
s1 = pd.Series([1,2,3,4], index = ['a', 'b', 'c', 'd'])
res = df1.append(s1, ignore_index=True)
print(res)