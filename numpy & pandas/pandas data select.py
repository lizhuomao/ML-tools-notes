import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates, columns=['A', 'B','C','D'])
print(df)
print(df['A'], df.A)
print(df[0:3], df['20130102':'20130104'])

print(df.loc['20130102']) #以标签的名义来选择
print(df.loc[:, ['A', 'B']]) #只打印某列
print(df.loc['20130102', ['A', 'B']])
print(df.iloc[3]) #索引方式打印
print(df.iloc[3:5, 1:3])
print(df.iloc[[1,3,5], 1:3])
#print(df.ix[:3, ['A', 'C']])#混合筛选 已被弃用
print(df[df.A > 8])

