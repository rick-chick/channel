#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
ret=`curl -X POST -H "Content-Type: application/json" -d "@$RELATIVE_DIR/authenticate.json" $HOST/user/authenticate`
echo $ret
export token=`python "take_token.py" $ret`
echo $token
