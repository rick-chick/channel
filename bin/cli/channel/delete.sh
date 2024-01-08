#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'channel/cli_channel_delete_handler.py'
python "$file" --json '
  {"ids": [9]}
' --token $token
