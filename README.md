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


# NOTE TO REMEMBER:

| Function           | Purpose                         |
| ------------------ | ------------------------------- |
| `pd.read_csv()`    | Read a CSV file                 |
| `df.head()`        | Display the first 5 rows        |
| `df.tail()`        | Display the last 5 rows         |
| `df.info()`        | Show dataset information        |
| `df.describe()`    | Generate summary statistics     |
| `df.columns`       | List column names               |
| `df.shape`         | Show number of rows and columns |
| `df.drop()`        | Remove rows or columns          |
| `df.sort_values()` | Sort data                       |
| `df.groupby()`     | Group and aggregate data        |
| `df.isnull()`      | Detect missing values           |
| `df.fillna()`      | Fill missing values             |

## Custom Index

data = pd.Series(
    [80, 90, 75],
    index=["Python", "Pandas", "NumPy"]
)

print(data)

Access a value:
print(data["Pandas"])


 DataFrame

A **DataFrame** is a two-dimensional table.


DataFrame = Rows + Columns

Example:
data = {
    "Name": ["Athmik", "Rahul", "Arun"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)


Inspecting a DataFrame

These functions are extremely important.

## `head()`

Shows the first 5 rows.


df.head()


First 10 rows:


df.head(10)


## `tail()`

Shows the last 5 rows.


df.tail()


## `shape`

print(df.shape)


## `columns`

Shows column names.

print(df.columns)


## `index`

Shows row indexes.

print(df.index)


## `dtypes`

Shows data type of every column.

print(df.dtypes)


## `info()`

Very important for data analysis.

df.info()


Shows:

* Column names
* Number of non-null values
* Data types
* Memory usage



## `describe()`

Provides statistical information.

df.describe()







# 7. Selecting Columns

## One column

```python
df["Name"]
```

This returns a **Series**.

---

## Multiple columns

```python
df[["Name", "Age"]]
```

This returns a **DataFrame**.

### Remember:

```python
df["Name"]
```

→ Series

```python
df[["Name", "Age"]]
```

→ DataFrame

---

# 8. Selecting Rows — `loc`

`loc` selects data using **labels/index names**.

Syntax:

```python
df.loc[row_label]
```

Example:

```python
print(df.loc[0])
```

Select multiple rows:

```python
print(df.loc[[0, 2, 4]])
```

Select rows and columns:

```python
print(df.loc[0, "Name"])
```

Multiple rows and columns:

```python
print(df.loc[[0, 1], ["Name", "Age"]])
```

---

# 9. Selecting Rows — `iloc`

`iloc` selects data using **integer positions**.

Example:

```python
df.iloc[0]
```

First row.

```python
df.iloc[1]
```

Second row.

Select rows:

```python
df.iloc[0:3]
```

Select specific row and column:

```python
df.iloc[0, 1]
```

Meaning:

```text
row position = 0
column position = 1
```

---

## `loc` vs `iloc`

Remember:

```text
loc  → labels
iloc → positions
```

Example:

```python
df.loc[5]
```

→ index label 5

```python
df.iloc[5]
```

→ sixth row position

---

# 10. Adding Columns

Create a new column:

```python
df["Salary"] = [25000, 30000, 35000]
```

Create a column using another column:

```python
df["Bonus"] = df["Salary"] * 0.10
```

Create a calculated column:

```python
df["Total"] = df["Marks"] + 10
```

---

# 11. Deleting Columns

Use `drop()`.

```python
df = df.drop(columns=["Salary"])
```

Multiple columns:

```python
df = df.drop(columns=["Salary", "Bonus"])
```

Alternative:

```python
df.drop("Salary", axis=1, inplace=True)
```

### Important

```text
axis=0 → rows
axis=1 → columns
```

---

# 12. Adding Rows

Modern Pandas generally prefers `pd.concat()` for adding rows.

Example:

```python
new_row = pd.DataFrame({
    "Name": ["Kiran"],
    "Age": [23],
    "Marks": [88]
})

df = pd.concat([df, new_row], ignore_index=True)
```

---

# 13. Filtering Data

Filtering is one of the **most important Pandas topics**.

Suppose:

```text
Name     Age     Marks
Alex      20      85
Bob       21      70
John      22      90
```

## Filter marks greater than 80

```python
df[df["Marks"] > 80]
```

---

## Filter age equal to 20

```python
df[df["Age"] == 20]
```

---

## Filter age not equal to 20

```python
df[df["Age"] != 20]
```

---

## Greater than or equal

```python
df[df["Marks"] >= 80]
```

---

## Less than

```python
df[df["Marks"] < 80]
```

---

## Multiple conditions

Use:

```text
& → AND
| → OR
~ → NOT
```

### AND

```python
df[(df["Age"] > 20) & (df["Marks"] > 80)]
```

### OR

```python
df[(df["Age"] > 20) | (df["Marks"] > 80)]
```

### NOT

```python
df[~(df["Age"] > 20)]
```

### ⚠️ Important

Don't use:

```python
df[df["Age"] > 20 and df["Marks"] > 80]
```

Use:

```python
df[(df["Age"] > 20) & (df["Marks"] > 80)]
```

---

# 14. Sorting Data

## Sort ascending

```python
df.sort_values("Marks")
```

## Sort descending

```python
df.sort_values("Marks", ascending=False)
```

Multiple columns:

```python
df.sort_values(
    ["Age", "Marks"],
    ascending=[True, False]
)
```

---

# 15. Aggregate Functions

Aggregate functions calculate summary values.

## Single column

```python
df["Height"].mean()
df["Weight"].sum()
df["Height"].min()
df["Weight"].max()
df["Height"].count()
df["Height"].median()
df["Height"].std()
df["Height"].var()
```

### Common functions

```text
mean()    → average
sum()     → total
min()     → minimum
max()     → maximum
count()   → number of non-missing values
median()  → middle value
std()     → standard deviation
var()     → variance
```

---

## Whole DataFrame

```python
df.mean(numeric_only=True)
df.sum(numeric_only=True)
df.min(numeric_only=True)
df.max(numeric_only=True)
```

`numeric_only=True` means:

> Perform the operation only on numeric columns.

---

# 16. GroupBy

`groupby()` is one of the **most important Pandas concepts**.

It means:

> Split data into groups and perform an operation on each group.

Suppose:

```text
Name       Type1       Height
Bulbasaur  Grass        0.7
Ivysaur    Grass        1.0
Charmander Fire         0.6
Charmeleon Fire         1.1
Squirtle   Water        0.5
```

Group by `Type1`:

```python
group = df.groupby("Type1")
```

Now calculate average height:

```python
df.groupby("Type1")["Height"].mean()
```

Calculate total:

```python
df.groupby("Type1")["Height"].sum()
```

Minimum:

```python
df.groupby("Type1")["Height"].min()
```

Maximum:

```python
df.groupby("Type1")["Height"].max()
```

Count:

```python
df.groupby("Type1")["Height"].count()
```

---

## GroupBy with multiple columns

```python
df.groupby(["Type1", "Type2"])["Weight"].mean()
```

---

## `agg()`

Perform multiple operations at once.

```python
df["Height"].agg(["mean", "min", "max", "sum"])
```

With groupby:

```python
df.groupby("Type1")["Height"].agg(
    ["mean", "min", "max"]
)
```

---

# 17. Missing Data

Missing values are usually represented as:

```text
NaN
```

---

## Detect missing values

```python
df.isna()
```

or:

```python
df.isnull()
```

---

## Count missing values

```python
df.isna().sum()
```

This is extremely useful.

Example:

```text
Name      0
Age       2
Weight    5
Type2    10
```

---

## Remove missing values

```python
df.dropna()
```

This removes rows containing missing values.

---

## Check only one column

```python
df.dropna(subset=["Type2"])
```

Meaning:

> Remove rows where `Type2` is missing.

---

## Fill missing values

```python
df.fillna(0)
```

Fill a specific column:

```python
df["Age"] = df["Age"].fillna(20)
```

Dictionary:

```python
df = df.fillna({
    "Age": 20,
    "Type2": "None"
})
```

---

## Fill with mean

Very common in data preprocessing:

```python
df["Age"] = df["Age"].fillna(
    df["Age"].mean()
)
```

---

## Fill with median

```python
df["Age"] = df["Age"].fillna(
    df["Age"].median()
)
```

---

# 18. Data Cleaning

Data cleaning means:

> Detecting and correcting or removing incorrect, incomplete, inconsistent, duplicate, or irrelevant data.

Typical process:

```text
Raw Data
   ↓
Inspect
   ↓
Remove unnecessary columns
   ↓
Handle missing values
   ↓
Fix incorrect values
   ↓
Standardize text
   ↓
Fix data types
   ↓
Remove duplicates
   ↓
Clean Data
```

---

## Remove irrelevant columns

```python
df = df.drop(columns=["No", "Legendary"])
```

---

## Remove missing rows

```python
df = df.dropna(subset=["Type2"])
```

---

## Fill missing values

```python
df = df.fillna({
    "Type2": "None"
})
```

---

## Fix inconsistent values

```python
df["Type1"] = df["Type1"].replace({
    "Grass": "GRASS"
})
```

---

## Standardize text

```python
df["Name"] = df["Name"].str.lower()
```

---

## Remove duplicates

```python
df = df.drop_duplicates()
```

---

# 19. String Operations

Pandas provides `.str` for string operations.

## Lowercase

```python
df["Name"].str.lower()
```

## Uppercase

```python
df["Name"].str.upper()
```

## Remove spaces

```python
df["Name"].str.strip()
```

## Replace text

```python
df["Name"].str.replace("a", "@")
```

## Contains

```python
df[df["Name"].str.contains("chu")]
```

## Starts with

```python
df[df["Name"].str.startswith("A")]
```

## Ends with

```python
df[df["Name"].str.endswith("u")]
```

## String length

```python
df["Name"].str.len()
```

---

# 20. Changing Data Types

Use:

```python
astype()
```

Example:

```python
df["Age"] = df["Age"].astype(int)
```

Convert to float:

```python
df["Age"] = df["Age"].astype(float)
```

Convert to string:

```python
df["Age"] = df["Age"].astype(str)
```

Convert to boolean:

```python
df["Legendary"] = df["Legendary"].astype(bool)
```

Check data types:

```python
df.dtypes
```

---

## `to_numeric()`

Useful when data contains invalid numerical values.

```python
df["Age"] = pd.to_numeric(
    df["Age"],
    errors="coerce"
)
```

`errors="coerce"` converts invalid values to `NaN`.

---

# 21. Duplicates

Check whether rows are duplicated:

```python
df.duplicated()
```

Count duplicates:

```python
df.duplicated().sum()
```

Remove duplicates:

```python
df = df.drop_duplicates()
```

---

# 22. Replacing Values

## Replace one value

```python
df["Type1"] = df["Type1"].replace(
    "Grass",
    "GRASS"
)
```

## Replace multiple values

```python
df["Type1"] = df["Type1"].replace({
    "Grass": "GRASS",
    "Fire": "FIRE"
})
```

---

# 23. Apply, Map and Map

## `map()`

Usually used with a Series.

```python
df["Marks"] = df["Marks"].map(
    lambda x: x + 5
)
```

---

## `apply()`

Can apply a function to a Series or DataFrame.

```python
df["Marks"] = df["Marks"].apply(
    lambda x: x + 5
)
```

Example:

```python
def grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 75:
        return "B"
    else:
        return "C"

df["Grade"] = df["Marks"].apply(grade)
```

---

## `DataFrame.map()`

For element-by-element transformation across a DataFrame:

```python
df.map(lambda x: str(x))
```

> Older tutorials may mention `DataFrame.applymap()`. In current Pandas, prefer `DataFrame.map()` for element-wise DataFrame transformations.

---

# 24. Value Counts

`value_counts()` counts how frequently each value appears.

Example:

```python
df["Type1"].value_counts()
```

Output might look like:

```text
Water    112
Normal    98
Grass     70
Fire      52
```

This is extremely useful for:

* Categorical data
* Data exploration
* Finding class imbalance
* Machine learning

---

# 25. Unique Values

## Get unique values

```python
df["Type1"].unique()
```

## Count unique values

```python
df["Type1"].nunique()
```

Example:

```python
df["Type1"].nunique()
```

means:

> How many different Type1 values exist?

---

# 26. Index

Every Pandas DataFrame has an index.

```python
print(df.index)
```

Example:

```text
RangeIndex(start=0, stop=100, step=1)
```

Set a column as index:

```python
df = df.set_index("Name")
```

Now:

```text
Name         Type1
Bulbasaur    Grass
Pikachu      Electric
```

---

# 27. Resetting Index

After filtering or grouping, you may want to restore a normal index.

```python
df = df.reset_index()
```

You can remove the old index:

```python
df = df.reset_index(drop=True)
```

Very useful after:

```python
df = df[df["Age"] > 20]
```

---

# 28. Reading CSV

One of the most important Pandas operations.

```python
df = pd.read_csv("sample.csv")
```

Print:

```python
print(df)
```

Better for complete output:

```python
print(df.to_string())
```

---

## CSV with custom index

```python
df = pd.read_csv(
    "sample.csv",
    index_col="Name"
)
```

---

## Read selected columns

```python
df = pd.read_csv(
    "sample.csv",
    usecols=["Name", "Type1", "Height"]
)
```

---

# 29. Writing CSV

Save DataFrame:

```python
df.to_csv("cleaned_data.csv")
```

Don't save the index:

```python
df.to_csv(
    "cleaned_data.csv",
    index=False
)
```

---

# 30. Excel Files

Read Excel:

```python
df = pd.read_excel("data.xlsx")
```

Write Excel:

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

---

# 31. JSON

Read JSON:

```python
df = pd.read_json("data.json")
```

Write JSON:

```python
df.to_json("output.json")
```

---

# 32. Merge

`merge()` combines DataFrames using a common column.

Example:

### Students

```text
ID    Name
1     Alex
2     Bob
3     John
```

### Marks

```text
ID    Marks
1     90
2     85
3     95
```

Merge:

```python
result = pd.merge(
    students,
    marks,
    on="ID"
)
```

Result:

```text
ID    Name    Marks
1     Alex     90
2     Bob      85
3     John     95
```

---

## Types of merge

### Inner

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="inner"
)
```

Only matching records.

### Left

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="left"
)
```

Keeps everything from left DataFrame.

### Right

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="right"
)
```

Keeps everything from right DataFrame.

### Outer

```python
pd.merge(
    df1,
    df2,
    on="ID",
    how="outer"
)
```

Keeps everything from both.

---

# 33. Concat

`concat()` combines DataFrames vertically or horizontally.

## Vertical

```python
result = pd.concat(
    [df1, df2],
    ignore_index=True
)
```

Think:

```text
df1
 ↓
df2
 ↓
combined
```

---

## Horizontal

```python
result = pd.concat(
    [df1, df2],
    axis=1
)
```

---

# 34. Join

`join()` is mainly used for combining DataFrames based on indexes.

```python
result = df1.join(df2)
```

You can specify:

```python
df1.join(
    df2,
    how="left"
)
```

---

# 35. Pivot Tables

Pivot tables summarize data.

Example:

```python
pd.pivot_table(
    df,
    values="Weight",
    index="Type1",
    aggfunc="mean"
)
```

Meaning:

> Find average Weight for every Type1.

Multiple calculations:

```python
pd.pivot_table(
    df,
    values="Weight",
    index="Type1",
    aggfunc=["mean", "max", "min"]
)
```

---

# 36. Crosstab

`crosstab()` creates a frequency table.

```python
pd.crosstab(
    df["Type1"],
    df["Type2"]
)
```

Useful for understanding relationships between categorical columns.

---

# 37. Datetime

Convert a column to datetime:

```python
df["Date"] = pd.to_datetime(
    df["Date"]
)
```

Extract year:

```python
df["Date"].dt.year
```

Month:

```python
df["Date"].dt.month
```

Day:

```python
df["Date"].dt.day
```

Day name:

```python
df["Date"].dt.day_name()
```

---

## Filtering dates

```python
df[df["Date"] >= "2026-01-01"]
```

---

# 38. Rolling and Window Operations

Useful for time-series data.

Example:

```python
df["Moving_Average"] = (
    df["Sales"]
    .rolling(3)
    .mean()
)
```

This calculates a 3-value moving average.

Example:

```text
Sales:
10
20
30
40
50

rolling(3):
NaN
NaN
20
30
40
```

---

# 39. Statistics

Common statistical functions:

```python
df["Marks"].mean()
df["Marks"].median()
df["Marks"].mode()
df["Marks"].std()
df["Marks"].var()
df["Marks"].min()
df["Marks"].max()
df["Marks"].sum()
df["Marks"].count()
```

---

## Quantiles

```python
df["Marks"].quantile(0.25)
```

25th percentile.

```python
df["Marks"].quantile(0.50)
```

Median.

```python
df["Marks"].quantile(0.75)
```

75th percentile.

---

# 40. Correlation

Correlation measures how strongly numerical variables are related.

```python
df.corr(numeric_only=True)
```

Example:

```text
          Height   Weight
Height      1.00     0.85
Weight      0.85     1.00
```

Interpretation:

```text
+1 → Strong positive relationship
 0 → No linear relationship
-1 → Strong negative relationship
```

---

# 41. Memory and Performance

For large datasets, performance matters.

Check memory usage:

```python
df.info(memory_usage="deep")
```

Use only required columns:

```python
df = pd.read_csv(
    "data.csv",
    usecols=["Name", "Age", "Marks"]
)
```

Avoid unnecessary loops.

Prefer Pandas operations such as:

```python
df["Marks"] * 2
```

instead of manually looping through every row.

---

# 42. Common Errors

## `KeyError`

```python
df["Height"]
```

If `Height` doesn't exist:

```text
KeyError: 'Height'
```

Check:

```python
print(df.columns)
```

---

## `AttributeError`

Example:

```python
df["Name"].mean()
```

Trying an inappropriate operation on strings can cause errors.

---

## `ValueError`

Often caused by invalid data or incompatible operations.

---

## `SettingWithCopyWarning`

Can happen when modifying a filtered DataFrame.

Instead of:

```python
filtered = df[df["Age"] > 20]
filtered["Marks"] = 100
```

prefer:

```python
filtered = df[df["Age"] > 20].copy()

filtered["Marks"] = 100
```

---

# 43. Pandas for Machine Learning

Pandas is heavily used before training a machine learning model.

Typical process:

```text
Dataset
   ↓
Read dataset
   ↓
Inspect data
   ↓
Clean data
   ↓
Handle missing values
   ↓
Remove duplicates
   ↓
Fix data types
   ↓
Encode categorical values
   ↓
Select features
   ↓
Separate X and y
   ↓
Train ML model
```

---

## Read dataset

```python
df = pd.read_csv("data.csv")
```

---

## Check dataset

```python
df.head()
df.info()
df.describe()
df.shape
```

---

## Check missing values

```python
df.isna().sum()
```

---

## Select features

```python
X = df[["Age", "Height", "Weight"]]
```

---

## Select target

```python
y = df["Result"]
```

Usually:

```text
X → Features / Inputs
y → Target / Output
```

---

## Remove unwanted columns

```python
df = df.drop(
    columns=["ID", "Name"]
)
```

---

# 44. Important Functions to Remember

## ⭐⭐⭐⭐⭐ Must Know

These are the functions you should know extremely well.

### Creating data

```python
pd.Series()
pd.DataFrame()
```

### Reading data

```python
pd.read_csv()
pd.read_excel()
pd.read_json()
```

### Inspecting

```python
df.head()
df.tail()
df.info()
df.describe()
df.shape
df.columns
df.dtypes
```

### Selecting

```python
df["column"]
df[["column1", "column2"]]
df.loc[]
df.iloc[]
```

### Filtering

```python
df[df["Age"] > 20]
```

### Cleaning

```python
df.drop()
df.dropna()
df.fillna()
df.replace()
df.drop_duplicates()
```

### Aggregation

```python
df.mean()
df.sum()
df.min()
df.max()
df.count()
df.median()
df.std()
```

### Grouping

```python
df.groupby()
df.agg()
```

### Unique values

```python
df.unique()
df.nunique()
df.value_counts()
```

### Sorting

```python
df.sort_values()
```

### Combining

```python
pd.merge()
pd.concat()
df.join()
```

### Data types

```python
df.astype()
pd.to_numeric()
pd.to_datetime()
```

### String operations

```python
df["Name"].str.lower()
df["Name"].str.upper()
df["Name"].str.strip()
df["Name"].str.contains()
```

---

# 45. Typical Pandas Workflow

This is a very important pattern to remember.

```python
import pandas as pd

# 1. Read data
df = pd.read_csv("sample.csv")

# 2. Inspect data
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# 3. Check missing values
print(df.isna().sum())

# 4. Remove unnecessary columns
df = df.drop(
    columns=["No"]
)

# 5. Handle missing values
df["Type2"] = df["Type2"].fillna("None")

# 6. Fix inconsistent values
df["Type1"] = df["Type1"].replace({
    "Grass": "GRASS"
})

# 7. Standardize text
df["Name"] = df["Name"].str.lower()

# 8. Remove duplicates
df = df.drop_duplicates()

# 9. Filter data
result = df[df["Height"] > 1]

# 10. Group data
grouped = df.groupby("Type1")["Height"].mean()

# 11. Sort data
sorted_df = df.sort_values(
    "Height",
    ascending=False
)

# 12. Save cleaned data
df.to_csv(
    "cleaned_data.csv",
    index=False
)

1. Read CSV
import pandas as pd

df = pd.read_csv("sample.csv")
2. Select a column
df["ColumnName"]
Example:
df["Weight"]
3. Select multiple columns
df[["Column1", "Column2"]]
Example:
df[["Name", "Weight"]]
4. Filter rows — VERY IMPORTANT
One condition
df[df["ColumnName"] > value]
Example:
df[df["Weight"] > 50]
Equal to
df[df["Type1"] == "Fire"]
Not equal
df[df["Type1"] != "Fire"]
Less than
df[df["Height"] < 1]
5. Multiple conditions
AND → &
df[(df["Column1"] > value) & (df["Column2"] > value)]
Example:
df[(df["Height"] > 1) & (df["Weight"] > 50)]
OR → |
df[(df["Type1"] == "Fire") | (df["Type1"] == "Water")]
⚠️ Put each condition inside parentheses.
6. loc — select using labels/conditions
df.loc[condition, "ColumnName"]
Example:
df.loc[df["Weight"] > 50, "Name"]
Multiple columns:
df.loc[df["Weight"] > 50, ["Name", "Weight"]]
7. iloc — select using positions
df.iloc[row_position, column_position]
Examples:
df.iloc[0]
df.iloc[0:5]
df.iloc[0:5, 0:3]
8. Sort data
Ascending
df.sort_values("ColumnName")
Descending
df.sort_values("ColumnName", ascending=False)
Example:
df.sort_values("Weight", ascending=False)
9. Find unique values
df["ColumnName"].unique()
Number of unique values:
df["ColumnName"].nunique()
10. Missing values
Check:
df.isna()
Count missing values:
df.isna().sum()
Remove missing rows:
df.dropna()
Fill missing values:
df["ColumnName"].fillna(value)
Example:
df["Type2"] = df["Type2"].fillna("None")
11. Remove duplicates
df.drop_duplicates()
12. Add a new column
df["NewColumn"] = value
Example:
df["DoubleWeight"] = df["Weight"] * 2
13. Delete a column
df.drop("ColumnName", axis=1)
Or permanently:
df.drop("ColumnName", axis=1, inplace=True)
14. Rename columns
df.rename(columns={"OldName": "NewName"}, inplace=True)
15. groupby() — VERY IMPORTANT
General syntax:
df.groupby("ColumnName")["ValueColumn"].function()
Example:
df.groupby("Type1")["Weight"].mean()
Other functions:
.sum()
.mean()
.max()
.min()
.count()
16. value_counts() — VERY COMMON
df["ColumnName"].value_counts()
Example:
df["Type1"].value_counts()
This tells you how many times each value occurs.
17. Aggregation
df.groupby("ColumnName")["ValueColumn"].agg(["mean", "max", "min"])
Example:
df.groupby("Type1")["Weight"].agg(["mean", "max", "min"])

⭐ Most Important Interview Pattern
When you see a question like:
"Find all Pokémon whose height is greater than 1 and weight is greater than 50."
Think:
df[(df["Height"] > 1) & (df["Weight"] > 50)]
When you see:
"Find average weight for each Type1."
Think:
df.groupby("Type1")["Weight"].mean()
When you see:
"Find the 5 heaviest Pokémon."
Think:
df.sort_values("Weight", ascending=False).head(5)
When you see:
"Find the number of Pokémon in each Type1."
Think:
df["Type1"].value_counts()
These patterns are much more important for interviews than memorizing individual questions.
df = pd.read_csv("sample.csv")

pokemon_select=df[['Height'>1] and ['Weight'>50]]

