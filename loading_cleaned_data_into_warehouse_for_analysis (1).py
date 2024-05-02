import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1713378164365 = glueContext.create_dynamic_frame.from_catalog(database="youtube_cleaned_data", table_name="csv_to_parquet_processed", transformation_ctx="AWSGlueDataCatalog_node1713378164365")

# Script generated for node AWS Glue Data Catalog
AWSGlueDataCatalog_node1713378162605 = glueContext.create_dynamic_frame.from_catalog(database="youtube_cleaned_data", table_name="json_to_parquet_processed", transformation_ctx="AWSGlueDataCatalog_node1713378162605")

# Script generated for node Join
Join_node1713378181887 = Join.apply(frame1=AWSGlueDataCatalog_node1713378164365, frame2=AWSGlueDataCatalog_node1713378162605, keys1=["category_id"], keys2=["id"], transformation_ctx="Join_node1713378181887")

# Script generated for node Amazon Redshift
AmazonRedshift_node1713378209186 = glueContext.write_dynamic_frame.from_options(frame=Join_node1713378181887, connection_type="redshift", connection_options={"redshiftTmpDir": "s3://aws-glue-assets-211125530375-us-east-2/temporary/", "useConnectionProperties": "true", "dbtable": "public.youtube_analysis", "connectionName": "Redshift connection", "preactions": "CREATE TABLE IF NOT EXISTS public.youtube_analysis (video_id VARCHAR, trending_date VARCHAR, title VARCHAR, channel_title VARCHAR, category_id BIGINT, publish_time VARCHAR, tags VARCHAR, views BIGINT, likes BIGINT, dislikes BIGINT, comment_count BIGINT, thumbnail_link VARCHAR, comments_disabled BOOLEAN, ratings_disabled BOOLEAN, video_error_or_removed BOOLEAN, description VARCHAR, region VARCHAR, kind VARCHAR, etag VARCHAR, id BIGINT, snippet_channelid VARCHAR, snippet_title VARCHAR, snippet_assignable BOOLEAN);"}, transformation_ctx="AmazonRedshift_node1713378209186")

job.commit()