#pandas basics
import pandas as pd
import numpy as np

#creating a series
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
#0    1.0
#1    3.0
#2    5.0
#3    NaN
#4    6.0
#5    8.0
#dtype: float64

print()

#creating a dataframe
dates = pd.date_range('20130101', periods=6)
print(dates)
#DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#               '2013-01-05', '2013-01-06'],
#              dtype='datetime64[ns]', freq='D')

print()

df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)
#                   A         B         C         D
#2013-01-01 -0.469474  0.542560 -0.463418 -0.465730
#2013-01-02  0.241962 -1.913280 -1.724918 -0.562288
#2013-01-03 -1.012831  0.314247 -0.908024 -1.412304
#2013-01-04  1.465649 -0.225776  0.067528 -1.424748
#2013-01-05 -0.544383  0.110923 -1.150994  0.375698
#2013-01-06 -0.600639 -0.291694 -0.601707  1.852278

print()

#creating a dataframe by passing a dict of objects that can be converted to series-like
df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print(df2)

#     A          B    C  D      E    F
#0  1.0 2013-01-02  1.0  3   test  foo
#1  1.0 2013-01-02  1.0  3  train  foo
#2  1.0 2013-01-02  1.0  3   test  foo
#3  1.0 2013-01-02  1.0  3  train  foo

print()

#The columns of the resulting DataFrame have different dtypes
print(df2.dtypes)
#A           float64
#B    datetime64[ns]
#C           float32
#D             int32
#E          category
#F            object
#dtype: object

print()

#If you’re using IPython, tab completion for column names (as well as public attributes) is automatically enabled. Here’s a subset of the attributes that will be completed:

#print(df2.<TAB>)   just an example

#df2.A                  df2.bool
#df2.abs                df2.boxplot
#df2.add                df2.C
#df2.add_prefix         df2.clip
#df2.add_suffix         df2.clip_lower
#df2.align              df2.clip_upper
#df2.all                df2.columns
#df2.any                df2.combine
#df2.append             df2.combine_first
#df2.apply              df2.compound
#df2.applymap           df2.consolidate
#df2.D

print()

#Viewing Data
print(df.head())
#                   A         B         C         D
#2013-01-01 -0.469474  0.542560 -0.463418 -0.465730
#2013-01-02  0.241962 -1.913280 -1.724918 -0.562288
#2013-01-03 -1.012831  0.314247 -0.908024 -1.412304
#2013-01-04  1.465649 -0.225776  0.067528 -1.424748
#2013-01-05 -0.544383  0.110923 -1.150994  0.375698

print()

print(df.tail(3))
#                   A         B         C         D
#2013-01-04  1.465649 -0.225776  0.067528 -1.424748
#2013-01-05 -0.544383  0.110923 -1.150994  0.375698
#2013-01-06 -0.600639 -0.291694 -0.601707  1.852278

print()

#Display the index, columns:
print(df.index)
#DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#               '2013-01-05', '2013-01-06'],
#              dtype='datetime64[ns]', freq='D')

print()

print(df.columns)
#Index(['A', 'B', 'C', 'D'], dtype='object')

print()

#DataFrame.to_numpy() gives a NumPy representation of the underlying data. Note that this can be an expensive operation when your DataFrame has columns with different data types, which comes down to a fundamental difference between pandas and NumPy: NumPy arrays have one dtype for the entire array, while pandas DataFrames have one dtype per column. When you call DataFrame.to_numpy(), pandas will find the NumPy dtype that can hold all of the dtypes in the DataFrame. This may end up being object, which requires casting every value to a Python object.
print(df.to_numpy())
#[[-0.46947439  0.54256004 -0.46341769 -0.46572975]
# [ 0.24196227 -1.91328024 -1.72491783 -0.56228753]
# [-1.01283112  0.31424733 -0.90802408 -1.4123037 ]
# [ 1.46564877 -0.2257763   0.0675282  -1.42474819]
# [-0.54438272  0.11092259 -1.15099358  0.37569802]
# [-0.60063869 -0.29169375 -0.60170661  1.85227818]]

print()

#For df, our DataFrame of all floating-point values, DataFrame.to_numpy() is fast and doesn’t require copying data.
print(df2.to_numpy())
