from typing import Any
from channel.adapter.controller.input_parser import InputParser
from tests.channel.factories import ChannelCreateInDtoFactory


class ChannelCreateInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> Any:
        print(in_dto)
        return ChannelCreateInDtoFactory.build()
    
