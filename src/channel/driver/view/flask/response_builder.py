import json
from typing import Any, List
from pydantic import BaseModel


class ResponseBuilder():

    def __init__(self, result: Any, exceptions: List[Exception]):
        self.exceptions = exceptions
        self.result = result

    def json(self) -> str:
        if len(self.exceptions) > 0:
            return json.dumps(
                {
                    "code": str(self.exceptions[0])
                }
            )
        if (isinstance(self.result, BaseModel)):
            return self.result.model_dump_json()
        raise Exception('cant_parse_body')
