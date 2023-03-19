# octopus-gbq-cloud-function
Import Octopus Energy data into Google BigQuery

## Requirements

* pyenv

## Install

```
scripts/setup_python.sh
scripts/install.sh
```

Create tables in Google BigQuery:

```
 bq mk --dataset --description="Energy usage" --location=EU energy_usage
GOOGLE_PROJECT=yourproject python src/create_tables.py
```

Setup Gcloud auth:

```
gcloud auth application-default login
```

## Development

To run the cloud function as a local web server:

```
functions-framework --source ./main.py --target entry_http --debug
```

Then to get data for yesterday:

```
curl -v http://localhost:8080/
```

Or to get data for a specific day:

```
curl "http://localhost:8080/?date=2023-03-01"
```

### Environment variables

* OCTOPUS_API_KEY
* OCTOPUS_ELECTRICITY_SERIAL
* OCTOPUS_ELECTRICITY_MPAN
* OCTOPUS_GAS_SERIAL
* OCTOPUS_GAS_MPRN

The values to the above variables can be found at:

https://octopus.energy/dashboard/developer/

## Deployment

```
scripts/deploy.sh
```
