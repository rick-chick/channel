from abc import ABC, abstractmethod

from channel.usecase.models import DeviceAuthenticateInDto, DeviceAuthenticateOutDto


class DeviceAuthenticateInputPort(ABC):

    @abstractmethod
    def authenticate(self, device_dto: DeviceAuthenticateInDto) -> DeviceAuthenticateOutDto:
        pass
