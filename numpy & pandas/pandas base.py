import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 44, 1]) #序列
print(s)
dates = pd.date_range('20160101', periods=6)
print(dates)

#index代表行 columns代表列
df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns=['a', 'b', 'c', 'd'])
print(df)
df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)
df2 = pd.DataFrame({'A':1., 'B':pd.Timestamp('20180102'), 'C' : pd.Series(1, index = list(range(4)), dtype='float32')
                    ,'E': pd.Categorical(["test", "train", "test", "train"])
                    ,'F':'foo'})
print(df2)
print(df2.dtypes)
print(df2.index) #列序号
print(df2.columns) #行序号
print(df2.values) #所有值
print(df2.describe()) #描述数据
print(df2.T) #转置
print(df2.sort_index(axis=0, ascending=False)) #axis=1对行序列号进行排序ascending=False倒序
print(df2.sort_values(by='E')) #对以第e列为基准进行排序