# Write Pandas code to display only the Pokémon whose Weight is greater than 0.5
import pandas as pd

# df = pd.read_csv("sample.csv")
# heavy_pokemon=df[df[('Weight')]>50]
# print(heavy_pokemon)

# Display Pokémon whose Height is greater than 1 AND Weight is greater than 50
# df = pd.read_csv("sample.csv")
# pokemon_select = df[(df["Height"] > 1) & (df["Weight"] > 50)]
# print(pokemon_select)

# Syntax: df[(df["Column1"] > value) & (df["Column2"] > value)]

# Display all Pokémon whose Type1 is either "Fire" OR "Water".
# df = pd.read_csv("sample.csv")
# pokemon_select = df[(df["Type1"] == 'Fire') | (df["Type1"] == 'Water')]
# print(pokemon_select)

#  Display the 5 heaviest Pokémon, with the heaviest one appearing first very imp
# df = pd.read_csv("sample.csv")
# print(df.sort_values("Weight", ascending=False).head(5))

# Find the average Weight of Pokémon for each Type1.
# df = pd.read_csv("sample.csv")
# group=(df.groupby("Type1"))
# print(group['Weight'].mean())

# # Find how many Pokémon belong to each Type1
# df=pd.read_csv("sample.csv")
# print(df["Type1"].value_counts())

#output predection
# import pandas as pd
# s = pd.Series([10, 20, 30, 40])
# print(s)

# import pandas as pd
# s = pd.Series([100, 200, 300], index=["A", "B", "C"])
# # print(s["B"])

# import pandas as pd
# s = pd.Series([10, 20, 30, 40])
# print(s[2])

# import pandas as pd
# s = pd.Series(50, index=["A", "B", "C"])
# print(s)

# import pandas as pd
# s = pd.Series([10, 20, 30, 40])
# print(s[1:3])

# import pandas as pd
# s = pd.Series([10, 20, 30], index=["A", "B", "C"])
# print(s.index)

# import pandas as pd
# s = pd.Series([10, 20, 30], index=["A", "B", "C"])
# print(s.values) # s.index    # gives labels
#                s.values   # gives values

# Create a Pandas Series containing:
# 10, 20, 30, 40, 50
# Then print the Series.
# s=pd.Series([10,20,30,40,50])
# print(s)

# Create a Pandas Series with these values:

# 100, 200, 300

# and use these custom indexes:

# "A", "B", "C"

# Then print the Series
# s=pd.Series([100,200,300],index=["A","B","C"])
# print(s)

# Create this Series:

# A    100
# B    200
# C    300

# Then print only the value 200 using its index label.
# s=pd.Series([100,200,300],index=["A","B","C"])
# print(s.loc["B"])

# Given:

# s = pd.Series([100, 200, 300], index=["A", "B", "C"])

# # Write code to print 300 using iloc.
# s=pd.Series([100,200,300],index=["A","B","C"])
# print(s.iloc[2])

# Create this Series:

# A    10
# B    20
# C    30
# D    40

# Then write code to print only 20 and 30 using iloc.
# s=pd.Series([10,20,30,40],index=["A","B","C","D"])
# print(s.iloc[1:3])

# Create this Series:

# A    10
# B    20
# C    30
# D    40

# Then write code to change the value at index "B" from 20 to 50.

# Use .loc[].
# s=pd.Series([10,20,30,40],index=["A","B","C","D"])
# s.loc["B"]=50
# print(s)

# s = pd.Series([10, 20, 30, 40], index=["A", "B", "C", "D"])

# Change the value at position 2 to 100 using .iloc.
# s = pd.Series([10, 20, 30, 40], index=["A", "B", "C", "D"])
# s.iloc[2]=100
# print(s)

# Given:

# s = pd.Series([10, 25, 30, 15, 40])

# Write code to print only values greater than 20.
# s = pd.Series([10, 25, 30, 15, 40])
# print(s[s > 20])

# Given:

# s = pd.Series([10, 25, 30, 15, 40])

# Write code to print only values less than 30.
# s = pd.Series([10, 25, 30, 15, 40])
# print(s[s<30])

# Given:

# s = pd.Series([10, 20, 30, 40, 50])

# Print values that are greater than 20 AND less than 50.
# s = pd.Series([10, 25, 30, 15, 40])
# print(s[(s>20) & (s<50)])

# Using:

# s = pd.Series([10, 25, 30, 15, 40])

# Print values that are less than 15 OR greater than 35
# s = pd.Series([10, 25, 30, 15, 40])
# print(s[(s<15)| (s>35)])

# Given:

# s = pd.Series([10, 20, 30, 40, 50])

# Write code to find the total of all values.
s = pd.Series([10, 20, 30, 40, 50])
print(s.sum()) # we can use mean,max,min,...To sort from large → small, we use s.sort_values(ascending=False)

# imp
s = pd.Series([10, 20, 10, 30, 20, 10])
print(s.value_counts())

import pandas as pd
s = pd.Series([10, 20, None, 40])
print(s.isna()) # checks the Not Avail(NaN) values 

s = pd.Series([10, None, 30, None, 50])
print(s.fillna(0)) # fillna() is used to replace missing (NaN) values with another value.

s = pd.Series([10, None, 30, None, 50])
print(s.dropna()) # dropna() is used to remove missing (NaN) values from a Series.

s = pd.Series([10, 20, None, 40, None])
print(s.count()) # count() tells you the number of non-missing values in a Series.

s = pd.Series([10, 20, 10, 30, 20, 40])
print(s.unique()) 

s = pd.Series([10, 20, 10, 30, 20, 40])
print(s.nunique())

