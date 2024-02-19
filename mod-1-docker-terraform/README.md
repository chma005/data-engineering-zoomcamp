Module 1 Docs:
Step 1 run below commmand in terminal in directory where Dockerfile is
# this command builds a new docker image with correct imports and 
# python file included in the script. Review the Dockerfile in this directory to see what is built.
docker build -t taxi_ingest:v001 . 

# Ensure image exists: 
docker image ls

Step 2: In terminal run the below: 
# This will run images described in docker-compose.yaml. Review this file. IMPORTANT NOTE: Leave this running in terminal
# and open new terminal for step 3. This must be running in order to write to postgresql db. 
# Open pgadmin using the username and password described in .yaml file. This is just a GUI to interact
# with postgresql db
# pgadmin is running on port described in .yaml file. In web browser enter localhost:8080 to access
docker compose up

Step 3: open a new terminal in directory where Dockerfile exists. copy and past below into terminal
# this command runs the docker image that was built in line 5 and defines the params that are called in the ingest_data.py
# must define --network to work. The reason because we have to tell docker file where our postgres db persists.
# host  is localhost because that is where the postgres is running. We define port 5432 in our docker compose file
docker run -it \
    --network="host" \
    taxi_ingest:v001 \
        --user=root \
        --password=root \
        --host=localhost \
        --port=5432 \
        --db=ny_taxi \
        --table_name=yellow_taxi_trips \
        --url="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2021-01.csv.gz"


       