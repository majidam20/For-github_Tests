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

from pyspark.sql.functions import *
df.filter(col('sale')==1).show()
df.filter(df['sale']==1).show(5)
df.select(col('sale')).show(5)
df.select('sale').show(5)
df.select("Department").distinct()
df.select('sale_date').dropna().show()
df.dropna(subset=["name"])
df.fillna({"name": "Unknown"})
df.withColumnRenamed("age", "years_old")
df_renamed = df.selectExpr("id", "name as full_name", "age as years_old")
df.withColumnRenamed("old_column", "new_column")  # ❌ This does not modify df in place, so we muss reassign it
df= df.withColumnRenamed("old_column", "new_column")## ✅ Apply changes on df
df.withColumn("sale", df.sale +1).show()
%%sql
select * from dbcatalog1.cls1_mobile_code_challenge_de_csv limit 10
spark.sql('select * from dbcatalog1.cls1_mobile_code_challenge_de_csv limit 10').show()


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
orderBy() / sort()
reduceByKey() (in RDDs)
+++++++++++++++++++++++++++++++++++++++++++++++++++++
Use broadcast() for Small Tables in Joins

from pyspark.sql.functions import broadcast
df1.join(broadcast(df2), on="id", how="inner")  # Avoids shuffle
Use coalesce() Instead of repartition() When Reducing Partitions

df.coalesce(5)  # Merges partitions without full shuffle
Cache Intermediate Results

df.cache()  # Helps avoid recomputation and unnecessary shuffles