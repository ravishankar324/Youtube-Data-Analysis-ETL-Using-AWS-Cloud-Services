import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

predicate_pushdown = "region in ('ca', 'gb', 'us')"

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1713308987395 = glueContext.create_dynamic_frame.from_catalog(database="youtube_raw_data", table_name="csv_raw_data_csv", transformation_ctx="AWSGlueDataCatalog_node1713308987395", push_down_predicate = predicate_pushdown)

# Script generated for node Change Schema
ChangeSchema_node1713309006786 = ApplyMapping.apply(frame=AWSGlueDataCatalog_node1713308987395, mappings=[("video_id", "string", "video_id", "string"), ("trending_date", "string", "trending_date", "string"), ("title", "string", "title", "string"), ("channel_title", "string", "channel_title", "string"), ("category_id", "long", "category_id", "bigint"), ("publish_time", "string", "publish_time", "string"), ("tags", "string", "tags", "string"), ("views", "long", "views", "bigint"), ("likes", "long", "likes", "bigint"), ("dislikes", "long", "dislikes", "bigint"), ("comment_count", "long", "comment_count", "bigint"), ("thumbnail_link", "string", "thumbnail_link", "string"), ("comments_disabled", "boolean", "comments_disabled", "boolean"), ("ratings_disabled", "boolean", "ratings_disabled", "boolean"), ("video_error_or_removed", "boolean", "video_error_or_removed", "boolean"), ("description", "string", "description", "string"), ("region", "string", "region", "string")], transformation_ctx="ChangeSchema_node1713309006786")

# Script generated for node Amazon S3
AmazonS3_node1713309034306 = glueContext.getSink(path="s3://dataengineering-cloudcomputing-project-cleaned-parquet-data/youtube/cleaned_data_csv/", connection_type="s3", updateBehavior="UPDATE_IN_DATABASE", partitionKeys=["region"], enableUpdateCatalog=True, transformation_ctx="AmazonS3_node1713309034306")
AmazonS3_node1713309034306.setCatalogInfo(catalogDatabase="youtube_cleaned_data",catalogTableName="csv_to_parquet_processed")
AmazonS3_node1713309034306.setFormat("glueparquet", compression="snappy")
AmazonS3_node1713309034306.writeFrame(ChangeSchema_node1713309006786)
job.commit()