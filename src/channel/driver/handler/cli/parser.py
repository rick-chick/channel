import argparse
import json
from typing import Dict, Optional

from pydantic import BaseModel


class ArgsDto(BaseModel):
    body: Dict
    token: Optional[str] = None
    api_key: Optional[str] = None


def parse() -> ArgsDto:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--json", "-j", help="json strings for model", required=True)
    parser.add_argument(
        "--token", "-t", help="jwt token", required=False)
    args = parser.parse_args()
    return ArgsDto(
        body=json.loads(args.json),
        token=args.token
    )
