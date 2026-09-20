# Write Pandas code to display only the Pokémon whose Weight is greater than 0.5
import pandas as pd

df = pd.read_csv("sample.csv")
heavy_pokemon=df[df[('Weight')]>50]
print(heavy_pokemon)

# # Display Pokémon whose Height is greater than 1 AND Weight is greater than 50
df = pd.read_csv("sample.csv")
pokemon_select = df[(df["Height"] > 1) & (df["Weight"] > 50)]
print(pokemon_select)

# # Syntax: df[(df["Column1"] > value) & (df["Column2"] > value)]

# # Display all Pokémon whose Type1 is either "Fire" OR "Water".
df = pd.read_csv("sample.csv")
pokemon_select = df[(df["Type1"] == 'Fire') | (df["Type1"] == 'Water')]
print(pokemon_select)

#  Display the 5 heaviest Pokémon, with the heaviest one appearing first very imp
df = pd.read_csv("sample.csv")
print(df.sort_values("Weight", ascending=False).head(5))

# Find the average Weight of Pokémon for each Type1.
df = pd.read_csv("sample.csv")
group=(df.groupby("Type1"))
print(group['Weight'].mean())

# # Find how many Pokémon belong to each Type1
df=pd.read_csv("sample.csv")
print(df["Type1"].value_counts())

#output predection
import pandas as pd
s = pd.Series([10, 20, 30, 40])
print(s)

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
# s = pd.Series([10, 20, 30, 40, 50])
# print(s.sum()) # we can use mean,max,min,...To sort from large → small, we use s.sort_values(ascending=False)

# # imp
# s = pd.Series([10, 20, 10, 30, 20, 10])
# print(s.value_counts())

# import pandas as pd
# s = pd.Series([10, 20, None, 40])
# print(s.isna()) # checks the Not Avail(NaN) values 

# s = pd.Series([10, None, 30, None, 50])
# print(s.fillna(0)) # fillna() is used to replace missing (NaN) values with another value.

# s = pd.Series([10, None, 30, None, 50])
# print(s.dropna()) # dropna() is used to remove missing (NaN) values from a Series.

# s = pd.Series([10, 20, None, 40, None])
# print(s.count()) # count() tells you the number of non-missing values in a Series.

# s = pd.Series([10, 20, 10, 30, 20, 40])
# print(s.unique()) 

# s = pd.Series([10, 20, 10, 30, 20, 40])
# print(s.nunique())


# s = pd.Series([10, 20, 30, 40], index=["A", "B", "C", "D"])
# s.iloc[2]=100
# print(s)

###
# data={
#     'name':["Mark","Jack","Henry"],
#     'age':[19,20,20],
#     'marks':[80,85,70],
    
# }
# df=pd.DataFrame(data)
# print(df)

###
# data={
#     'name':["Mark","Jack","Henry"],
#     'age':[19,20,20],
#     'marks':[80,85,70],
# }
# df=pd.DataFrame(data)
# print(df["name"])

# remember
# df["Name"]       # Select a column
# df.loc[0]        # Select row with index 0
# df.loc[0, "Name"] # Select a specific value

###
# data={
#     'name':["Mark","Jack","Henry"],
#     'age':[19,20,20],
#     'marks':[80,85,70],
# }
# df=pd.DataFrame(data)
# print(df[["name","marks"]])

# ###
# data={
#     'name':["Mark","Jack","Henry"],
#     'age':[19,20,20],
#     'marks_python':[80,85,70],
# }
# df=pd.DataFrame(data)
# print(df[df["name"] == "Jack"])

###
# data={
#     'name':["Mark","Jack","Henry"],
#     'age':[19,20,20],
#     'marks_python':[80,85,70],
# }
# df=pd.DataFrame(data,index=["student1",'student2','student3'])
# print(df.loc["student2"])
# # note:
# df.loc[row_label, column_label]
# df.loc[row_label, [column1, column2]]

###
# Using the same DataFrame, select student1 and student3, but display only the name column.
# data={
#     'name':["Mark","Jack","Henry"],
#     'age':[19,20,20],
#     'marks_python':[80,85,70],
# }
# df=pd.DataFrame(data,index=["student1",'student2','student3'])
# print(df.loc[["student1", "student3"], "name"])

# # Using the same DataFrame, select:
# # student1 and student3
# # name and marks_python
# data={
#     'name':["Mark","Jack","Henry"],
#     'age':[19,20,20],
#     'marks_python':[80,85,70],
# }
# df=pd.DataFrame(data,index=["student1",'student2','student3'])
# print(df.loc[["student1", "student3"], ["name", "marks_python"]])

# ###
# data={
#     'name':["Mark","Jack","Henry"],
#     'age':[19,20,20],
#     'marks_python':[80,85,70],
# }
# df=pd.DataFrame(data,index=["student1",'student2','student3'])
# print(df.iloc[[0, 2], [0, 2]])
# #note:
# df.iloc[0]          # row 0
# df.iloc[:, 0]       # column 0
# df.iloc[[0, 2]]     # rows 0 and 2
# df.iloc[[0, 2], [0, 2]]  # rows 0,2 and columns 0,2


# display n print student who scored more than 80
# import pandas as pd
# data = {
#     "Name": ["Rahul", "Anu", "Kiran", "Sneha", "Arjun"],
#     "Age": [21, 20, 22, 19, 23],
#     "Marks": [78, 92, 65, 88, 95]
# }
# df = pd.DataFrame(data)
# print(df["Marks"]>80)# this gives me Boolean values.
# print(df[df['Marks']>80]) # this gives the actual result.

# Find and display students whose Age is greater than 20 AND Marks are greater than 80.
# data={
#     'name':["MARK","JACK","HENRY","NATALIE"],
#     'age':[21,22,20,19],
#     'marks':[80,75,90,85],
# }
# df=pd.DataFrame(data)
# print(df[(df["Age"] > 20) & (df["Marks"] > 80)])

# # same as above but with or condition
# data={
#         'name':["MARK","JACK","HENRY","NATALIE"],
#         'age':[21,22,20,19],
#         'marks':[80,75,90,85],
# }
# df=pd.DataFrame(data)
# print(df[(df['age']<20)| (df["marks"]>80)])

# ### imp place question
# data = {
#     "Name": ["Rahul", "Anu", "Kiran", "Sneha", "Arjun"],
#     "Age": [21, 20, 22, 19, 23],
#     "Marks": [78, 92, 65, 88, 95]
# }
# df = pd.DataFrame(data)
# df["Result"] = df["Marks"] >= 40
# print(df)

# write code to sort the students by Marks from highest to lowest
data={
    "name":['raju','manglu','bheem','kumar','yasir','abdul'],
    "marks":[75,60,70,100,85,55],
}
df=pd.DataFrame(data)
print(df.sort_values('marks')) # ascending=False means descending order (highest → lowest).

# Find the average marks of each department.
data = {
    "name": ["raju", "manglu", "bheem", "kumar", "yasir", "abdul"],
    "department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "marks": [75, 60, 70, 100, 85, 55]
}
df = pd.DataFrame(data)
print(df.groupby("department")["marks"].mean())

# Find how many students are in each department.
data = {
    "name": ["raju", "manglu", "bheem", "kumar", "yasir", "abdul"],
    "department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "marks": [75, 60, 70, 100, 85, 55]
}

df = pd.DataFrame(data)
print(df["department"].value_counts())

# # Remove the duplicate rows and display the DataFrame containing only unique records.
data = {
    "name": ["raju", "manglu", "raju", "kumar", "manglu"],
    "marks": [75, 60, 75, 100, 60]
}
df = pd.DataFrame(data)
print(df.drop_duplicates())

# # Display students who:
# Have marks >= 60
# Are from CSE
# Sort the result by marks from highest to lowest
import pandas as pd

data = {
    "name": ["Raju", "Bheem", "Kumar", "Anu", "Sneha", "Arjun"],
    "department": ["CSE", "ECE", "CSE", "ECE", "CSE", "ECE"],
    "marks": [75, 45, 90, 35, 85, 95],
    "age": [21, 22, 20, 19, 21, 23]
}
df = pd.DataFrame(data)
print(df[(df["marks"] >= 60) & (df["department"] == "CSE")].sort_values("marks", ascending=False))
# df[(condition1) & (condition2)].sort_values("column", ascending=False)
