from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import DeviceListInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliDeviceListInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> DeviceListInDto:
        if ('args' in self.memory):
            return DeviceListInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return DeviceListInDto(**in_dto.body)
