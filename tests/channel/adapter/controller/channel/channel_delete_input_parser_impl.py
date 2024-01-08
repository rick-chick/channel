from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import ChannelDeleteInDto
from tests.channel.factories import ChannelDeleteInDtoFactory


class ChannelDeleteInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> ChannelDeleteInDto:
        print(in_dto)

        return ChannelDeleteInDtoFactory.build()
