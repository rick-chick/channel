from channel.usecase.models import (
    DeviceSessionDsDto
)

from abc import ABC, abstractmethod
from typing import Optional


class DeviceSession(ABC):

    @abstractmethod
    def save(self, device_session_ds_dto: DeviceSessionDsDto):
        pass

    @abstractmethod
    def load(self) -> Optional[DeviceSessionDsDto]:
        pass
