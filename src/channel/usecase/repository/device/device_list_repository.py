from abc import ABC, abstractmethod
from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    ChannelListOutDto,
    DeviceListInDsDto,
    DeviceListOutDsDto,
    UserSessionDsDto
)

from typing import List, Optional


class DeviceListRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def list(
        self,
        device_dto: DeviceListInDsDto
    ) -> List[DeviceListOutDsDto]:
        pass

    @abstractmethod
    def list_channel(
        self,
        channel_dto: ChannelListInDsDto
    ) -> List[ChannelListOutDsDto]:
        pass
