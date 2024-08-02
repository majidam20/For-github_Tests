https://sparkbyexamples.com/pyspark-tutorial/
https://spark.apache.org/docs/latest/rdd-programming-guide.html

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

df = spark.createDataFrame(df_pd)  

df = spark.sparkContext.parallelize([(12, 20, 35, 'a b c'),(41, 58, 64, 'd e f'), (70, 85, 90, 'g h i')]).toDF(['col1', 'col2', 'col3','col4']) 

df.write.parquet(parquet_file_path)

# Add a new calculated column
df_with_new_column = df.withColumn("revenue", df.quantity * df.price)


from pyspark.sql.window import Window
from pyspark.sql import functions as F
# Create a window specification
window_spec = Window.partitionBy("department").orderBy(F.desc("salary"))
# Calculate the rank of employees within each department based on salary
employee_salary.withColumn("rank", F.rank().over(window_spec)).show()

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