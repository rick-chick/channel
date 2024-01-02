from abc import ABC, abstractmethod
from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    DeviceListInDsDto,
    DeviceListOutDsDto,
    UserSessionDsDto
)

from typing import Optional, List


class ChannelListRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def list(
        self,
        channel_dto: ChannelListInDsDto
    ) -> List[ChannelListOutDsDto]:
        pass

    @abstractmethod
    def list_device(
        self,
        device_dto: DeviceListInDsDto
    ) -> List[DeviceListOutDsDto]:
        pass
