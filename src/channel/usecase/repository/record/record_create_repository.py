from abc import ABC, abstractmethod
from datetime import datetime
from channel.usecase.models import (
    DeviceSessionDsDto,
    RecordCreateInDsDto,
    RecordCreateOutDsDto,
    UserSessionDsDto,
)
from typing import List, Optional


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

    @abstractmethod
    def exists_record_by_channel_ids_time(
        self,
        channel_ids: List[int],
        time: datetime
    ) -> bool:
        pass
