from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserSignupInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliUserSignupInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> UserSignupInDto:
        if ('args' in self.memory):
            return UserSignupInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return UserSignupInDto(**in_dto.body)
