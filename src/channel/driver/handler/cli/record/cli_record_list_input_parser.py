from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import RecordListInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliRecordListInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> RecordListInDto:
        if ('args' in self.memory):
            return RecordListInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return RecordListInDto(**in_dto.body)
