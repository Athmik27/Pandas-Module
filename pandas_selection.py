#SELECTION means choosing specific rows or columns from a DataFrame.

import pandas as pd

df=pd.read_csv('sample.csv')

# selection by column
print(df["Name"])   # here inside the [] we write the column name 
                    # again this form's an truncated version to get the entire data table we write
                    #  .to_string() after the []
print(df[["Name","Height"]])

#selection by row or rows

import pandas as pd
df=pd.read_csv('sample.csv',index_col="Name") # usually pandas create an default index value with 0,1,2,3....
                                              # but index_col="name" is telling to create 'Name' as an Index
print(df)

# here we find an  data in thr table
import pandas as pd
df=pd.read_csv('sample.csv',index_col="Name") # usually pandas create an default index value with 0,1,2,3....
                                              # but index_col="name" is telling to create 'Name' as an Index
print(df.loc["Caterpie"]) # find the row whose index is Caterpie

#here we find an particular data
import pandas as pd
df=pd.read_csv('sample.csv',index_col="Name") # usually pandas create an default index value with 0,1,2,3....
                                              # but index_col="name" is telling to create 'Name' as an Index
print(df.loc["Caterpie",["Height","Weight"]]) # this gives height and weight of the particular mention index value only


import pandas as pd
df=pd.read_csv('sample.csv',index_col="Name") # usually pandas create an default index value with 0,1,2,3....
                                              # but index_col="name" is telling to create 'Name' as an Index
print(df.loc["Squirtle":"Caterpie",["Height","Weight"]]) # this gives height and weight of the particular mention index value from  Squirtle and Caterpie

import pandas as pd
df=pd.read_csv('sample.csv',index_col="Name")
print(df.iloc[0:11]) # this gives the data from 0 to 10 only

# CHECKS whether the pokemon is found or no
import pandas as pd
df=pd.read_csv('sample.csv',index_col="Name")
pokemon=input("enter the name of pokemon:")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")