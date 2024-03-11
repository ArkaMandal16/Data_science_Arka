from operator import index
from os import name
import pandas as pd
import numpy as np

#pd.__version__

#pandas series

lst = [1,2,3]
series = pd.Series(lst)
print(series)

a = pd.Series([1,2,3,4], index=['a','b','c','d'], name='random')
print(a)

#pandas series using dictionary

dict = pd.Series({'a':1,'b':2,'c':3})
print(dict)

dict1 = pd.Series({'a':[1,2,3],'b':[1,2,3],'c':[1,2,3]})
print(dict1)

#pandas dataframe:

lst = np.array([1,2,3])
df = pd.DataFrame(lst)
print(df)

lst1 = [[1,2,3],[10,2,3]]
df1 = pd.DataFrame(lst1)
print(df1)

b = {'roll':pd.Series([1,2,3,4,5]),
     'DSA':pd.Series([10,20,30,40,50]),
     'Math':pd.Series([10,20,30,40,50])}
df2 = pd.DataFrame(b)
print(df2)

#CSV files as dataframes

df_csv = pd.read_csv()
print(df_csv)

print(df_csv.columns)
print(df_csv.shape)


