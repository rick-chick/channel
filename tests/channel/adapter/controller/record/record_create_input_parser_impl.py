from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import RecordCreateInDto
from tests.channel.factories import RecordCreateInDtoFactory


class RecordCreateInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> RecordCreateInDto:
        print(in_dto)

        return RecordCreateInDtoFactory.build()
