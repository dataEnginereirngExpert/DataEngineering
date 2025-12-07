from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# --------------------------------------
# CREATE SPARK SESSION
# --------------------------------------
spark = SparkSession.builder \
    .appName("MyPySpark") \
    .master("local[*]") \
    .getOrCreate()

print("Spark Session Created Successfully!")

# --------------------------------------
# SAMPLE DATA (in Python list)
# --------------------------------------
data = [
    ("Uttam", "Engineering", 90000),
    ("Amit", "Finance", 75000),
    ("John", "Engineering", 82000),
    ("Mary", "HR", 65000)
]

columns = ["name", "dept", "salary"]

# --------------------------------------
# CREATE DATAFRAME
# --------------------------------------
df = spark.createDataFrame(data, columns)

print("\n=== Original DataFrame ===")
df.show()

# --------------------------------------
# TRANSFORMATION: FILTER + ADD BONUS
# --------------------------------------
df2 = df.filter(col("salary") > 70000) \
        .withColumn("bonus", col("salary") * 0.10)

print("\n=== Filtered DataFrame (Salary > 70000) with Bonus ===")
df2.show()

# --------------------------------------
# GROUPING: AVERAGE SALARY BY DEPARTMENT
# --------------------------------------
df3 = df.groupBy("dept").avg("salary")

print("\n=== Average Salary by Department ===")
df3.show()

# --------------------------------------
# STOP SPARK SESSION
# --------------------------------------
spark.stop()
print("\nSpark Session Stopped.")
