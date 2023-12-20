from typing import Any, Dict
from channel.adapter.controller.input_parser import InputParser
from channel.usecase.models import DeviceAuthenticateInDto
from channel.driver.handler.cli.parser import ArgsDto


class CliDeviceAuthenticateInputParser(InputParser):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def parse(self, in_dto: ArgsDto) -> DeviceAuthenticateInDto:
        if ('args' in self.memory):
            return DeviceAuthenticateInDto(**in_dto.body)

        self.memory['args'] = in_dto
        return DeviceAuthenticateInDto(**in_dto.body)
