# octopus-gbq-cloud-function
Import Octopus Energy data into Google BigQuery

## Requirements

* pyenv

## Install

```
scripts/setup_python.sh
scripts/install.sh
```

Setup Gcloud auth:

```
gcloud auth application-default login
```

Create tables in Google BigQuery:

```
bq mk --dataset --description="Energy usage" --location=EU energy_usage
GOOGLE_PROJECT=yourproject python src/create_tables.py
```

Google BigQuery Permissions:

Grant `BigQuery Data Editor` to the function's service account on the dataset created above.


Add cloud function permissions to service account:

```
gcloud projects add-iam-policy-binding dumb-1 --member serviceAccount:serviceaccount@yourproject.iam.gserviceaccount.com --role roles/cloudfunctions.invoker
```

## Development

To run the cloud function as a local web server:

```
functions-framework --source ./main.py --target entry_http --debug
```

Then to get data for yesterday:

```
scripts/execute_dev.sh
```

Or to get data for a specific day:

```
scripts/execute_dev.sh 2023-03-01
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

### Manual execution

To get data for yesterday:

```
scripts/execute_production.sh
```

Or to get data for a specific day:

```
scripts/execute_production.sh 2023-03-01
```

## TODO

* Document secret setup

* Document env var setup

* Document cloud function setup

* Fix permissions so scheduler can run function

