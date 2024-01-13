from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserResetPasswordInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliUserResetPasswordInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> UserResetPasswordInDto:
        if ('args' in self.memory):
            return UserResetPasswordInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return UserResetPasswordInDto(**in_dto.body)
