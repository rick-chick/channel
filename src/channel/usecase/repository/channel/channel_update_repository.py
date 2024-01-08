from abc import ABC, abstractmethod
from channel.usecase.models import (
    ChannelGetOutDsDto,
    ChannelUpdateInDsDto,
    ChannelUpdateOutDsDto,
    UserSessionDsDto,
)

from typing import Optional


class ChannelUpdateRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def find_channel_by_id(
        self,
        id: int
    ) -> Optional[ChannelGetOutDsDto]:
        pass

    @abstractmethod
    def update(
        self,
        channel: ChannelUpdateInDsDto
    ) -> Optional[ChannelUpdateOutDsDto]:
        pass
