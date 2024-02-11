FROM python:3.10.13

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2

WORKDIR /app

COPY ingest_hw_data.py ingest_hw_data.py

ENTRYPOINT [ "python", "ingest_hw_data.py" ]