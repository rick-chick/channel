from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserTokenAuthenticateInDto


class UserTokenAuthenticateInputParserImpl(InputParser):

    parse_out: UserTokenAuthenticateInDto
    
    def parse(self, in_dto: Any) -> UserTokenAuthenticateInDto:
        print(in_dto)
        return self.parse_out
