{{
    config(
        materialized='view'
    )
}}

with 

fhv_tripdata as (

    select * 
    from {{ source('staging', 'fhv_tripdata') }}
),

renamed as (
    select
        dispatching_base_num,
        pickup_datetime,
        dropoff_datetime,
        pulocationid,
        dolocationid,
        sr_flag,
        affiliated_base_number
    from fhv_tripdata
)
select * from renamed

