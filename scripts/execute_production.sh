#!/usr/bin/env bash

DATE=$1

FUNCTION_NAME=octopus-gbq
REGION=europe-west2

if [ "${DATE}" != "" ]; then
  echo "Using date: ${DATE}"
  gcloud functions call ${FUNCTION_NAME} --region=${REGION} --gen2 --data "{\"date\":\"${DATE}\"}"
else
  gcloud functions call ${FUNCTION_NAME} --region=${REGION} --gen2
fi
