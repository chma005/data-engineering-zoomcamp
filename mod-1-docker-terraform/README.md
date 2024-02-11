services: 
    postgres: 
        image: postgres:13
        environment:
            POSTGRES_USER: airflow
            POSTGRES_PASSWORD: airflow
            POSTGRES_DB: airflow
        volumes:
            - postgres/deb-volume:/var/lib/postgresql/data
        healthcheck: 
            test: ["CMD", "pg_isready", "-U", "airflow"]
            interval: 5s
            restries:5
        restart: always

# run an instance of post gres, this comman will run an image of postgres(from the hub) and has the env variabiable 
# (-e) that we create. -v is connect a file from this directory to the image. This ensures the data will persist. 
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v /Users/chasehudsonmahoney/Desktop/2024-DE-course/mod-1-docker-terraform/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    postgres:13

https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

# this creates a container of pgadmin. it's ran on our localhost and accessed via the web. port 8080 on our machine connects with
# port 80 on container
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    dpage/pgadmin4


    # network
    # run the image of postgres on a network so we can connect is to pgadmin. These two have to be on the same network
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v /Users/chasehudsonmahoney/Desktop/2024-DE-course/mod-1-docker-terraform/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 5432:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:13

    # pga admin container on the same network as postgres
docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pgadmin \
    dpage/pgadmin4

    # ingest data with python script and specify params


python ingest_data.py \
    --user=root \
    --password=root \
    --host=localhost \
    --port=5432 \
    --db=ny_taxi \
    --table_name=yellow_taxi_trips \
    --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"

# this command builds a new docker image with correct imports and python file included in the script. 
docker build -t taxi_ingest:v001 . 

# this command runs the docker image that was built in line 71 and uses the correct params, we have to use pg-database
# as the host because that is where the postgres is running. trying to run on localhost port 5432 will produce an error
docker run -it \
    --network=pg-network \
    taxi_ingest:v001 \
        --user=root \
        --password=root \
        --host=pg-database \
        --port=5432 \
        --db=ny_taxi \
        --table_name=yellow_taxi_trips \
        --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"


       