#!/bin/bash
echo "host: $HOST"
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
ret=`curl -X POST -H "Content-Type: application/json" -d "@$RELATIVE_DIR/reset_password.json" $HOST/user/reset_password`
echo $ret
