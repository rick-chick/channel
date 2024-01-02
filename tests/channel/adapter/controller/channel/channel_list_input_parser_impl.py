from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import ChannelListInDto
from tests.channel.factories import ChannelListInDtoFactory


class ChannelListInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> ChannelListInDto:
        print(in_dto)

        return ChannelListInDtoFactory.build()
