from abc import ABC, abstractmethod
from channel.usecase.models import DeviceAuthenticateOutDto


class DeviceAuthenticateOututPort(ABC):

    @abstractmethod
    def prepare_success_view(self, device: DeviceAuthenticateOutDto) -> DeviceAuthenticateOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
