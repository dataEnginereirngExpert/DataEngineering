import pandas as pd

# Creating a Series : It  is like a single column of data.
s = pd.Series([10, 20, 30, 40])
print(s)

# Creating a DataFrame : It is like an Excel sheet — rows and columns of data.
df = pd.DataFrame({
    "name": ["Amit", "Riya", "John"],
    "age": [25, 30, 28]
})

print(df)

df1 = pd.read_csv("employees.csv")
print(df1.head())        # first 5 rows
print(df1.shape)         # (rows, columns)
print(df1.describe())    # stats for numeric columns