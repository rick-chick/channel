from abc import ABC, abstractmethod
from channel.usecase.models import (
    ChannelCreateInDsDto,
    ChannelCreateOutDsDto,
    UserSessionDsDto,
)

from typing import Optional


class ChannelCreateRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def create(self, channel: ChannelCreateInDsDto) -> ChannelCreateOutDsDto:
        pass
