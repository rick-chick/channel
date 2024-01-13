from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserSignupInDto
from tests.channel.factories import UserSignupInDtoFactory


class UserSignupInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> UserSignupInDto:
        print(in_dto)

        return UserSignupInDtoFactory.build()
