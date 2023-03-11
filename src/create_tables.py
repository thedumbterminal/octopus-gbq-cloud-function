from google.cloud import bigquery
from os import environ

client = bigquery.Client()

project_id = environ["GOOGLE_PROJECT"]

schema = [
    bigquery.SchemaField("date", "DATE", mode="REQUIRED"),
    bigquery.SchemaField("updated", "TIMESTAMP", mode="REQUIRED"),
    bigquery.SchemaField("usage", "DECIMAL", mode="REQUIRED"),
]

table_ids = [
    "energy_usage.octopus_electricity",
    "energy_usage.octopus_gas"
]

for table_id in table_ids:
    full_table_id=f'{project_id}.{table_id}'
    table = bigquery.Table(full_table_id, schema=schema)
    table_result = client.create_table(table)  # Make an API request.
    print(
        "Created table {}.{}.{}".format(table_result.project, table_result.dataset_id, table_result.table_id)
    )
