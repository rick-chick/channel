from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserCreateInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliUserCreateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> UserCreateInDto:
        if ('args' in self.memory):
            return UserCreateInDto(**self.memory['args'].body)

        self.memory['args'] = in_dto
        return UserCreateInDto(**in_dto.body)
