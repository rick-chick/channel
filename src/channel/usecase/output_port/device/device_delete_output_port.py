from abc import ABC, abstractmethod

from channel.usecase.models import DeviceDeleteOutDto


class DeviceDeleteOututPort(ABC):

    @abstractmethod
    def prepare_success_view(
        self, device_dto: DeviceDeleteOutDto
    ) -> DeviceDeleteOutDto:
        pass

    @abstractmethod
    def prepare_fail_view(self, exception: Exception):
        pass
