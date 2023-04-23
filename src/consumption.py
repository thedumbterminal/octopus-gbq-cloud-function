from octopus_energy_client import OctopusEnergy, ResourceType, Aggregate
from datetime import datetime
from google.cloud import bigquery

octopus_client = OctopusEnergy()
bigquery_client = bigquery.Client()


def consumption_from_response(response):
    print(response)
    if response["count"] == 0:
        return 0
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


def insert_row_into_table(table, when, usage):
    row = {
        "date": when.strftime('%Y-%m-%d'),
        "usage": usage,
        "updated": datetime.utcnow().isoformat(),
    }
    print(table, row)
    errors = bigquery_client.insert_rows_json(table, [row])
    if errors != []:
        print(errors[0])
        raise Exception(errors[0]['errors'])


def save_elec(when, usage):
    table_id = "energy_usage.octopus_electricity"
    insert_row_into_table(table_id, when, usage)


def save_gas(when, usage):
    table_id = "energy_usage.octopus_gas"
    insert_row_into_table(table_id, when, usage)
