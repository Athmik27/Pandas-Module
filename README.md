  PANDAS 

Pandas is a popular open-source Python library used for data manipulation, analysis, and cleaning.

Main Data Structures:

(i)Series:
A one-dimensional labeled array.

Eg:
import pandas as pd
s = pd.Series([10, 20, 30, 40])
print(s)


(ii)DataFrame:
A two-dimensional table with rows and columns.

Eg:
import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35]
}
df = pd.DataFrame(data)
print(df)
