#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'channel/cli_channel_update_handler.py'
python "$file" --json '
  {
    "id": "33",
    "name": "照度"
  }
' --token $token
