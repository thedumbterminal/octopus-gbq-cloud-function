#!/usr/bin/env bash

DATE=$1

if [ "${DATE}" != "" ]; then
  echo "Using date: ${DATE}"
  curl -v http://localhost:8080/ \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2023-03-01"
  }'
else
  curl -v http://localhost:8080/
fi
