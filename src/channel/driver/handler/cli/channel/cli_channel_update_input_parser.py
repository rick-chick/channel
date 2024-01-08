from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import ChannelUpdateInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliChannelUpdateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> ChannelUpdateInDto:
        if ('args' in self.memory):
            return ChannelUpdateInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return ChannelUpdateInDto(**in_dto.body)
