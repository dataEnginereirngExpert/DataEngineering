import pandas as pd

df = pd.read_csv("employees.csv")

print(df.head())       # first 5 rows
print(df.shape)        # rows, columns
print(df.describe())   # stats (salary, age)
print(df.columns)      # column names

#employees older than 30
filtered_df = df[df["age"] > 30]
print(filtered_df)

#Engineering department only
eng = df[df["department"] == "Engineering"]
print(eng)

#Sort by salary (descending):
sorted_df = df.sort_values(by="salary", ascending=False)
print(sorted_df)

#Sort by age (ascending):
print(df.sort_values("age"))

#Convert salary to lakhs
df["salary_lakhs"] = df["salary"] / 100000
print(df.head())

#count employees per department
count_dept = df.groupby("department")["id"].count()
print(count_dept)

#max and min Salary
print(df["salary"].max())
print(df.loc[df["salary"].idxmax()])

df.to_csv("employees_output.csv", index=False)