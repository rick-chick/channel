#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
ret=`curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer $token" -d "@$RELATIVE_DIR/delete.json" $HOST/device`
echo $ret
