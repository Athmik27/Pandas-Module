# IMPORTING bringing data from an external file or source into Python

#csv=comma seperated value
#json=javascript object notation

import pandas as pd
df=pd.read_csv("sample.csv")
print(df) # if there are many data's this gives in truncated form.


import pandas as pd
df=pd.read_csv("sample.csv")
print(df.to_string())# there is no truncate of data (truncate means hiding of the data)

import pandas as pd
df=pd.read_json("sample1.json") #save json file in an json format.
print(df)


#read both csv and json file
import pandas as pd
df=pd.read_csv("sample.csv")
df=pd.read_json("sample1.json") #save json file in an json format.
print(df.to_string())