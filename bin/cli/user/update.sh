#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'user/cli_user_update_handler.py'
python "$file" --json '
  {
    "id": "0e83d5fd-624e-4e58-9e80-273895b4850f",
    "email": "test@admin.com",
    "password": "test@admin.pass"
  }
' --token $token
