from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import DeviceCreateInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliDeviceCreateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> DeviceCreateInDto:
        if ('args' in self.memory):
            return DeviceCreateInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return DeviceCreateInDto(**in_dto.body)
