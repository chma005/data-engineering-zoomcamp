# data-engineering-zoomcamp
Data Engineering course to gain some knowledge in DE. 

Goal: Apply the learnings in this course to my life. Merge the learnings from DE-ZC24 to my Food Safety / Quality background.

Brief Summary over different modules:

Module 1: 
Build a data ingestion pipeline. Use docker file to build image that will run python ingestion script. Python ingestion script loads data in chunks to postgres db. Post gres db is ran using a docker_compose.yaml file. PGAdmin is used as GUI to interact with pg db. 

Module 2: 
Utilize Mage to build ETL pipeline. Extract data located on the web. Data is in CSV or Parquet files, we transform data within mage, then load data to Cloud or BQ.

Module 3: 
Overview of data warehouses. Utilize Big Query to interact with data stored in google cloud (mod 2). Build queries and understand the different between internal and external tables.

Module 4:
Utilize DBT, to run analytics on data stored in google cloud. Build tests in dbt. Build jobs to test if pull requests will work to prevent crashing the production branch. Utilized Google Looker to build out graphs of data from BQ. 
