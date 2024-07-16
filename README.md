
# Youtube Data Analysis ETL pipeline

## Overview 
YouTube Data Analysis project involves developing ETL pipeline using AWS services for securely managing, streamlining, and performing analysis on the structured and semi-structured data Using AWS Lambda and AWS glue. Further, the transformed parquet data is loaded into AWS Redshift to visualize data insights in Tableau Desktop.

**Below are some of the business questions we aim to answer with this project.**
1. Which region has the highest YouTube viewership? 
2. Which category of videos are most consumed? 
3. Which videos are most disliked based on category and region? 
4. What are the total number of likes across all videos in regions Canada, United States, and Great Britain? 
5. Which category of videos are most liked? 

# Architecture Diagram

![youtube_data_analysis_architecture_100%](https://github.com/user-attachments/assets/82dd370e-38d3-43a7-9acf-f2190f9822d9)

## Goals
1. **AWS Cloud** : Processing vast amounts of data to answer business questions could be challenging on local computers, so need to use the cloud, in this case, we will use AWS.
2. **Data Ingestion** : Build a mechanism to ingest data into S3. Involves planning a strategy to handle both CSV and JSON files extracted from Kaggle.
3. **Staging** : Build a staging Layer using the Glue catalog for further processing of JSON and CSV data.
4. **Testing** : Testing small batches of CSV and JSON Data with AWS Lambda and AWS Glue before automating the entire processing layer.
5. **ETL (Extract, Transform, Load)** : Both CSV and JSON Data in raw format should be cleaned and transformed into Parquet format using AWS Lambda and AWS Glue.
6. **Automation** : Make sure the entire ETL is automated to handle higher throughputs using AWS Lambda triggers.
7. **Data Lake** : All the cleaned data from CSV and JSON needs a centralized repo such as S3 to store them to perform further transformations and loading into the warehouse.
8. **Analytics** : Further transformed data should be loaded into Redshift for faster querying and analytics purposes.
9. **Reporting** : Build a dashboard from Redshift to get insights required for business needs using Amazon QuickSight.
10. **Scalability** : As the size of data increases, we need to make sure the architecture built scales with it.
11. **Monitoring** : Use CloudWatch to monitor logs across all AWS services.

## Services
1. **Amazon S3** : An object storage service providing manufacturing scalability, data availability, security, and performance.
2. **AWS IAM** : Identity and Access Management enabling secure management of access to AWS services and resources.
3. **QuickSight** : A scalable, serverless, embeddable, machine learning-powered business intelligence (BI) service built for the cloud.
4. **AWS Glue** : A serverless data integration service that makes it easy to discover, prepare, and combine data for analytics, machine learning, and application development.
5. **AWS Lambda** : A computing service allowing programmers to run code without creating or managing servers.
6. **AWS Athena** : An interactive query service for S3, with no need to load data as it stays in S3.
7. **AWS Redshift** : A data warehouse service used to store processed data for analytics purposes.
8. **AWS CloudWatch** : A service for monitoring and observing logs across all AWS services.

## Datasets used
This Kaggle dataset contains statistics (CSV files and JSON files) on daily popular YouTube videos over the course of many months. There are up to 200 trending videos published every day for many locations. The data for each region is in its own file. The video title, channel title, publication time, tags, views, likes and dislikes, description, and comment count are among the items included in the data. A category_id field, which differs by area, is also included in the JSON file linked to the region.
https://www.kaggle.com/datasets/datasnaek/youtube-new

## Risks and Mitigation
Costs of AWS services could be increasing if not monitored properly. To tackle this problem, budgets can be introduced using AWS billing and cost management. 

## Conclusion
Overall, we have to process both CSV and JSON data in the cloud environment and visualize data insights to answer business questions.

## Data Visualization with Tableau Desktop
1. **Install the ODBC Redshift Driver**: Required for Tableau Desktop to connect to Redshift.
2. **Create an Extract Connection**: Connect Tableau Desktop to Redshift.
3. **Create Visualizations**: Use Tableau Desktop to process and visualize the data.

> ### Checkout Tableau data visualization at [Youtube data metrics \| Tableau Public](https://public.tableau.com/app/profile/ravi.shankar.p.r/viz/youtube_data_metrics/Dashboard2)


