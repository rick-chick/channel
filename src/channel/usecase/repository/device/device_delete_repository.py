from abc import ABC, abstractmethod
from channel.usecase.models import (
    ChannelDeleteInDsDto,
    ChannelDeleteOutDsDto,
    DeviceDeleteInDsDto,
    DeviceDeleteOutDsDto,
    RecordDeleteInDsDto,
    RecordDeleteOutDsDto,
    UserSessionDsDto
)

from typing import List, Optional


class DeviceDeleteRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def delete_channel(
        self,
        channel_dto: ChannelDeleteInDsDto
    ) -> List[ChannelDeleteOutDsDto]:
        pass

    @abstractmethod
    def delete_record(
        self,
        record_dto: RecordDeleteInDsDto
    ) -> List[RecordDeleteOutDsDto]:
        pass

    @abstractmethod
    def delete(
        self,
        device_dto: DeviceDeleteInDsDto
    ) -> List[DeviceDeleteOutDsDto]:
        pass
