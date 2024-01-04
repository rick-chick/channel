from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import DeviceDeleteInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliDeviceDeleteInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> DeviceDeleteInDto:
        if ('args' in self.memory):
            return DeviceDeleteInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return DeviceDeleteInDto(**in_dto.body)
