from abc import ABC, abstractmethod
from channel.usecase.models import DeviceCreateOutDto


class DeviceCreateOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, device: DeviceCreateOutDto) -> DeviceCreateOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
