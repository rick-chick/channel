#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../src/channel/driver/handler/flask'
file=$dir'/handler.py'
python "$file"
