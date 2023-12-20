from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserTokenAuthenticateInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliUserTokenAuthenticateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> UserTokenAuthenticateInDto:
        if ('args' in self.memory):
            return UserTokenAuthenticateInDto(token=self.memory['args'].token)

        self.memory['args'] = in_dto
        if in_dto.token:
            return UserTokenAuthenticateInDto(token = in_dto.token)

        raise Exception('missing token')
