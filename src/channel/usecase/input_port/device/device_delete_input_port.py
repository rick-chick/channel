from abc import ABC, abstractmethod
from channel.usecase.models import (DeviceDeleteInDto, DeviceDeleteOutDto)

from typing import List


class DeviceDeleteInputPort(ABC):

    @abstractmethod
    def delete(self, device_dto: DeviceDeleteInDto) -> DeviceDeleteOutDto:
        pass
