from abc import ABC, abstractmethod
from channel.usecase.models import (
    DeviceSessionDsDto,
    RecordCreateInDsDto,
    RecordCreateOutDsDto,
    UserSessionDsDto,
)
from typing import Optional


class RecordCreateRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def create(self, record: RecordCreateInDsDto) -> RecordCreateOutDsDto:
        pass

    @abstractmethod
    def load_session_device(self) -> Optional[DeviceSessionDsDto]:
        pass
