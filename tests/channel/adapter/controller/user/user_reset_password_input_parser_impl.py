from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserResetPasswordInDto
from tests.channel.factories import UserResetPasswordInDtoFactory


class UserResetPasswordInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> UserResetPasswordInDto:
        print(in_dto)

        return UserResetPasswordInDtoFactory.build()
