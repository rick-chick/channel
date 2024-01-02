from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import DeviceListInDto
from tests.channel.factories import DeviceListInDtoFactory


class DeviceListInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> DeviceListInDto:
        print(in_dto)

        return DeviceListInDtoFactory.build()
