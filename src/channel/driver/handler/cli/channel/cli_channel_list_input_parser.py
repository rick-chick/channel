from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import ChannelListInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliChannelListInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> ChannelListInDto:
        if ('args' in self.memory):
            return ChannelListInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return ChannelListInDto(**in_dto.body)
