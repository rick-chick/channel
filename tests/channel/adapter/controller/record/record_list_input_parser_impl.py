from typing import Any
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import RecordListInDto
from tests.channel.factories import RecordListInDtoFactory


class RecordListInputParserImpl(InputParser):

    def parse(self, in_dto: Any) -> RecordListInDto:
        print(in_dto)

        return RecordListInDtoFactory.build()
