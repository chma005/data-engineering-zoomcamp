import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/ny-rides-chaybang-49ef32a4b790.json"

bucket_name = 'mage-zoomcamp-chaybang'
project_id = 'ny-rides-chaybang'

table_name = "2022_green_taxi"

root_path = f"{bucket_name}/{table_name}"


@data_exporter
def export_data(data, *args, **kwargs):
    
    table = pa.Table.from_pandas(data)
    
    gcs = pa.fs.GcsFileSystem()

    pq.write_to_dataset(
        table,
        root_path=root_path,
        filesystem=gcs,
        use_deprecated_int96_timestamps=True
    )