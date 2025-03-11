import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from recipe_transforms import *
from awsgluedq.transforms import EvaluateDataQuality
from awsglue.dynamicframe import DynamicFrame
from awsglue import DynamicFrame
from pyspark.sql import functions as SqlFuncs

def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)
# Generated recipe steps for DataPreparationRecipe_node1741539496515
def applyRecipe_node1741539496515(inputFrame, glueContext, transformation_ctx):
    frame = inputFrame.toDF()
    gc = glueContext
    df0 = frame
    return DynamicFrame.fromDF(df0, gc, transformation_ctx)

def sparkAggregate(glueContext, parentFrame, groups, aggs, transformation_ctx) -> DynamicFrame:
    aggsFuncs = []
    for column, func in aggs:
        aggsFuncs.append(getattr(SqlFuncs, func)(column))
    result = parentFrame.toDF().groupBy(*groups).agg(*aggsFuncs) if len(groups) > 0 else parentFrame.toDF().agg(*aggsFuncs)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Default ruleset used by all target nodes with data quality enabled
DEFAULT_DATA_QUALITY_RULESET = """
    Rules = [
        ColumnCount > 0
    ]
"""

# Script generated for node Amazon S3
AmazonS3_node1741539402305 = glueContext.create_dynamic_frame.from_options(format_options={"quoteChar": "\"", "withHeader": True, "separator": ","}, connection_type="s3", format="csv", connection_options={"paths": ["s3://bucketusatest1/mobile_code_challenge_de.csv"], "recurse": True}, transformation_ctx="AmazonS3_node1741539402305")

# Script generated for node Data Preparation Recipe
# Adding configuration for certain Data Preparation recipe steps to run properly
spark.conf.set("spark.sql.legacy.timeParserPolicy", "LEGACY")
# Recipe name: DataPreparationRecipe_node1741539496515
DataPreparationRecipe_node1741539496515 = applyRecipe_node1741539496515(
    inputFrame=AmazonS3_node1741539402305,
    glueContext=glueContext,
    transformation_ctx="DataPreparationRecipe_node1741539496515")

# Script generated for node Change Schema
ChangeSchema_node1741539538149 = ApplyMapping.apply(frame=DataPreparationRecipe_node1741539496515, mappings=[("_ingested_at", "string", "_ingested_at", "string"), ("lead_id", "string", "lead_id", "bigint"), ("at_date", "string", "at_date", "string"), ("request_amount", "string", "request_amount", "string"), ("sale", "string", "sale", "string"), ("sale_amount", "string", "sale_amount", "string"), ("sale_date", "string", "sale_date", "string"), ("lead_beendet__kredit_storniert", "string", "lead_beendet__kredit_storniert", "string"), ("tracking", "string", "tracking", "string")], transformation_ctx="ChangeSchema_node1741539538149")

# Script generated for node SQL Query
SqlQuery0 = '''
select sale, sale_amount, sale_date  from myDataSource
'''
SQLQuery_node1741539663929 = sparkSqlQuery(glueContext, query = SqlQuery0, mapping = {"myDataSource":ChangeSchema_node1741539538149}, transformation_ctx = "SQLQuery_node1741539663929")

# Script generated for node Aggregate
Aggregate_node1741539725604 = sparkAggregate(glueContext, parentFrame = SQLQuery_node1741539663929, groups = [], aggs = [["sale_amount", "avg"]], transformation_ctx = "Aggregate_node1741539725604")

# Script generated for node Amazon S3
EvaluateDataQuality().process_rows(frame=Aggregate_node1741539725604, ruleset=DEFAULT_DATA_QUALITY_RULESET, publishing_options={"dataQualityEvaluationContext": "EvaluateDataQuality_node1741539070110", "enableDataQualityResultsPublishing": True}, additional_options={"dataQualityResultsPublishing.strategy": "BEST_EFFORT", "observations.scope": "ALL"})
AmazonS3_node1741540241302 = glueContext.getSink(path="s3://bucketusatest1", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=[], compression="snappy", enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1741540241302")
AmazonS3_node1741540241302.setCatalogInfo(catalogDatabase="dbcatalog1",catalogTableName="tbl3")
AmazonS3_node1741540241302.setFormat("csv")
AmazonS3_node1741540241302.writeFrame(Aggregate_node1741539725604)
job.commit()