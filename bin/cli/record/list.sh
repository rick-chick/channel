#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'record/cli_record_list_handler.py'
current_datetime=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
python "$file" --json '
  {
    "device_id": 1,
    "date_from": "2023-12-22T00:00:00",
    "date_to": "2023-12-23T00:00:00"
  }
' --token $token
