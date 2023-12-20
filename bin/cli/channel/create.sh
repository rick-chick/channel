#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'channel/cli_channel_create_handler.py'
python "$file" --json '
  {
    "name": "照度",
    "unit": "V",
    "device_id": "1"
  }
' --token $token
