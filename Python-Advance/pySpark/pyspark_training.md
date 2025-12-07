# 1. Introduction to Apache Spark & PySpark

Apache Spark is a distributed data processing engine used to handle **large-scale data workloads**.  
PySpark is its **Python API**, enabling Python developers to write distributed ETL pipelines.

### Why PySpark?
- Processes TB–PB scale data  
- Fast in-memory computation  
- Ideal for data engineering pipelines  
- Supports SQL, streaming, ML  

---

# 2. SparkSession

###  What is SparkSession?
SparkSession is the entry point to PySpark.  
It allows you to create DataFrames, run SQL, read files, and access cluster resources.

###  Important Statements
```python
from pyspark.sql import SparkSession
spark = SparkSession.builder     .appName("TrainingSession")     .master("local[*]")     .getOrCreate()
```

### What These Do:
- `.appName("TrainingSession")` → Names the Spark application  
- `.master("local[*]")` → Runs Spark using all CPU cores on your machine  
- `.getOrCreate()` → Creates a session or returns existing one  

### Sample Program
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder     .appName("SparkBasics")     .master("local[*]")     .getOrCreate()

print("Spark Session Created!")
```

---

# 3. Creating Spark DataFrames

### What is a DataFrame?
A distributed table with rows and columns (similar to Pandas, but scalable).

### Ways to Create DataFrames
1. From Python lists/dictionaries  
2. From CSV/JSON/Parquet  
3. From Pandas DataFrame  

---

## 3.1 Creating DataFrame from Python List

### Statements:
```python
data = [("Uttam", "Engineering", 90000), ("Amit", "Finance", 80000)]
df = spark.createDataFrame(data, ["name", "dept", "salary"])
df.show()
```

### What These Do:
- `spark.createDataFrame()` → converts Python list to distributed DataFrame  
- `.show()` → displays the data  

### Sample Program
```python
data = [
    ("John", "IT", 70000),
    ("Mary", "HR", 65000)
]

df = spark.createDataFrame(data, ["name", "dept", "salary"])
df.show()
```

---

## 3.2 Creating DataFrame from CSV/JSON/Parquet

### Statements:
```python
df = spark.read.csv("employees.csv", header=True, inferSchema=True)
```

### What These Do:
- `spark.read.csv()` → reads CSV file  
- `header=True` → first row contains column names  
- `inferSchema=True` → auto-detects data types  

### Sample Program
```python
df = spark.read.csv("employees.csv", header=True, inferSchema=True)
df.printSchema()
df.show()
```

---

# 4. Transformations & Actions

Spark uses **lazy evaluation**:  
Transformations do NOT execute until an Action triggers the job.

---

## 4.1 Transformations (Do NOT execute immediately)

### Common Transformations + Explanation
| Transformation | What It Does |
|----------------|--------------|
| `select()` | Choose specific columns |
| `filter()` | Filter rows based on conditions |
| `withColumn()` | Add or update a column |
| `groupBy()` | Group rows for aggregation |
| `orderBy()` | Sort data |
| `join()` | Join two DataFrames |

### ✔ Sample Program
```python
from pyspark.sql.functions import *

df = spark.read.csv("employees.csv", header=True, inferSchema=True)

df2 = df.filter(df.salary > 50000)         .withColumn("bonus", df.salary * 0.10)         .select("name", "salary", "bonus")

df2.show()
```

---

## 4.2 Actions (Trigger Execution)

### Common Actions
| Action | What It Does |
|--------|--------------|
| `show()` | Displays DataFrame |
| `count()` | Returns row count |
| `collect()` | Retrieves all rows to driver *(dangerous on big data)* |
| `take(n)` | Gets first n rows |
| `write` | Saves the DataFrame |

### ✔ Sample Program
```python
df = spark.read.csv("employees.csv", header=True, inferSchema=True)

print("Total rows:", df.count())
df.show(3)
```

---

# 5. Integration with Pandas

Use Pandas only for **small datasets**.

---

## 5.1 Convert Spark DF → Pandas

### Statement:
```python
pdf = df.toPandas()
```

### Explanation:
Pulls distributed data into local memory (driver machine).  
Use only for sampling or small data.

### ✔ Sample Program
```python
sample_pdf = df.limit(5).toPandas()
print(sample_pdf)
```

---

## 5.2 Convert Pandas → Spark

### Statement:
```python
sdf = spark.createDataFrame(pdf)
```

### ✔ Sample Program
```python
import pandas as pd

pdf = pd.DataFrame({"name": ["A", "B"], "age": [25, 30]})
sdf = spark.createDataFrame(pdf)
sdf.show()
```

---

# 6. Hands-On Project 1: Word Count in PySpark

### Problem
Count the occurrences of each word in a text file.

### Statements Used
| Statement | What It Does |
|----------|----------------|
| `spark.read.text()` | Reads text file line by line |
| `split()` | Splits lines into arrays of words |
| `explode()` | Converts array into individual rows |
| `groupBy().count()` | Performs aggregation |

---

### ✔ Full Program
```python
from pyspark.sql.functions import *

text = spark.read.text("sample.txt")

words = text.select(explode(split(col("value"), " ")).alias("word"))

word_count = words.groupBy("word").count()

word_count.show()
```

---

# 7. Hands-On Project 2: Aggregate CSV using Spark DataFrame

### ✔ Problem
Read a sales CSV and calculate total sales per region.

### ✔ Statements Used
| Statement | What It Does |
|----------|----------------|
| `read.csv()` | Read CSV file |
| `groupBy()` | Group by region |
| `sum()` | Aggregates values |
| `write.csv()` | Save results |

---

### ✔ Full Program
```python
from pyspark.sql.functions import *

df = spark.read.csv("sales.csv", header=True, inferSchema=True)

result = df.groupBy("region").agg(
    sum("amount").alias("total_sales")
)

result.show()

result.write.csv("output_sales", header=True)
```

---

# 8. PySpark in Data Engineering Pipelines

Data engineering pipelines typically follow **ETL**:

---

## ✔ Extract
Read data from sources such as S3, ADLS, HDFS, RDBMS, Kafka.

### Example:
```python
df = spark.read.csv("s3://raw/customer.csv", header=True)
```

---

## ✔ Transform
Clean, filter, dedupe, join, aggregate, or apply business logic.

### Example:
```python
df_clean = df.filter(df.status == "ACTIVE")              .withColumn("load_ts", current_timestamp())
```

---

## ✔ Load
Write curated data to Parquet, Delta, S3, Snowflake, etc.

### Example:
```python
df_clean.write.parquet("s3://clean/customer/")
```

---

# 9. Best Practices for Associate Data Engineers

- Prefer **DataFrames over RDDs**  
- Never use `collect()` for large datasets  
- Use **Parquet/Delta** instead of CSV  
- Partition large datasets  
```python
df.write.partitionBy("year", "month").parquet("s3://path/")
```
- Cache only when reused  
```python
df.cache()
```

### Library Insnallation 
- Install OpenJDK 11 
- Install pip install pyspark==3.4.1
- 


---
