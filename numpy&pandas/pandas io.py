'''
pandas可以读取和保存的格式:
    csv excel hdf sql json msgpack html gbq stata sas
    clipboard pickle
'''
import pandas as pd
data = pd.read_csv('Student.csv', )
print(data)
data.to_pickle('Student.pickle')
 