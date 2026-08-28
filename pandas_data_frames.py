# DATA FRAMES are the tabular data structure with rows and column.
# df is simply a common variable name used for a Pandas DataFrame.
import pandas as pd

data={

    'name':["spongebob","patrick","squidward"],
    'age':[30 , 35 , 50],
}
# represent dataframe as df
df=pd.DataFrame(data) #converts that dictionary into a DataFrame:
print(df)


data={

    'name':["spongebob","patrick","squidward"],
    'age':[30 , 35 , 50],
}
df=pd.DataFrame(data,index=["employee_1","employee_2","employee_3"]) 
print(df)


data={

    'name':["spongebob","patrick","squidward"],
    'age':[30 , 35 , 50],
}
df=pd.DataFrame(data,index=["employee_1","employee_2","employee_3"]) 
print(df.loc["employee_1"]) # this gives me all the data of an employee_1 only


data={

    'name':["spongebob","patrick","squidward"],
    'age':[30 , 35 , 50],
}
df=pd.DataFrame(data,index=["employee_1","employee_2","employee_3"]) 
print(df.iloc[1]) # this gives me the data of an employee_2 by the help of index


data={

    'name':["spongebob","patrick","squidward"],
    'age':[30 , 35 , 50],
}
df=pd.DataFrame(data,index=["employee_1","employee_2","employee_3"]) 
# # if need to add a new column
df["job"]=["cook","n/a",'manager']
print(df)


data={

    'name':["spongebob","patrick","squidward"],
    'age':[30 , 35 , 50],
}
df=pd.DataFrame(data,index=["employee_1","employee_2","employee_3"]) 
# if need to add a new row
new_row=pd.DataFrame([{"name":"sandy","age":28,"job":'hr'}],
                     index=["employee_5"])
df=pd.concat([df,new_row]) 
print(df)


data={

    'name':["spongebob","patrick","squidward"],
    'age':[30 , 35 , 50],
}
df=pd.DataFrame(data,index=["employee_1","employee_2","employee_3"]) 
# if need to add a new rows (many row)
new_rows=pd.DataFrame([{"name":"sandy","age":28,"job":'hr'},
                        {"name":"sandra","age":25,"job":'manager'},
                        {"name":"alex","age":21,"job":'finance'},
                        {"name":"aleena","age":20,"job":'project head'}],
                     index=["employee_5","employee_6","employee_7","employee_8"])
df=pd.concat([df,new_rows]) 
print(df)
