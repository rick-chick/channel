from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import ChannelDeleteInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliChannelDeleteInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> ChannelDeleteInDto:
        if ('args' in self.memory):
            return ChannelDeleteInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return ChannelDeleteInDto(**in_dto.body)
