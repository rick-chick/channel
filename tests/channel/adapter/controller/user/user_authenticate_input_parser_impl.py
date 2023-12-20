from channel.usecase.models import UserAuthenticateInDto
from channel.adapter.controller.input_parser import InputParser

from typing import Any


class UserAuthenticateInputParserImpl(InputParser):

    parse_out: UserAuthenticateInDto
    parse_in: Any

    def parse(self, in_dto: Any) -> UserAuthenticateInDto:
        self.parse_in = in_dto
        return self.parse_out
