from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import ChannelUpdateInDto
from tests.channel.factories import ChannelUpdateInDtoFactory


class ChannelUpdateInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> ChannelUpdateInDto:
        print(in_dto)

        return ChannelUpdateInDtoFactory.build()
