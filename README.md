# Spotify End-to-End Data Engineering Project

### Introduction
In this project, I have build an automated ELT (Extract, Transform and Load) data pipeline using Spotify API on AWS. This project will fetch Spotify API response for a playlist, load it into raw_data S3 bucket and then extract 3 different datasets (album, artist, song) out of each json file and store it in transformed S3 folder.

### Architecture
![Architecture Diagram] ()

### About API
This API contains information about music albums, artists and songs

### AWS Services used
1. **Cloud Watch:** Amazon CloudWatch is a monitoring and observability service provided by AWS that allows users to collect, track, and analyze metrics, logs, and events for their AWS resources and applications. It enables users to gain insights into the operational health, performance, and resource utilization of their infrastructure and applications. CloudWatch allows users to set alarms, visualize data, and automate actions based on predefined rules.
2. **Lambda:** AWS Lambda is a serverless compute service that enables users to run code without provisioning or managing servers. It functions as a "Function as a Service" (FaaS), meaning users upload their code as "Lambda functions," and AWS handles all the underlying infrastructure, including server and operating system maintenance, capacity provisioning, automatic scaling, and logging.
3. **S3:** Amazon S3, or Simple Storage Service, is a cloud-based object storage service offered by AWS. It allows users to store and retrieve any amount of data from anywhere on the web. S3 is designed for storing data as objects, each consisting of a file and its metadata, within containers called buckets. It's highly scalable, durable, and secure, making it a popular choice for various storage needs.
4. **Glue Crawler:** An AWS Glue Crawler is an automated tool within the AWS Glue service designed to discover and catalog metadata from various data sources. It scans your data repositories, infers the schema, and populates the AWS Glue Data Catalog with organized tables.
5. **Data Catalog:** The AWS Glue Data Catalog is a centralized, fully managed metadata repository for all your data assets within the AWS ecosystem. It functions as a persistent, Hive-compatible metastore, providing a unified view of your data across various data stores like Amazon S3, Amazon RDS, Amazon Redshift, and more.
6. **Athena:** Amazon Athena is an interactive query service provided by Amazon Web Services (AWS) that enables users to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL.

### Install packages
```
pip install numpy
pip install pandas
pip install spotipy
```

### Execution Flow
Run Extract Lambda function(every 1 hour) -> Get API response data (json) -> Store in RAW folder -> Run Transform Lambda function(based on object create event) -> Store result (album, artist, song) in transformed folder as csv file -> Run Glue Crawler to build Data Catalog -> Analyze using Athena
