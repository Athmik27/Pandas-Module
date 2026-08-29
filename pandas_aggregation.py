#AGGREGATE FUNCTION  takes many values and produces one result.

import pandas as pd

df=pd.read_csv("sample.csv")
print(df)
#mean() func is usually used to find mean/average for numeric data column's only

# these agregate func is for whole data frame
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.count()) # for count we need not pass any argument
                  # count() wont include any null values

# agregate func for single column
print(df["Height"].mean()) # inside [] just put the column name
print(df["Weight"].sum())
print(df["Height"].min())
print(df["Weight"].max())
print(df['Height'].count())

# we now group the data frame but use of groupby() keyword
group=df.groupby("Type1")
print(group) #we get the below warning because for groupby() we must tell it what to do with each group.
#<pandas.api.typing.DataFrameGroupBy object at 0x10880fe00>
# so we write
group=df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())
