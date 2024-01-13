#!/bin/bash
RELATIVE_DIR="$( cd "$(dirname "${BASH_SOURCE[0]}" )" && pwd)"
dir=$RELATIVE_DIR'/../../../src/channel/driver/handler/cli/'
file=$dir'user/cli_user_reset_password_handler.py'
python "$file" --json '
  {
    "token": "25b538410a2831f94095a547802ad4aa03d41468e7df8d5682d37a5b5f560622",
    "password": "hogehuga"
  }
'
