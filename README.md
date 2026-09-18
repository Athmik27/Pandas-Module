#  Pandas Module

Pandas is a Python library used for **data manipulation and data analysis**.

It works closely with **NumPy, Matplotlib, and Seaborn**.

```python
import pandas as pd
```

---

## 1. Series

A Series is a **one-dimensional labeled array**.

```python
data = [10, 20, 30, 40]

s = pd.Series(data)

print(s)
```

With custom index:

```python
s = pd.Series(
    [10, 20, 30],
    index=["A", "B", "C"]
)
```

---

## 2. DataFrame

A DataFrame is a **two-dimensional table** with rows and columns.

```python
data = {
    "Name": ["Pikachu", "Charmander", "Squirtle"],
    "Height": [0.4, 0.6, 0.5],
    "Weight": [6, 8.5, 9]
}

df = pd.DataFrame(data)

print(df)
```

---

## 3. Read CSV

```python
df = pd.read_csv("sample.csv")

print(df)
```

Using a column as index:

```python
df = pd.read_csv(
    "sample.csv",
    index_col="Name"
)
```

---

## 4. View Data

First 5 rows:

```python
df.head()
```

Last 5 rows:

```python
df.tail()
```

Specific number of rows:

```python
df.head(10)
```

---

## 5. Basic Information

```python
df.info()
```

Shows:

* Column names
* Data types
* Number of non-null values
* Memory usage

---

## 6. Statistical Summary

```python
df.describe()
```

Provides:

* Count
* Mean
* Standard deviation
* Minimum
* Maximum

---

## 7. Selecting Columns

Select one column:

```python
df["Height"]
```

Select multiple columns:

```python
df[["Name", "Height", "Weight"]]
```

---

## 8. Selection Using `loc`

`loc` is used for **label-based selection**.

```python
df.loc["Caterpie"]
```

Multiple rows:

```python
df.loc[["Caterpie", "Metapod"]]
```

Specific columns:

```python
df.loc[
    "Caterpie",
    ["Height", "Weight"]
]
```

---

## 9. Selection Using `iloc`

`iloc` is used for **position-based selection**.

```python
df.iloc[0]
```

First three rows:

```python
df.iloc[0:3]
```

---

## 10. Filtering

Filtering means keeping rows that match a condition.

```python
tall_pokemon = df[df["Height"] >= 1]

print(tall_pokemon)
```

Multiple conditions:

```python
result = df[
    (df["Height"] >= 1) &
    (df["Weight"] >= 50)
]
```

OR condition:

```python
result = df[
    (df["Height"] >= 1) |
    (df["Weight"] >= 50)
]
```

---

## 11. Sorting

Sort by a column:

```python
df.sort_values("Weight")
```

Descending order:

```python
df.sort_values(
    "Weight",
    ascending=False
)
```

---

## 12. Missing Values

Check missing values:

```python
df.isna()
```

Count missing values:

```python
df.isna().sum()
```

---

## 13. Remove Missing Values

Remove rows containing missing values:

```python
df.dropna()
```

Remove missing values from a specific column:

```python
df.dropna(
    subset=["Type2"]
)
```

---

## 14. Fill Missing Values

```python
df["Type2"] = df["Type2"].fillna("None")
```

Using a dictionary:

```python
df.fillna({
    "Type2": "None"
})
```

---

## 15. Remove Columns

```python
df.drop(
    columns=["Type2"]
)
```

Modify the original DataFrame:

```python
df.drop(
    columns=["Type2"],
    inplace=True
)
```

---

## 16. Rename Columns

```python
df.rename(
    columns={
        "Height": "Pokemon_Height"
    }
)
```

---

## 17. Replace Values

Replace a value:

```python
df["Type1"] = df["Type1"].replace(
    "Firee",
    "Fire"
)
```

Multiple replacements:

```python
df["Type1"] = df["Type1"].replace({
    "Firee": "Fire",
    "Watter": "Water"
})
```

---

## 18. Data Types

Check data types:

```python
df.dtypes
```

Convert data type:

```python
df["Weight"] = df["Weight"].astype(float)
```

---

## 19. Unique Values

Get unique values:

```python
df["Type1"].unique()
```

Count unique values:

```python
df["Type1"].nunique()
```

Count each value:

```python
df["Type1"].value_counts()
```

---

## 20. Aggregation

Common aggregation functions:

```python
df["Weight"].sum()

df["Weight"].mean()

df["Weight"].median()

df["Weight"].min()

df["Weight"].max()

df["Weight"].std()
```

---

## 21. GroupBy

Used to **group data based on a category**.

```python
df.groupby("Type1")["Weight"].mean()
```

Multiple aggregations:

```python
df.groupby("Type1")["Weight"].agg(
    ["mean", "max", "min"]
)
```

---

## 22. `agg()`

Used to perform multiple aggregation operations.

```python
df["Weight"].agg(
    ["mean", "max", "min", "sum"]
)
```

---

## 23. Apply Function

Apply a function to a column:

```python
df["Weight"] = df["Weight"].apply(
    lambda x: x * 2
)
```

---

## 24. Creating a New Column

```python
df["Weight_kg"] = df["Weight"] / 1000
```

---

## 25. Delete a Column

```python
del df["Weight_kg"]
```

---

## 26. Index

Default index:

```text
0
1
2
3
4
```

Set a column as index:

```python
df.set_index("Name")
```

Reset index:

```python
df.reset_index()
```

---

## 27. DataFrame Shape

```python
df.shape
```

Example:

```text
(800, 7)
```

Means:

```text
800 → rows
7   → columns
```

---

## 28. Number of Rows

```python
len(df)
```

or:

```python
df.shape[0]
```

---

## 29. Number of Columns

```python
df.shape[1]
```

---

## 30. Checking Conditions

```python
df["Height"] > 1
```

Example:

```python
df[df["Legendary"] == 1]
```

---

## 31. Concatenation

Combine DataFrames:

```python
pd.concat(
    [df1, df2]
)
```

---

## 32. Merge

Combine DataFrames using a common column:

```python
pd.merge(
    df1,
    df2,
    on="Name"
)
```

---

## 33. Read Other Files

CSV:

```python
pd.read_csv("data.csv")
```

Excel:

```python
pd.read_excel("data.xlsx")
```

JSON:

```python
pd.read_json("data.json")
```

---

## 34. Save Data

Save as CSV:

```python
df.to_csv(
    "output.csv",
    index=False
)
```

Save as Excel:

```python
df.to_excel(
    "output.xlsx",
    index=False
)
```

---

## 35. Data Cleaning

Data cleaning means **removing or fixing incorrect, incomplete, duplicate, or inconsistent data**.

Common operations:

```text
dropna()
fillna()
drop()
replace()
drop_duplicates()
astype()
```

---

## 36. Duplicate Values

Check duplicates:

```python
df.duplicated()
```

Remove duplicates:

```python
df.drop_duplicates()
```

---

## 37. Important Pandas Functions

| Function               | Use                      |
| ---------------------- | ------------------------ |
| `pd.Series()`          | Create Series            |
| `pd.DataFrame()`       | Create DataFrame         |
| `pd.read_csv()`        | Read CSV                 |
| `df.head()`            | First rows               |
| `df.tail()`            | Last rows                |
| `df.info()`            | Data information         |
| `df.describe()`        | Statistical summary      |
| `df.loc[]`             | Label-based selection    |
| `df.iloc[]`            | Position-based selection |
| `df.sort_values()`     | Sort data                |
| `df.isna()`            | Find missing values      |
| `df.dropna()`          | Remove missing values    |
| `df.fillna()`          | Fill missing values      |
| `df.drop()`            | Remove rows/columns      |
| `df.replace()`         | Replace values           |
| `df.groupby()`         | Group data               |
| `df.agg()`             | Aggregation              |
| `df.apply()`           | Apply function           |
| `df.merge()`           | Merge DataFrames         |
| `pd.concat()`          | Combine DataFrames       |
| `df.drop_duplicates()` | Remove duplicates        |

---

# CHEAT SHEET

```python
import pandas as pd

df = pd.read_csv("sample.csv")

df.head()
df.tail()

df.info()
df.describe()

df["Height"]
df[["Name", "Height", "Weight"]]

df.loc["Caterpie"]
df.iloc[0]

df[df["Height"] >= 1]

df.sort_values("Weight")
df.sort_values("Weight", ascending=False)

df.isna()
df.isna().sum()

df.dropna()
df.fillna({"Type2": "None"})

df.drop(columns=["Type2"])

df["Type1"].unique()
df["Type1"].nunique()
df["Type1"].value_counts()

df["Weight"].mean()
df["Weight"].sum()
df["Weight"].min()
df["Weight"].max()

df.groupby("Type1")["Weight"].mean()

df.drop_duplicates()

df.shape

df.to_csv("output.csv", index=False)
```


