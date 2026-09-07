#AGGREGATE FUNCTION  takes many values and produces one result.

import pandas as pd

df=pd.read_csv("sample.csv")
print(df)
#   mean() func is usually used to find mean/average for numeric data column's only

# these agregate func is for whole data frame
print(df.mean(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True)) # numeric_only=True means peform operations on that column which has numerical values.so any column that has text data are being ignored and only numerical data type is used.
# and we use this numeric_only=True because for 'text' performing operations like mean,sum is not valid.
print(df.count()) # for count we need not pass any argument
                  # count() wont include any null values and counts the number of non-empty  values in each column's

# agregate func for single column
# syntax:
# df["column_name"].aggregate_function()
print(df["Height"].mean()) # inside [] just put the column name
print(df["Weight"].sum())
print(df["Height"].min())
print(df["Weight"].max())
print(df['Height'].count())

# we now group the data frame but use of groupby() keyword
group=df.groupby("Type1")
print(group) #we get the below warning because for groupby() we must tell it what to do with each group.
#<pandas.api.typing.DataFrameGroupBy object at 0x10880fe00>
# so we write print(group["Height"].sum())
# Separate my DataFrame into groups according to the Type1 column."

group=df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].sum())


# df["Height"].mean()      # Average
# df["Height"].sum()       # Total
# df["Height"].min()       # Minimum
# df["Height"].max()       # Maximum
# df["Height"].count()     # Number of non-empty values
# df["Height"].median()    # Middle value
# df["Height"].std()       # Standard deviation
# df["Height"].var()       # Variance

# agg() function:
# here we can perform multiple aggregate functions at once.

print(df["Height"].agg(["mean", "min", "max", "sum"]))
