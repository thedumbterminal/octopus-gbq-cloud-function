from octopus_energy_client import OctopusEnergy, ResourceType, Aggregate
from datetime import datetime
from google.cloud import bigquery

octopus_client = OctopusEnergy()
bigquery_client = bigquery.Client()


def consumption_from_response(response):
    print(response)
    if response["count"] == 0:
        return
    return response["results"][0]["consumption"]


def elec_for_day(when):
    electricity_consumption = octopus_client.get_consumption_for_date(
        ResourceType.ELECTRICITY, when, group_by=Aggregate.DAILY
    )
    return consumption_from_response(electricity_consumption)


def gas_for_day(when):
    gas_consumption = octopus_client.get_consumption_for_date(
        ResourceType.GAS, when, group_by=Aggregate.DAILY
    )
    return consumption_from_response(gas_consumption)


def insert_row_into_table(table, row):
    print(table, row)
    bigquery_client.insert_rows_json(table, [row])


def save_elec(when, usage):
    row_to_insert = {
        "date": when.isoformat(),
        "usage": usage,
        "updated": datetime.now().isoformat(),
    }
    table_id = "energy_usage.octopus_electricity"
    insert_row_into_table(table_id, row_to_insert)


def save_gas(when, usage):
    row_to_insert = {
        "date": when.isoformat(),
        "usage": usage,
        "updated": datetime.now().isoformat(),
    }
    table_id = "energy_usage.octopus_gas"
    insert_row_into_table(table_id, row_to_insert)
