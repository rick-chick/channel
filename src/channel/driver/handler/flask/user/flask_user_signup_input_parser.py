from typing import Any, Dict
from flask import Request
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import UserSignupInDto


class FlaskUserSignupInputParser(InputParser):

    def __init__(self):
        pass

    def parse(self, in_dto: Request) -> UserSignupInDto:
        return UserSignupInDto(**in_dto.get_json())
