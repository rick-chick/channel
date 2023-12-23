#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'user/cli_user_authenticate_handler.py'
ret=`python "$file" --json '
  {
    "email": "test@admin.com",
    "password": "test@admin.pass"
  }
'`
export token=`python "$RELATIVE_DIR/take_token.py" $ret`
echo $token
