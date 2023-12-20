from abc import ABC, abstractmethod
from channel.usecase.models import (
        DeviceCreateInDto, DeviceCreateOutDto)


class DeviceCreateInputPort(ABC):

    @abstractmethod
    def create(self, device_dto: DeviceCreateInDto) -> DeviceCreateOutDto:
        pass
