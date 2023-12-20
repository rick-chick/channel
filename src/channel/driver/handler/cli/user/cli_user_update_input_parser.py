from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserUpdateInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliUserUpdateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> UserUpdateInDto:
        if ('args' in self.memory):
            return UserUpdateInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return UserUpdateInDto(**in_dto.body)
