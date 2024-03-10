from operator import index
from os import name
import pandas as pd

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