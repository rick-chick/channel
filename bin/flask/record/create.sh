#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
ret=`curl -X POST -H "Content-Type: application/json" -d "@$RELATIVE_DIR/create.json" $HOST/record`
echo $ret
