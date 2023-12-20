from typing import Any, Dict

from flask import Request

from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserTokenAuthenticateInDto


class FlaskUserTokenAuthenticateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: Request) -> UserTokenAuthenticateInDto:
        if (not 'args' in self.memory):
            data = in_dto.get_json()
            self.memory['args'] = data
        if "Authorization" in in_dto.headers:
            token = in_dto.headers["Authorization"].split(" ")[1]
            self.memory['token'] = token
        return UserTokenAuthenticateInDto(token=self.memory['token'])
