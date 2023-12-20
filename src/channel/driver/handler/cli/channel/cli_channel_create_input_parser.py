from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import ChannelCreateInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliChannelCreateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> ChannelCreateInDto:
        if ('args' in self.memory):
            return ChannelCreateInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return ChannelCreateInDto(**in_dto.body)
