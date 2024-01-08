#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
ret=`curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer $token" -d "@$RELATIVE_DIR/update.json" $HOST/channel`
echo $ret
