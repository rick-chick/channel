#!/bin/bash
echo "host: $HOST"
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
ret=`curl -X POST -H "Content-Type: application/json" -d "@$RELATIVE_DIR/authenticate.json" $HOST/user/authenticate`
export token=`python "$RELATIVE_DIR/take_token.py" $ret`
echo $token
