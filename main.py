import functions_framework
from datetime import datetime, timedelta, date
from .src.consumption import elec_for_day, save_elec, gas_for_day, save_gas


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
