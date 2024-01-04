from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import DeviceDeleteInDto
from tests.channel.factories import DeviceDeleteInDtoFactory


class DeviceDeleteInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> DeviceDeleteInDto:
        print(in_dto)

        return DeviceDeleteInDtoFactory.build()
