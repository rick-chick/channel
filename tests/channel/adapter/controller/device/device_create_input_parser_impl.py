from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import DeviceCreateInDto

from tests.channel.factories import DeviceCreateInDtoFactory


class DeviceCreateInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> DeviceCreateInDto:
        self.in_dto = in_dto
        return DeviceCreateInDtoFactory.build()
