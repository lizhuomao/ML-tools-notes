import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
df.iloc[2, 2] = 1111
df.loc['20130101', 'B'] = 2222
df.A[df.A > 4] = 0 #集体修改
print(df)
df[df.A > 4] = 0
print(df)
df['F'] = np.nan #整列插入
print(df)
df['E'] = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130101', periods=6))
print(df)

