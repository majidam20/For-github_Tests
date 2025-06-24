https://sparkbyexamples.com/pyspark-tutorial/
https://spark.apache.org/docs/latest/rdd-programming-guide.html

###In chatgpt:
important pyspark python codes

from pyspark import SparkContext
from pyspark import *
from pyspark.sql import *

#sc   = SparkContext.getOrCreate()
#from pyspark import SparkConf, SparkContext
#conf = SparkConf().setAppName("PySpark App").setMaster("spark://master:7077")
#sc   = SparkContext(conf=conf)

#conf = SparkConf().setAppName(appName).setMaster(master)
#sc   = SparkContext(conf=conf)

sc = SparkContext("local", "App Name")

spark = SparkSession(sc)

rdd = spark.read.text(pathData +"a.xml")
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from pyspark import SparkContext
logFile = "file:///home/hadoop/spark-2.1.0-bin-hadoop2.7/README.md"  
sc = SparkContext("local", "first app")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print "Lines with a: %i, lines with b: %i" % (numAs, numBs)
+++++++++++++++++++++++++++++++++++++++++++++++++
words=sc.parallelize (["scala","sss"])
words.collect(); words.count(); words.cache(); 
words_filter = words.filter(lambda x: 'spark' in x)
filtered = words_filter.collect()

words_map = words.map(lambda x: (x, 1))
mapping = words_map.collect()

nums = sc.parallelize([1, 2, 3, 4, 5])
adding = nums.reduce(add)

x = sc.parallelize([("spark", 1), ("hadoop", 4)])
y = sc.parallelize([("spark", 2), ("hadoop", 5)])
joined = x.join(y)
final = joined.collect()
+++++++++++++++++++++++++++++++++++++++++++++
from pyspark import SparkContext
from pyspark import SparkFiles
finddistance = "/home/hadoop/examples_pyspark/finddistance.R"
finddistancename = "finddistance.R"
sc = SparkContext("local", "SparkFile App")
sc.addFile(finddistance)
++++++++++++++++++++++++++++++++++++++++++++++++
StorageLevel decides how RDD should be stored. In Apache Spark, StorageLevel decides whether RDD should be stored in the memory or should it be stored over the disk, or both. It also decides whether to serialize RDD and whether to replicate RDD partitions.
rdd1 = sc.parallelize([1,2], NumberOf_partitions)
rdd1.persist( pyspark.StorageLevel.MEMORY_AND_DISK_2 )
rdd1.getStorageLevel()
+++++++++++++++++++++++++++++++++++++++++++++++++
textFile = spark.read.text("README.md")
textFile.count()  # Number of rows in this DataFrame
textFile.first()
linesWithSpark = textFile.filter(textFile.value.contains("Spark"))

from pyspark.sql import functions as sf
textFile.select(sf.size(sf.split(textFile.value, "\s+")).name("numWords")).agg(sf.max(sf.col("numWords"))).collect()

wordCounts = textFile.select(sf.explode(sf.split(textFile.value, "\s+")).alias("word")).groupBy("word").count()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
distFile = sc.textFile("data.txt")
distFile.map(lambda s: len(s)).reduce(lambda a, b: a + b)
+++++++++++++++++++++++++++++++++++++++++++
df.select('CustomerID').distinct().count()
df.groupBy('Country').agg(countDistinct('CustomerID').alias('country_count')).show()

spark.sql("set spark.sql.legacy.timeParserPolicy=LEGACY")
df = df.withColumn('date',to_timestamp("InvoiceDate", 'yy/MM/dd HH:mm'))
df.select(max("date")).show()
df2 = df2.join(df2.groupBy('CustomerID').agg(max('recency').alias('recency')),on='recency',how='leftsemi')

spark = SparkSession.builder.getOrCreate()  
df = spark.sql('''select 'spark' as hello ''')  
df.show()

songdf.select("Genre").show()  
songdf.filter(songdf["Genre"]=="pop").show() 
df.filter(df.quantity > 20)

df = spark.read.csv("path/to/your/file.csv", header=True, inferSchema=True)
daily_metrics_df.write.mode("overwrite").parquet(daily_metrics_output_path)

student = sqlContext.read.parquet("...")  
department = sqlContext.read.parquet("...")  
student.filter(marks > 55).join(department, student.student_Id == department.id).groupBy(student.name, "gender")

df.dropna(how="any", subset=["column_name"])

df = spark.createDataFrame(df_pd)  

df = spark.sparkContext.parallelize([(12, 20, 35, 'a b c'),(41, 58, 64, 'd e f'), (70, 85, 90, 'g h i')]).toDF(['col1', 'col2', 'col3','col4']) 

df.write.parquet(parquet_file_path)

# Add a new calculated column
df_with_new_column = df.withColumn("revenue", df.quantity * df.price)


from pyspark.sql.window import Window
from pyspark.sql.functions import *
from pyspark.sql import functions as F
# Create a window specification
window_spec = Window.partitionBy("department").orderBy(F.desc("salary"))
# Calculate the rank of employees within each department based on salary
employee_salary.withColumn("rank", F.rank().over(window_spec)).show()

df = df.withColumn("gender",when(col("gender").equalTo("M"),lit("Male"))
                           .when(col("gender").equalTo("F"),lit("Female"))
                           .otherwise(lit("")))
                           
df = df.withColumnRenamed("gender","gender/sex")  

+++++++++++++++++++++++++++++++++++++++++++++++++++++
from pyspark.sql.types import StringType, ArrayType
distinctDF = df.distinct()
df2 = df.dropDuplicates()
dropDisDF = df.dropDuplicates(["department","salary"])
++++++++++++++++++++++++++++++++++++++++++++++++++++++
schema = StructType([
    StructField("artist_id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("albums", ArrayType(StructType([
        StructField("album_id", IntegerType(), True),
        StructField("name", StringType(), True),
        StructField("year_released", IntegerType(), True)
    ])), True)
])
parsed_df = df2.withColumn("parsed_json", from_json(col("unencoded_base64"), schema))

flattened = parsed_df.select(col("parsed_json.artist_id"), col("parsed_json.name"), explode(col("parsed_json.albums")))

flattened_with_albums = flattened.select(col("artist_id"), col("name"), col("col.album_id"), col("col.name").alias("album_name") , col("col.year_released"))
display(flattened_with_albums)

++++++++++++++++++++++++++++++++
from pyspark.sql.functions import col, to_date

# Convert column types
df_transformed = df_raw.withColumn("sale_amount", col("sale_amount").cast("double")) \
                       .withColumn("sale_date", to_date(col("sale_date"), "yyyy-MM-dd"))

++++++++++++++++++++++++++++++++++++++
df.cache()  # Keep DataFrame in memory for faster access
df.count()  # Trigger cache

df.write.partitionBy("state").parquet("output/")
df.write.bucketBy(4, "state").saveAsTable("bucketed_t )  
++++++++++++++++++++++++++++++++++
# Initialize Spark Session
spark = SparkSession.builder.appName("MapReduceExample").getOrCreate()
sc = spark.sparkContext  # Get the SparkContext

# Sample text data
data = ["hello world", "hello spark", "hello pyspark"]

# Parallelize the data into an RDD
rdd = sc.parallelize(data)

# MapReduce Process
word_counts = (rdd
    .flatMap(lambda line: line.split(" "))   # Map: Split lines into words
    .map(lambda word: (word, 1))             # Map: Assign count 1 to each word
    .reduceByKey(lambda a, b: a + b)         # Reduce: Sum counts for each word
)

# Collect and print results
print(word_counts.collect())
++++++++++++++++++++++++++++++++++++++++++++++ 


✅ Want to run MapReduce on a large dataset (Parquet, CSV, JSON)?
✅ Need to orchestrate MapReduce jobs using Airflow, AWS Glue, or Databricks?
✅ Want performance optimization techniques for PySpark MapReduce?  

# Use SQL-style aggregation instead of RDD MapReduce
result = df.groupBy("category").sum("sales")
result.show()
✅ Better performance than RDD MapReduce due to Catalyst Optimizer.                 

rdd.mapPartitions(lambda partition: (expensive_function(x) for x in partition))
🔹 Processes multiple records at once, reducing function call overhead.

 Slow Approach (groupByKey())

rdd = sc.parallelize([("apple", 1), ("banana", 1), ("apple", 1)])
result = rdd.groupByKey().map(lambda x: (x[0], sum(x[1])))  # BAD: High shuffle cost
print(result.collect())
✅ Optimized Approach (reduceByKey())


rdd = sc.parallelize([("apple", 1), ("banana", 1), ("apple", 1)])
result = rdd.reduceByKey(lambda a, b: a + b)  # GOOD: Reduces before shuffle
print(result.collect())
🔹 reduceByKey() improves performance by reducing shuffle data.

The persist() function in Apache Spark is used to store an RDD or DataFrame in memory (or disk) across multiple actions, preventing recomputations and improving performance.


🔹 Feature	  groupByKey()	                            reduceByKey()
Function	  Groups values by key	                    Aggregates values by key using a function
Shuffle Cost  High (sends all values across nodes)	    Optimized (reduces data before shuffle)
Performance	  Slow for large data (high memory usage)	Faster (less memory & optimized network traffic)
Use Case	  When you need all values per key	        When you need aggregated results per key


from pyspark.sql.functions import broadcast
df1.join(broadcast(df2), "id")  # Faster join


🔹 Use repartition(n) to increase partitions (expensive shuffle).
repartition(number): Changes the physical number of partitions, distributing data randomly/round-robin.
repartition(column_name_string): Partitions based on the hash of the specified column's values, using default number of partitions.
repartition(number, column_name_string)

🔹 Use coalesce(n) to decrease partitions (cheaper operation).

df.write.partitionBy("category").parquet("output/")  # Efficient partitioning
🔹 Speeds up queries by reducing unnecessary scans.
+++++++++++++++++++++++++++++++++++++++++++++++++++++
@pytest.fixture
def sample_data(spark):
    # Create a sample dataset for testing
    schema = StructType([
        StructField("timestamp", TimestampType(), True),
        StructField("vehicle_id", StringType(), True),
        StructField("temperature", DoubleType(), True),
        StructField("position", StructType([
            StructField("x", DoubleType(), True),
            StructField("y", DoubleType(), True),
            StructField("z", DoubleType(), True)
        ]), True)
    ])
Practically tested+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Add a Quality Check Status Column
df = df.withColumn("Quality_Check", F.lit("Passed"))

# Add a Transformed Time Column
df = df.withColumn("Transformed_Time", current_timestamp())
# Fix "Count_date" Date Format
df = df.withColumn(
    "Count_date",
    F.to_date(F.to_timestamp(F.col("Count_date"), "M/d/yyyy H:mm"))  # Flexible format for 1 or 2 digits
)
 df_veh = df.withColumn('Vehicle_Intensity',
               col('Motor_Vehicles_Count') / col('Link_length_km')
               )

# Both are correct:
print("--- Using col('sale') ---")
df.withColumn("sale", col("sale") + 1).show()

print("\n--- Using df.sale ---")
df.withColumn("sale", df.sale + 1).show()

from pyspark.sql.functions import *
df.filter(col('sale')==1).show()
df.filter(df['sale']==1).show(5)
df.select(col('sale')).show(5)
df.select('sale').show(5)
df.select("Department").distinct()
df.select('sale_date').dropna().show()
df.dropna(subset=["name"])
df.fillna({"name": "Unknown"})
col("prev_position").isNotNull()
df_nulls = df.filter(col("prev_position").isNull())
df.withColumnRenamed("age", "years_old")
df_renamed = df.selectExpr("id", "name as full_name", "age as years_old")
df.withColumnRenamed("old_column", "new_column")  # ❌ This does not modify df in place, so we muss reassign it
df= df.withColumnRenamed("old_column", "new_column")## ✅ Apply changes on df
df.withColumn("sale", df.sale +1).show()
%%sql
select * from dbcatalog1.cls1_mobile_code_challenge_de_csv limit 10
spark.sql('select * from dbcatalog1.cls1_mobile_code_challenge_de_csv limit 10').show()
# Data Cleaning: Apply data cleaning and transformation operations
cleaned_df = df.withColumn("cleaned_column", regexp_replace(col("column"), "[^a-zA-Z0-9]", ""))

# ❌ Inefficient: Avoid using Python loops for row-wise operations
for row in df.collect():
    row['age_category'] = "Adult" if row["user_age"] > 25 else "Young"

# ✅ Efficient: Use PySpark functions instead of Python loops
from pyspark.sql.functions import when

df = df.withColumn("age_category", when(df.user_age > 25, "Adult").otherwise("Young"))
df.show()
df1.intersect(df2)# similarity two dfs
df1.except(df2)# diferences of two dfs
df.coalesce(1)# reduce partiotions of a df
df.withColumn('rank, row_number().over(window.partitionBy('c1').orderBy('c2')))
df.groupBy("category").agg(F.sum("sales"))
df.groupBy("category").sum("sales")
+++++++++++++++++++++++++++++++++++++++++++++
In PySpark, the reduceByKey() operation is typically used on RDDs, not DataFrames. However, I can show you how to convert a DataFrame to an RDD and then apply reduceByKey() to perform aggregations, such as summing values for each key.

df = spark.createDataFrame(data, ["category", "amount"])

# Convert DataFrame to RDD and apply reduceByKey
rdd = df.rdd
reduced_rdd = rdd.map(lambda x: (x[0], x[1])) \
                 .reduceByKey(lambda a, b: a + b)

# Collect and print the result
result = reduced_rdd.collect()
for category, total_amount in result:
    print(f"Category: {category}, Total Amount: {total_amount}")
    
    
###If you prefer a pure DataFrame-based solution, you can achieve the same result using groupBy and sum():

df.groupBy("category").sum("amount").show()
++++++++++++++++++++++++++++++++
df_left_join = df1.join(df2, on="id", how="left")

SELECT t1.*
FROM table1 t1
LEFT JOIN table2 t2 ON t1.common_column = t2.common_column
WHERE t2.common_column IS NULL;
++++++++++++++++++++++++++++++++++++++++
in PySpark, shuffle happens when data needs to be redistributed across partitions. This occurs in operations that require moving data between different worker nodes.

Common Shuffle Triggers in PySpark
groupBy()
join() (Except Broadcast Joins)
repartition()
distinct()
orderBy()
sort()
reduceByKey() (in RDDs)
df.write.partitionBy("column_name").parquet("output_path")
+++++++++++++++++++++++++++++++++++++++++++++++++++++
Use broadcast() for Small Tables in Joins

from pyspark.sql.functions import broadcast
df1.join(broadcast(df2), on="id", how="inner")  # Avoids shuffle
Use coalesce() Instead of repartition() When Reducing Partitions

df.coalesce(5)  # Merges partitions without full shuffle
Cache Intermediate Results

df.cache()  # Helps avoid recomputation and unnecessary shuffles
++++++++++++++++++++++++++++++++++++++++++
# Get SparkContext
sc = spark.sparkContext

# Create an RDD from a list
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data, numSlices=2)

# Check partitions
print(f"Number of partitions: {rdd.getNumPartitions()}")

# Collect results
print(rdd.collect())  # Output: [1, 2, 3, 4, 5]
✅ Spark distributes data into 2 partitions, allowing parallel processing.
+++++++++++++++++++++++++++++++++++++
rdd = x.reduceByKey(lambda a, b: a + b)
print(rdd.collect())

[('spark', 1), ('hadoop', 4)]
+++++++++++++++++++++++++++++++++++++++++++++++
from operator import add
# Create an RDD with key-value pairs
data = [("apple", 3), ("banana", 2), ("apple", 5), ("banana", 4), ("orange", 6)]
rdd = sc.parallelize(data)

# Apply reduceByKey() to sum the values for each fruit
result_rdd = rdd.reduceByKey(add)

# Collect and print results
print(result_rdd.collect())
🔹 Explanation
sc.parallelize(data) → Creates an RDD with key-value pairs (fruits & their counts).

reduceByKey(add) → Groups data by key (fruit) and adds the values.

[('apple', 8), ('banana', 6), ('orange', 6)]
✅ The function adds up values for each key:

"apple": 3 + 5 = 8

"banana": 2 + 4 = 6

"orange": 6

📌 When to Use reduceByKey() Instead of reduce()?
Function	        Use Case
reduce(func)	    Aggregates all values into a single result (e.g., sum of an entire list).
reduceByKey(func)	Aggregates values per key in a key-value RDD (e.g., summing sales per product).
+++++++++++++++++++++++++++++++++++
join(how=semileft)
join(how=leftanti)### show unmatch data from left df
+++++++++++++++++++++++
2. intersect() (Strict, Based on All Columns)
Compares entire rows, not specific columns.

Returns only common rows across both DataFrames.

Automatically removes duplicates (like SQL INTERSECT).

Does not allow column selection for comparison.

+++++++++++++++++++++++++++++++++++++++++++++++
Difference Between map() and flatMap() in PySpark

1. map()
Applies a function to each element in the RDD.
Each input produces exactly one output element.
The output remains a list of lists if the function returns a list.


2. flatMap()
Applies a function that returns an iterable (list, set, etc.).
Flattens the output, meaning multiple elements can be returned for each input.
Removes one level of nesting.
+++++++++++++++++++++++++++++++++++++++++++++++
df.write.mode("overwrite").csv("path/to/output_directory", header=True)
df.write.option("compression", "gzip").csv("path/to/output_directory")
f.write.partitionBy("year", "month").csv("path/to/output_directory", header=True)
df.coalesce(1).write.csv("path/to/output_directory", header=True)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
In PySpark, DataFrames are immutable, meaning you cannot modify them "in place" like you can in Pandas. Instead, every transformation creates a new DataFrame.

However, you can reassign the modified DataFrame to the same variable to simulate in-place modifications.
++++++++++++++++++++++++++++++++++++++++++++++++
df = spark.read.json("path/to/output.json")
df = spark.read.format("delta").load("s3://my-bucket/delta_table")
df.write.format("delta").mode("overwrite").save("/delta/events")
df.printSchema()
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
OPTIMIZE delta.`/path/to/table`
[WHERE predicate]
[ZORDER BY (col1, col2, ...)]
Compacts small files: It combines many small files into larger ones to reduce the overhead of managing numerous files (which is common with frequent streaming or batch inserts).
Z-ordering is a technique that physically co-locates related data in the same set of files based on the values in specified columns. When queries filter on these Z-ordered columns, the Delta Lake data-skipping feature can quickly prune away irrelevant files, dramatically reducing the amount of data that needs to be read from storage.
+++++++++++++++++++++++++++++++++++++++++++++
from delta.tables import *
deltaTable = DeltaTable.forName(spark, "table_name")
deltaTable.optimize().where("date='2021-11-18'").executeCompaction()


# Incremental RUN 
if spark.catalog.tableExists('cars_catalog.gold.dim_model'):
    delta_table = DeltaTable.forPath(spark, "abfss://gold@datalakecarsale.dfs.core.windows.net/dim_model")
    # update when the value exists
    # insert when new value 
    delta_table.alias("target").merge(df_final.alias("source"), "target.dim_model_key = source.dim_model_key")\
        .whenMatchedUpdateAll()\
        .whenNotMatchedInsertAll()\
        .execute()
++++++++++++++++++++++++++++++++++++++++++++++++++++
# mode("overwrite") for initial run, mode("append") for subsequent incremental runs.
df.write
  .format("delta")
  .mode("overwrite")
  .option("replaceWhere", "date >= '2017-01-01' AND date <= '2017-01-31'")
  .save("/delta/events")
  
 By default, overwriting the data in a table does not overwrite the schema. When overwriting a table using mode("overwrite") without replaceWhere, you may still want to override the schema of the data being written. You can choose to replace the schema and partitioning of the table by setting:
 
df.write.option("overwriteSchema", "true")
 
df_one_column.write.format("delta").mode("overwrite").option("mergeSchema", "true").save(my_path)
df_one_column.write.format("delta").mode("overwrite").option("overwriteSchema", "True").option("mergeSchema", "true").save(my_path) 

Option	            Use Case
mergeSchema	        Add new columns without dropping existing ones.
overwriteSchema	    Completely replace the existing schema — drops columns not in the DataFrame.
Both together	    Usually redundant; if overwriteSchema is set, it dominates and mergeSchema has no practical effect.


.save()	            _delta_log folder + Parquet files at my_path. No metastore entry.
.saveAsTable()	    Same _delta_log and Parquet files (often at a default or external location) plus a metastore (e.g. Databricks Hive Metastore or Unity Catalog, depending on your environment). entry so you can SELECT * FROM my_table_name.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@dlt.table(
    comment="Raw customer orders, as-is from source files. Auto Loader detects new files incrementally.",
    table_properties={"quality": "bronze"}
)
def raw_customer_orders():
  return (
    spark.readStream.format("cloudFiles")
      .option("cloudFiles.format", "json") # Or "csv", "parquet" etc.
      .option("cloudFiles.schemaLocation", f"{raw_data_path_orders}/_schema") # DLT manages schema for Auto Loader
      .option("cloudFiles.inferSchema", "true") # Infer schema at Bronze for flexibility
      .load(raw_data_path_orders)
      .withColumn("ingestion_timestamp", current_timestamp())
  )

Note: cloudFiles.schemaLocation	Tells Auto Loader where to store and retrieve the schema in cloud storage

++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Use CREATE STREAMING LIVE TABLE for true streaming sources (Kafka, Event Hubs).

Use CREATE INCREMENTAL LIVE TABLE when you’re working with files that arrive in batches in a data lake.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
from pyspark.sql.functions import lit, col

# Add a constant column
df = df.withColumn("constant_column", lit("constant_value"))

# Use literal in a calculation
df = df.withColumn("new_value", col("existing_column") * lit(5))
++++++++++++++++++++++++++++++++++++++++++++++
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Starting transformation step 1")
+++++++++++++++++++++++++++++++++++++++++++++++++++
print("\nReading previous version (version 0) of Delta table:")
spark.read.format("delta").option("versionAsOf", 0).load(delta_output_path).show()

# Run OPTIMIZE to consolidate small files
print("\nRunning OPTIMIZE command...")
deltaTable = DeltaTable.forPath(spark, delta_table_path)
# You can specify optional ZORDER BY for further optimization based on query patterns
deltaTable.optimize().executeCompaction()
print("OPTIMIZE complete.")
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Partition the DataFrame by multiple columns (SaleYear, SaleMonth, Region)
df_partitioned.write \
    .partitionBy("SaleYear", "SaleMonth", "Region") \
    .mode("overwrite") \
    .parquet(output_path)

partitioned by year, month, region
# 2. Filter for specific partitions using the partitioning columns
# Spark's optimizer will push these filters down to the file system level
# and only read data from matching directories (e.g., /data/sales_by_ymr/year=2023/month=1/region=East/)
filtered_df_1 = df.filter((col("year") == 2023) & (col("month") == 1) & (col("region") == "East"))

+++++++++++++++++++++++++++++++++++++++++++++++update in spark+++++++++++++++++++++
B. Updating Data (by rewriting affected partitions)
To update sales for "RegionA" in "2023-Q1" to 500:

# Create the initial data again for this update example
df.write.partitionBy("Year", "Quarter", "Region").mode("overwrite").parquet(base_data_path)

# 1. Read the data you want to update (the specific partition)
df_to_update = spark.read.parquet(base_data_path).filter(
    (col("Year") == "2023") & (col("Quarter") == "Q1") & (col("Region") == "RegionA")
)

# 2. Apply the update
df_updated_part = df_to_update.withColumn("Sales", col("Sales") * 5) # Example: Multiply sales by 5

# 3. Read all data *excluding* the partition you just updated
df_other_parts = spark.read.parquet(base_data_path).filter(
    ~((col("Year") == "2023") & (col("Quarter") == "Q1") & (col("Region") == "RegionA"))
)

# 4. Union the updated partition with the rest of the data
df_final = df_other_parts.union(df_updated_part)

# 5. Overwrite the entire dataset (or just the affected partitions if using dynamic partition overwrite)
# For dynamic partition overwrite, Spark rewrites only the partitions present in df_final
# Ensure spark.sql.sources.partitionOverwriteMode is set to "dynamic" (default in Spark 3.x)
df_final.write.partitionBy("Year", "Quarter", "Region").mode("overwrite").parquet(base_data_path)

print("\nAfter updating sales for 2023-Q1-RegionA:")
spark.read.parquet(base_data_path).orderBy("Year", "Quarter", "Region").show()

+++++++++++++++++++++++++++++++++++++++++++++++++delete in spark +++++++++++++++++++++++
# 1. Read all data *excluding* the partition(s) you want to delete
# Filter to keep everything that is NOT '2023' AND 'Q1' AND 'RegionA'
df_to_keep = spark.read.parquet(base_data_path).filter(
    ~((col("Year") == "2023") & (col("Quarter") == "Q1") & (col("Region") == "RegionA"))
)

# 2. Overwrite the original data location with the filtered DataFrame
# This will effectively delete the rows/partitions not included in df_to_keep
df_to_keep.write.partitionBy("Year", "Quarter", "Region").mode("overwrite").parquet(base_data_path)
+++++++++++++++++++++++++++++++++++++++++++++++++ delta delete+++++++++++++++++++++++++++

# Load the Delta table
delta_table = DeltaTable.forPath(spark, delta_table_path)

# Delete all data for "RegionA" in "2023-Q1"
# This will be optimized to delete the specific partition directory if it contains only this data
delta_table.delete(
    "Year = '2023' AND Quarter = 'Q1' AND Region = 'RegionA'"
)

When you execute the delta_table.delete(...) command, the changes are automatically applied to the underlying Parquet files as part of that transactional operation. You do not need to perform a separate rewrite step.
++++++++++++++++++++++++++++++++++++++++++delta update++++++++++++++++++++++++++++++++++++++
# Update sales for "RegionA" in "2023-Q1"
delta_table.update(
    condition = "Year = '2023' AND Quarter = 'Q1' AND Region = 'RegionA'",
    set = { "Sales": col("Sales") * 5 } # Multiply sales by 5
)

No, you do not need to manually rewrite the Delta table after executing the delta_table.update(...) code. The changes are automatically applied to the underlying Parquet files as an atomic part of the update transaction.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
CREATE TABLE FactSales (
    SalesOrderID INT NOT NULL,
    ProductKey INT NOT NULL,
    CustomerKey INT NOT NULL,
    OrderDate DATE NOT NULL,
    SalesAmount DECIMAL(18,2)
)
WITH (
    DISTRIBUTION = HASH (CustomerKey) -- Distribute by CustomerKey
);
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++cloud_files
The cloud_files command (and by extension, Databricks Auto Loader) can read a wide variety of file formats. The most commonly supported and widely used file types are:

JSON
CSV
XML
PARQUET (Highly recommended for analytical workloads) 
Delta
AVRO
ORC
TEXT
BINARYFILE (For reading files as binary objects, useful for images, audio, etc., where the content isn't directly parsed)
When you use cloud_files, you specify the format using an option like option("cloudFiles.format", "parquet") or format => "csv" in SQL.

Example in Python (PySpark):

Python

# Ingesting Parquet files
df = spark.readStream \
  .format("cloudFiles") \
  .option("cloudFiles.format", "parquet") \
  .option("cloudFiles.schemaLocation", "/path/to/schema_checkpoint_directory")// Yes, the cloudFiles.schemaLocation option in Databricks Auto Loader is available for all supported data file formats, not just Delta Lake
  format.load("/path/to/source_data_directory")

# Write to a Delta Lake table
df.writeStream \
  .format("delta") \
  .option("checkpointLocation", "/path/to/checkpoint_directory") \
  .start("/path/to/delta_table_location")
Example in SQL (Delta Live Tables or Streaming Tables):

SQL

CREATE OR REFRESH STREAMING TABLE raw_data_table
AS SELECT * FROM cloud_files("/path/to/source_data_directory", "csv", map("cloudFiles.schemaLocation", "/path/to/schema_checkpoint_directory"));
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++merge

from delta.tables import DeltaTable

# Suppress INFO messages for cleaner output
spark.sparkContext.setLogLevel("ERROR")

# ... (SparkSession and target_delta_table setup) ...

# Get the target DeltaTable object
deltaTable = DeltaTable.forPath(spark, "/path/to/delta/table")

# Perform the merge operation
deltaTable.merge(
    source=source_df,                             # The DataFrame with new data/changes
    target=target_alias,                          # An alias for the target table (e.g., "target_alias")
    condition="target_alias.id = source_df.id"    # The join/matching condition between source and target
) \
.whenMatchedUpdate(                               # Action when rows match
    condition="...",                              # Optional: further condition for update
    set = { "col1": "source_df.new_col1", "col2": "source_df.new_col2" } # Columns to update
) \
.whenMatchedDelete(                               # Action when rows match
    condition="..."                               # Optional: further condition for delete
) \
.whenNotMatchedInsert(                            # Action when rows don't match
    values = { "col1": "source_df.col1", "col2": "source_df.col2" } # Columns to insert
) \
.execute()
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# --- 5. Using rlike() for pattern matching (similar to 'LIKE' in SQL) ---
# Add a 'CityType' column:
#   "East Coast" if City contains "New York" or "Boston"
#   "West Coast" if City contains "Los Angeles"
#   "Midwest" if City contains "Chicago"
#   "Other" otherwise
print("--- 5. DataFrame with 'CityType' Column using rlike() ---")
df_with_city_type = df_with_special_category.withColumn(
    "CityType",
    when(col("City").rlike("New York|Boston"), "East Coast") # Matches "New York" or "Boston"
    .when(col("City").rlike("Los Angeles"), "West Coast")    # Matches "Los Angeles"
    .when(col("City").rlike("Chicago"), "Midwest")            # Matches "Chicago"
    .otherwise("Other")
    
 df_with_name_like = df_with_age_parity.withColumn(
    "NameContainsA",
    when(col("Name").like("%a%"), "Yes") # Checks if 'Name' contains 'a'
    .otherwise("No")
)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
should we mention complete partition path if we want to update data in pyspark?



Show thinking
When performing an "update" operation on partitioned data in PySpark, you generally do not explicitly mention the complete partition path in your write operation. Instead, Spark handles the partition discovery and overwrite logic based on your DataFrame's content and the partitionBy and mode("overwrite") options.

Let's break down why and how:

Spark's Immutability and How "Updates" Work
A fundamental concept in Spark (and distributed file systems like HDFS, S3, ADLS) is that data files are generally immutable. You don't update individual rows in place within an existing Parquet or ORC file.

When you "update" data in Spark, what actually happens is:

Read: You read the existing data (or the relevant portions/partitions of it).
Transform: You apply your update logic (e.g., filtering, joining with new data, modifying columns) to create a new DataFrame that contains the updated rows.
Write: You write this new DataFrame to the storage location.
The "update" part comes from how you manage the writing part, especially with partitioned data.

Strategies for "Updating" Partitioned Data
There are a few common strategies, and the handling of partition paths differs:

1. Full Overwrite (Least Efficient for Updates)
If you read the entire dataset, apply updates, and then overwrite the entire base path, Spark will delete all existing data in that location and write the new data, recreating the partition structure.

Python

# Assume original data is at "abfss://mycontainer@mystorage.dfs.core.windows.net/my_dataset"
# Partitioned by year and month, e.g., my_dataset/year=2023/month=01/part-00000.parquet

# 1. Read ALL existing data
df_existing = spark.read.parquet("abfss://mycontainer@mystorage.dfs.core.windows.net/my_dataset")

# 2. Perform your updates (e.g., update 'value' for 'id' 100)
from pyspark.sql.functions import when
df_updated_all = df_existing.withColumn(
    "value",
    when(df_existing.id == 100, 999).otherwise(df_existing.value)
)

# 3. Overwrite the entire dataset (deletes everything and rewrites)
# You only specify the base path.
df_updated_all.write.mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet("abfss://mycontainer@mystorage.dfs.core.windows.net/my_dataset")

# Disadvantage: This is very inefficient for large datasets if only a few records change.
2. Dynamic Partition Overwrite (Most Common for Partial Updates)
This is where the power of Spark's partitioning for updates shines. You only process and write the specific partitions that contain the data you want to update. Spark then intelligently overwrites only those partitions while leaving others untouched.

For this to work, you need to:

Ensure your DataFrame contains the partition columns (year, month in our example).
Use mode("overwrite").
Specify partitionBy() with the partition columns.
<!-- end list -->

Python

# Assume original data:
# my_dataset/year=2023/month=01/part-x.parquet (contains id=100)
# my_dataset/year=2023/month=02/part-y.parquet

# Let's say we want to update a record with id=100, which is in year=2023, month=01

# 1. Read ONLY the specific partition(s) affected by your update
# You can use filter pushdown for this, or explicitly point to the sub-path if known
df_target_partition = spark.read.parquet("abfss://mycontainer@mystorage.dfs.core.windows.net/my_dataset") \
    .filter("year = 2023 AND month = 01")

# 2. Perform your updates on this filtered DataFrame
from pyspark.sql.functions import lit
df_updated_partition = df_target_partition.withColumn(
    "value",
    when(df_target_partition.id == 100, lit(999)).otherwise(df_target_partition.value)
)

# 3. Write back the updated partition.
# Spark will automatically overwrite ONLY the partitions (year=2023/month=01)
# that are present in the `df_updated_partition` DataFrame.
# The `partitionBy` is crucial for Spark to understand the partitioning scheme.
df_updated_partition.write.mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet("abfss://mycontainer@mystorage.dfs.core.windows.net/my_dataset")

# After this, the data in 'my_dataset/year=2023/month=01' is replaced,
# but 'my_dataset/year=2023/month=02' (and other partitions) remains untouched.
Key takeaway for Dynamic Partition Overwrite: You don't provide a path like "my_dataset/year=2023/month=01". You provide the base path of the table ("my_dataset") and let Spark's partitionBy and mode("overwrite") logic handle which specific partition directories to rewrite based on the data within the DataFrame being written.

3. Using Transactional Lakehouse Formats (Delta Lake, Apache Iceberg, Apache Hudi)
For true row-level updates, upserts, and merges, the most robust and recommended approach in a "Lakehouse" architecture is to use a transactional table format like Delta Lake, Apache Iceberg, or Apache Hudi.

With these formats, you interact with the data more like a traditional database table:

You refer to the table by name (or base path), not by partition paths.
You use SQL-like commands (UPDATE, MERGE INTO, DELETE) or their specific API operations.
The underlying engine (Delta, Iceberg, Hudi) intelligently identifies and rewrites only the specific data files within partitions that contain the changed rows. This is highly optimized and handles ACID properties.
Example with Delta Lake (available in Azure Synapse Analytics, Azure Databricks):

Python

# Assume you have a Delta table at "abfss://mycontainer@mystorage.dfs.core.windows.net/my_delta_table"
# This table is also partitioned by year and month internally.

# 1. Read the Delta table
from delta.tables import DeltaTable # Requires delta-spark package

delta_table = DeltaTable.forPath(spark, "abfss://mycontainer@mystorage.dfs.core.windows.net/my_delta_table")

# 2. Perform an UPDATE operation (true in-place update behavior)
delta_table.update(
    condition = "id = 100 AND year = 2023 AND month = 01",
    set = { "value": lit(999), "last_updated": current_timestamp() }
)

# 3. Perform a MERGE (upsert) operation
# df_updates: a DataFrame containing new or updated records, including partition columns
delta_table.merge(
    source = df_updates,
    target = delta_table.alias("target"),
    condition = "target.id = source.id AND target.year = source.year AND target.month = source.month"
).whenMatchedUpdate(set = {
    "value": "source.value",
    "last_updated": current_timestamp()
}).whenNotMatchedInsert(values = {
    "id": "source.id",
    "name": "source.name",
    "value": "source.value",
    "year": "source.year",
    "month": "source.month",
    "last_updated": current_timestamp()
}).execute()

# Here, you don't mention the partition path at all.
# The Delta Lake engine handles the file-level operations within the partitions automatically.
Conclusion
So, to directly answer your question:

For native PySpark (without transactional formats like Delta Lake), you do not mention the complete partition path in the write operation itself. Instead, you write to the base path and rely on mode("overwrite") combined with partitionBy() on a DataFrame that only contains data for the partitions you intend to overwrite. This is known as dynamic partition overwrite.
For transactional table formats (Delta Lake, Iceberg, Hudi), you perform SQL UPDATE or MERGE INTO commands on the table name (or base path), and the underlying engine automatically manages the specific file changes within the affected partitions. This provides the most "database-like" update experience.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
CREATE TABLE t1
USING DELTA
LOCATION '/mnt/teste1/'; -- Use the correct absolute path to your Delta table data
++++++++++
-- Assuming '/mnt/teste1/' points to an existing Delta table
CREATE TABLE t1 AS
SELECT * FROM delta.`/mnt/teste1/`;
-- Or, if the path is complex or needs to be quoted
-- SELECT * FROM delta."/mnt/teste1/";
++++++++++++
SELECT * FROM delta.`/mnt/teste1/`;

++++++++++++++++++++++++++++++++++++++++++
-- Assuming your CSV files are located in '/mnt/teste1/'
-- and the first row contains headers.

CREATE TABLE t1 (
  -- Define your schema here based on your CSV columns
  col1 STRING,
  col2 INT,
  col3 DOUBLE
)
USING CSV
OPTIONS (
  'header' = 'true', -- If your CSV has a header row
  'inferSchema' = 'true' -- Optional: Let Spark infer column types, but defining them is more robust
)
LOCATION '/mnt/teste1/';
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
does the following sql code work in sql server: No, the SQL code you provided will NOT work in SQL Server.

CREATE TABLE t1 (

  -- Define your schema here based on your CSV columns

  col1 STRING,

  col2 INT,

  col3 DOUBLE

)

USING CSV

OPTIONS (

  'header' = 'true', -- If your CSV has a header row

  'inferSchema' = 'true' -- Optional: Let Spark infer column types, but defining them is more robust

)

LOCATION '/mnt/teste1/';
+++
§§§$$$$$$$$$$ Solutions:
-- 1. Create the table in SQL Server first (manually defining columns and data types)
CREATE TABLE t1 (
    col1 NVARCHAR(255), -- Use appropriate SQL Server data types
    col2 INT,
    col3 FLOAT
);
GO

-- 2. Use BULK INSERT to load data from the CSV file
BULK INSERT t1
FROM 'C:\path\to\your\local\file\teste1.csv' -- Or a UNC path for network share, or Azure Blob Storage URL with credential
WITH (
    FORMAT = 'CSV',        -- Specifies the file is CSV format
    FIRSTROW = 2,          -- Skips the header row (if present)
    FIELDTERMINATOR = ',', -- Specifies comma as delimiter
    ROWTERMINATOR = '\n'   -- Specifies newline as row terminator (use '\r\n' for Windows-style)
    -- Other options like CODEPAGE, TABLOCK, ERRORFILE, etc.
);
GO
+++
§§§ 
-- Example for local file (requires appropriate drivers and permissions)
SELECT *
FROM OPENROWSET(BULK 'C:\path\to\your\local\file\teste1.csv',
                FORMATFILE='C:\path\to\your\local\file\teste1.fmt', -- Optional: A format file can define schema and options
                FIRSTROW = 2) AS t1_data;

-- Example for Azure Blob Storage (requires external data source and credentials setup)
SELECT *
FROM OPENROWSET(BULK 'https://<storageaccount>.blob.core.windows.net/<container>/teste1.csv',
                DATA_SOURCE = 'AzureBlobDataSource', -- An external data source pointing to your blob storage
                FORMAT = 'CSV',
                FIRSTROW = 2,
                PARSER_VERSION = '2.0' -- For newer features
               ) AS t1_data;
+++
§§§
-- PolyBase Example (simplified)
-- Requires prior setup of external data source and external file format

CREATE EXTERNAL TABLE t1 (
    col1 NVARCHAR(255),
    col2 INT,
    col3 FLOAT
)
WITH (
    LOCATION = '/path/to/csv/folder/', -- Path within your external data source
    DATA_SOURCE = ExternalDataSourceName,
    FILE_FORMAT = ExternalFileFormatName -- Defined for CSV with header etc.
);
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
mounted_filesystems = dbutils.fs.mounts()
mount_point_to_check = "/mnt/medallion"
is_mounted = False
for mount in mounted_filesystems:
    if mount.mountPoint == mount_point_to_check:
        is_mounted = True
        break
if is_mounted:
    print("Mount point is mounted.")
else:
    print("Mount point is not mounted.")
    dbutils.fs.mount(
    source="wasbs://<container_name>@<storage_account_name>.blob.core.windows.net/",
    mount_point="/mnt/medallion",
    extra_configs={
    "fs.azure.account.key.<storage_account_name>.blob.core.windows.net": "<storage_account_key>"
  }
)
++++++
https://medium.com/@geetanjalichipurapalli/end-to-end-azure-data-engineering-project-part-2-implementing-medallion-architecture-in-azure-ffd03c718673
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
logging.info("notify") (using Python's logging module)
Logging Levels: The logging module supports different severity levels:

DEBUG: Detailed information, typically only of interest when diagnosing problems.
INFO: Confirmation that things are working as expected.

WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g., 'disk space low'). The software is still working as expected.

ERROR: Due to a more serious problem, the software has not been able to perform some function.
CRITICAL: A serious error, indicating that the program itself may be unable to continue running. You can configure the 

logger to only output messages at or above a certain level.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
file_path = "/path/to/your/parquet/data/" # Placeholder: Update with your actual path

@dlt.table(
  comment="Raw data from a subset of the Million Song Dataset; a collection of features and metadata for contemporary music tracks. Ingested from Parquet files."
)
def songs_raw():
  return (spark.readStream
    .format("cloudFiles")
    # Removed .schema(schema) because inferSchema=True will handle it.
    .option("cloudFiles.format", "parquet") # Changed format to parquet
    # Removed .option("sep","\t") as it's not relevant for Parquet files.
    .option("inferSchema", True) # Keep inferSchema as requested
    .load(file_path))
 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
data = [("A", [1, 2, 3]), ("B", [4, 5]), ("C", [6])]
columns = ["group", "numbers"]
df = spark.createDataFrame(data, columns)

def process_partition(iterator):
    # This loop runs on each executor, for the rows in its partition
    for row in iterator:
        group_id = row["group"]
        processed_numbers = []
        # Inner loop to process elements in the 'numbers' array
        for num in row["numbers"]:
            processed_numbers.append(f"{group_id}_{num}") # Example transformation
            
        yield (group_id, processed_numbers)# Yes, you could technically discard yield in that specific process_partition function and achieve the same functional result, but it would come with a potential memory and performance drawback.

# Apply the function to each partition
result_rdd = df.rdd.mapPartitions(process_partition)

# Convert back to DataFrame
result_df = result_rdd.toDF(["group", "processed_numbers_list"])
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Reading CSV files incrementally and writing to a Delta table
spark.readStream.format("cloudFiles") \
  .option("cloudFiles.format", "csv") \
  .option("cloudFiles.schemaLocation", "/path/to/csv_schema_checkpoint") \
  .option("header", "true") \
  .load("/path/to/incoming/csv_files") \
  .filter("some_condition") \
  .writeStream \
  .format("delta") \
  .option("checkpointLocation", "/path/to/delta_checkpoint") \
  .start("/path/to/bronze_delta_table")