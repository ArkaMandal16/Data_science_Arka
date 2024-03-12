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

df_csv = pd.read_csv(r"C:\Users\91743\Documents\Book1.csv")
print(df_csv)

print(df_csv.columns)
print(df_csv.shape)
print(df_csv.size)

print(df_csv.head)
print(df_csv.tail)
print(df_csv.describe())
print(df_csv.info())

#describe function only gives numeric columns as output

df_csv1 = pd.read_csv(r"C:\Users\91743\Desktop\IT_DATA BASE.csv")
print(df_csv1.tail)

print(df_csv1.info())

print(df_csv1.isnull())

print(df_csv1.isnull().sum())

print(df_csv1.isnull().sum().sum())

#deleting rows with null value

print(df_csv1.shape)
df_new = df_csv1.dropna()
print(df_new)

#deleting columns with null value
df_new = df_csv1.dropna(axis=1)
print(df_new)

#selective dropping of null rows

df_new1 = df_csv1.dropna(how="any") #if onlu one element in the row is null, it will remove the row

df_new2 = df_csv1.dropna(how="all") #if and only if all the elements in the row is null, it will remove the row

print(df_csv1.dropna(inplace= True))

# filling null places in a data frame

print(df_csv1.fillna('fuck you'))

#ffill: forward fill: just copies the previous non-null value and puts it in the null place; if no axis is mentioned thn by default it works along row. otherwise if axis = 1, then it works along column.

print(df_csv1.fillna(method='ffill'))

#ffill: forward fill: just copies the following non-null value and puts it in the null place

print(df_csv1.fillna(method='bfill'))
