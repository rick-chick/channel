#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
ret=`curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $token" -d "@$RELATIVE_DIR/list.json" $HOST/records`
echo $ret
