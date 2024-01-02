from abc import ABC, abstractmethod
from channel.usecase.models import DeviceListOutDto


class DeviceListOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, device: DeviceListOutDto) -> DeviceListOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
