#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'record/cli_record_create_handler.py'
current_datetime=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
python "$file" --json '
  {
    "api_key": "4f7ec8b8-0dcd-4def-869e-4046e4d68a43",
    "time": "'$current_datetime'",
    "values": {
      "1": "23.5",
      "2": "43.2",
      "3": "1.5"
    }
  }
' --token $token
