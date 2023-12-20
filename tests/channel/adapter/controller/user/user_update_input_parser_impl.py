from channel.usecase.models import UserUpdateInDto
from channel.adapter.controller.input_parser import InputParser
from tests.channel.factories import UserUpdateInDtoFactory

from typing import Any


class UserUpdateInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> UserUpdateInDto:
        print(in_dto)
        return UserUpdateInDtoFactory.build()
