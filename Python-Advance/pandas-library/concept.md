# Pandas Library — Major Usable Functions

Pandas is a powerful Python library used for **data manipulation, cleaning, transformation, and analysis**.  
It provides two main data structures:

- **Series** → 1-D labeled array  
- **DataFrame** → 2-D tabular data (like an Excel sheet)

---

## 1. Reading & Writing Data (I/O Functions)

### Read
```python
pd.read_csv("file.csv")
pd.read_excel("file.xlsx")
pd.read_json("file.json")
pd.read_sql(query, connection)


### Write
```python
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", index=False)
df.to_json("output.json")

### Exploring Data
```python
df.head()
df.tail()
df.info()
df.describe()

### Selecting Columns & Rows
```python
df["column"]
df[["col1", "col2"]]

df.loc[5]           # label-based
df.iloc[5]          # index-based
df.loc[0:10]        # range by label
df.iloc[0:10]       # range by index

### Filtering / Querying Data
```python
df[df["age"] > 30]
df[(df["age"] > 30) & (df["city"] == "Delhi")]

df.query("age > 30 and city == 'Delhi'")


### Creating & Modifying Columns
```python
df["total"] = df["qty"] * df["price"]
df["age"] = df["age"] + 1
df["name_len"] = df["name"].apply(len) ```

### Merge (SQL JOIN)
```python
pd.merge(df1, df2, on="id", how="inner")
pd.merge(df1, df2, on="id", how="left")

df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

df.drop_duplicates()
df.drop_duplicates(subset=["email"])```