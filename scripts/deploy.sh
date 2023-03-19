#!/usr/bin/env bash

# Upload cloud function

FUNCTION_NAME=octopus-gbq
REGION=europe-west2

gcloud functions deploy ${FUNCTION_NAME} \
  --gen2 \
  --region=${REGION} \
  --runtime=python310 \
  --source=./ \
  --entry-point=entry_http \
  --trigger-http
