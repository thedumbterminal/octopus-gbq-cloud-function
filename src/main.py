import functions_framework
from octopus_energy_client import OctopusEnergy, ResourceType, ChargeType, Aggregate
from datetime import datetime, timedelta, date
from google.cloud import bigquery

octopus_client = OctopusEnergy()
bigquery_client = bigquery.Client()

def consumption_from_response(response):
    return response['results'][0]['consumption']

def elec_for_day(when):
    electricity_consumption = octopus_client.get_consumption_for_date(ResourceType.ELECTRICITY, when, group_by=Aggregate.DAILY)
    return consumption_from_response(electricity_consumption)

def gas_for_day(when):
    gas_consumption = octopus_client.get_consumption_for_date(ResourceType.GAS, when, group_by=Aggregate.DAILY)
    return consumption_from_response(gas_consumption)

def save_elec(when, usage):
    row_to_insert={
        'date': when.isoformat(),
        'usage': usage,
        'updated': datetime.now().isoformat()
    }
    print(row_to_insert)
    table_id='energy_usage.octopus_electricity'
    bigquery_client.insert_rows_json(table_id, [row_to_insert])

def save_gas(when, usage):
    row_to_insert={
        'date': when.isoformat(),
        'usage': usage,
        'updated': datetime.now().isoformat()
    }
    print(row_to_insert)
    table_id='energy_usage.octopus_gas'
    bigquery_client.insert_rows_json(table_id, [row_to_insert])


@functions_framework.http
def entry_http(request):
    """
    HTTP Cloud Function.
    """
    
    request_args = request.args

    when = datetime.now() - timedelta(days = 1)
    if request_args['date']:
        when = date.fromisoformat(request_args['date'])
    print('Running for date: ', when)

    elec_amount = elec_for_day(when)
    save_elec(when, elec_amount)
    gas_amount = gas_for_day(when)
    save_gas(when, gas_amount)

    return f'Elec amount: {elec_amount}, Gas amount: {gas_amount}'

