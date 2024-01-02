from typing import Any, Dict
from flask import Request
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import ChannelListInDto


class FlaskChannelListInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: Request) -> ChannelListInDto:
        if (not 'args' in self.memory):
            data = in_dto.get_json()
            self.memory['args'] = data
        return ChannelListInDto(**self.memory['args'])
