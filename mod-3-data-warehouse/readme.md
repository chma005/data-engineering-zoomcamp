CREATE OR REPLACE EXTERNAL TABLE `ny-rides-chaybang.ny_taxi.external_2022_green_taxi_data`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://mage-zoomcamp-chaybang/2022_green_taxi/9e4ac0291368490e96679f717158af93-0.parquet']
);
-- create a non partitioned table from external table
CREATE OR REPLACE TABLE `ny-rides-chaybang.ny_taxi.2022_green_taxi_data_internal_non_partitioned` AS
SELECT * FROM `ny-rides-chaybang.ny_taxi.external_2022_green_taxi_data`;
-- Q1:
SELECT COUNT(*) FROM `ny-rides-chaybang.ny_taxi.2022_green_taxi_data_internal_non_partitioned`;
-- I GOT 840402 FOR Q1: B

-- Q2:
SELECT COUNT (DISTINCT PULocationID) as PULocationsIDS
FROM `ny-rides-chaybang.ny_taxi.2022_green_taxi_data_internal_non_partitioned`;
-- external 0B and internal 6.41MB; Answer A

-- Q3:
SELECT COUNT (fare_amount) as broke_boys
FROM `ny-rides-chaybang.ny_taxi.2022_green_taxi_data_internal_non_partitioned`
WHERE fare_amount = 0; 
-- 1622 broke boys. Answer D

-- Q4

CREATE OR REPLACE TABLE `ny-rides-chaybang.ny_taxi.2022_nyc_green_taxi_partitioned_clustered`
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT * FROM `ny-rides-chaybang.ny_taxi.external_2022_green_taxi_data`;

-- we should partition by lpep_pickup_datetime  and cluster on PULocationID. This will optimize our query. Answer B

-- Q5

-- query materialized table
SELECT DISTINCT PULocationID 
FROM `ny-rides-chaybang.ny_taxi.2022_green_taxi_data_internal_non_partitioned` 
WHERE TIMESTAMP_TRUNC(lpep_pickup_datetime, DAY) 
  BETWEEN TIMESTAMP("2022-06-01") and TIMESTAMP("2022-06-30");
-- bytes for materialized table: 12.82MB. 

-- query partitioned and clustered table
SELECT DISTINCT PULocationID 
FROM `ny-rides-chaybang.ny_taxi.2022_nyc_green_taxi_partitioned_clustered` 
WHERE TIMESTAMP_TRUNC(lpep_pickup_datetime, DAY) 
  BETWEEN TIMESTAMP("2022-06-01") and TIMESTAMP("2022-06-30");
-- bytes for partitioned/clustered table: 1.12 MB.
-- Answer B

-- Q6
-- GCP Bucket is where external table is stored 
-- answer B

-- Q7
-- False. Not always best practice to cluster.

-- Q8
SELECT COUNT (*) as total_data
FROM `ny-rides-chaybang.ny_taxi.2022_green_taxi_data_internal_non_partitioned`;

-- 0 bytes of data will be processed when running this query. This is because the table exists in BQ and is easier to query compared to an external table. We already invested the processing power when the table was created in BQ. 

