from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import DeviceAuthenticateInDto

from tests.channel.factories import DeviceAuthenticateInDtoFactory


class DeviceAuthenticateInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> DeviceAuthenticateInDto:
        self.in_dto = in_dto
        return DeviceAuthenticateInDtoFactory.build()
