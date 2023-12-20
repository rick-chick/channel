#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'user/cli_user_create_handler.py'
python "$file" --json '
  {
    "email": "hoge@admin.com",
    "password": "hoge@admin.pass"
  }
' --token $token
