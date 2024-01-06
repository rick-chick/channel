from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserTokenRefreshInDto
from tests.channel.factories import UserTokenRefreshInDtoFactory


class UserTokenRefreshInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> UserTokenRefreshInDto:
        print(in_dto)

        return UserTokenRefreshInDtoFactory.build()
