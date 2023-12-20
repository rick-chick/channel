from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import RecordCreateInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliRecordCreateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> RecordCreateInDto:
        if ('args' in self.memory):
            return RecordCreateInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return RecordCreateInDto(**in_dto.body)
