import functions_framework
from octopus_energy_client import OctopusEnergy, ResourceType, ChargeType, Aggregate
from datetime import datetime, timedelta, date

octopus_client = OctopusEnergy()

def consumption_from_response(response):
    return response['results'][0]['consumption']

def elec_for_day(when):
    electricity_consumption = octopus_client.get_consumption_for_date(ResourceType.ELECTRICITY, when, group_by=Aggregate.DAILY)
    return consumption_from_response(electricity_consumption)

def gas_for_day(when):
    gas_consumption = octopus_client.get_consumption_for_date(ResourceType.GAS, when, group_by=Aggregate.DAILY)
    return consumption_from_response(gas_consumption)


@functions_framework.http
def entry_http(request):
    """
    HTTP Cloud Function.
    """
    
    request_args = request.args
    print(request_args)

    when = datetime.now() - timedelta(days = 1)
    if request_args['date']:
        when = date.fromisoformat(request_args['date'])
    print('Running for date: ', when)

    elec_amount = elec_for_day(when)
    gas_amount = gas_for_day(when)

    return f'Elec amount: {elec_amount}, Gas amount: {gas_amount}'

