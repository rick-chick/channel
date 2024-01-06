#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'user_token/cli_user_token_refresh_handler.py'
ret=`python "$file" --json '
  {
    "refresh_token": "'$refresh_token'",
	"user_id": "0e83d5fd-624e-4e58-9e80-273895b4850f"
  }
'`
echo $ret
python "$RELATIVE_DIR/../user/take_token.py" $ret
source ./output_script.sh
