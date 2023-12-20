from abc import ABC, abstractmethod
from channel.usecase.models import (
    DeviceCreateInDsDto,
    DeviceCreateOutDsDto,
    UserSessionDsDto
)

from typing import Optional


class DeviceCreateRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def create(self, device: DeviceCreateInDsDto) -> DeviceCreateOutDsDto:
        pass
