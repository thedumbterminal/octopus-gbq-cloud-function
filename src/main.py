import functions_framework
from octopus_energy_client import OctopusEnergy, ResourceType, ChargeType, Aggregate
from datetime import datetime, timedelta, date




@functions_framework.http
def entry_http(request):
    """
    HTTP Cloud Function.
    """
    
    request_args = request.args
    print(request_args)
    
    octopus_client = OctopusEnergy(
        api_key=octopus_api_key,
        electricity_serial=octopus_electricity_serial,
        electricity_mpan=octopus_electricity_mpan,
        electricity_product_code=octopus_electricity_product_code,
        electricity_region=octopus_electricity_region,
        gas_serial=octopus_gas_serial,
        gas_mprn=octopus_gas_mprn,
        gas_product_code=octopus_gas_product_code,
        gas_region=octopus_gas_region,
    )

    when = datetime.now() - timedelta(days = 1)
    if request_args['date']:
        when = date.fromisoformat(request_args['date'])
    print('Running for date: ', when)

    electricity_consumption = octopus_client.get_consumption_for_date(ResourceType.ELECTRICITY, when, group_by=Aggregate.DAILY)


    return electricity_consumption
