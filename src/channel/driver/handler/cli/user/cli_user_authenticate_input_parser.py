from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserAuthenticateInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliUserAuthenticateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> UserAuthenticateInDto:
        if ('args' in self.memory):
            return UserAuthenticateInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return UserAuthenticateInDto(**in_dto.body)
