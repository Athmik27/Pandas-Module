#DATA CLEAANING is removing an incomplete data
#75% of work with pandas is data cleaning

import pandas as pd

df=pd.read_csv("sample.csv")
print(df)

#(1) drop the irrelevent columns
df=df.drop(columns=["Legendary"])
print(df)

df=df.drop(columns=["Legendary","No"])# this removes No and Legendary columms.
print(df)

#(2) handel missing data
df=df.dropna(subset=["Type2"]) # if no subset dropna check's the entire data table.
print(df) 
#dropna=drop not available removes rows containing missing values.
#subset=["Type2"] → Tells pandas Only check the Type2 column for missing values."

#drop()      → I tell Pandas WHAT to drop
#dropna()    → Pandas finds missing values and drops them
print(df.to_string()) # print(df.to_string())
# asks Pandas to convert the whole DataFrame into a string, so you can see all the data.



#fillna =fill not available this fills the not available columns with 'None'
df=df.fillna({"Type2": "None"}) # df.fillna({column: replacement_value})
print(df.to_string())

#(3) fix inconsistent values
df["Type"]=df["Type1"].replace({"Grass":"GRASS"}) # df[Type] creates an new column that stores the updated value.
print(df.to_string()) # this replaces the Grass  to GRASS

#(4) standardize text
df["Name"]=df["Name"].str.lower() # this gives all the names in lower case
print(df.to_string())

#(5) fix data type
df['Legendary']=df['Legendary'].astype(bool) # this gives all the Legendary  in boolean value
print(df.to_string())

#(6) remove duplicate datas
df=df.drop_duplicates()
print(df.to_string())

df["Name"].str.lower()      # lowercase
df["Name"].str.upper()      # uppercase
df["Name"].str.strip()      # remove extra spaces.