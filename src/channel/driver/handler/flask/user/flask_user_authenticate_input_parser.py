from typing import Any, Dict
import json
from flask import Request
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserAuthenticateInDto


class FlaskUserAuthenticateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: Request) -> UserAuthenticateInDto:
        if (not 'args' in self.memory):
            data = in_dto.get_json()
            self.memory['args'] = data
        return UserAuthenticateInDto(**self.memory['args'])
