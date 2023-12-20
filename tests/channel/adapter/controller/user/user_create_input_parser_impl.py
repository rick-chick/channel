from channel.usecase.models import UserCreateInDto
from channel.adapter.controller.input_parser import InputParser
from tests.channel.factories import UserCreateInDtoFactory

from typing import Any


class UserCreateInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> UserCreateInDto:
        print(in_dto)
        return UserCreateInDtoFactory.build()
