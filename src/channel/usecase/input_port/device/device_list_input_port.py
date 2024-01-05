from abc import ABC, abstractmethod
from channel.usecase.models import (
    DeviceListInDto, DeviceListOutDto)


class DeviceListInputPort(ABC):

    @abstractmethod
    def list(self, device_dto: DeviceListInDto) -> DeviceListOutDto:
        pass
