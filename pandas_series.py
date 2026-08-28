#this is an python library

# SERIES is an 1D data structure (an single column table)

import pandas as pd
# print(pd.__version__) #pd means access pandas

data=[100,105,110]
series=pd.Series(data) #.Series() is an constructor
print(series) #when we run this we get metadata at the bottom


data=[100,105,110]
series=pd.Series(data,index=["a","b","c"]) #.Series() is an constructor
print(series) #here we are setting an index our own values
print(series.loc["a"]) #loc=location by property this returns the value that is in the label "a"

data=[100,105,110]
series=pd.Series(data,index=["a","b","c"])
series.loc["c"]=20 #means modify using the label.
print(series.loc["c"]) # loc means find the index labeled "c" and change its value to 20.

data=[100,105,110]
series=pd.Series(data,index=["a","b","c"])
series.iloc[0]    # means modify using the position.            
print(series.iloc[0])  #iloc means integer-location based indexing.

data=[100,105,110,115,120]
series=pd.Series(data,index=["a","b","c","d","e"])
print(series[series>=110]) # this prints all the value that are greater than 110.

calories={
    "day_1":1750,
    "day_2":2100,
    "day_3":1700,
    "day_4":1850,

 }
series=pd.Series(calories)
print(series.loc["day_1"])

# this updates the calories of day_4
series.loc["day_4"]+=2000 
print(series.loc["day_4"])
print(series)

print(series[series>=2000])
