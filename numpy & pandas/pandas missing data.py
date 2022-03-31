import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
#axis0 行 1列
print(df.isnull()) #是否有缺失
print(np.any(df.isnull) == True) #数据集大的判断
print(df.dropna(axis=0, how='any')) #how = {'any', 'all'}all指所有数据为nan丢掉， any指出现nan就丢掉
print(df.fillna(value=0)) #填上nan的数据
