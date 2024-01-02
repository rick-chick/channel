#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'device/cli_device_list_handler.py'
python "$file" --json '
  {
    "user_id": "1"
  }
' --token $token
