from abc import ABC, abstractmethod
from channel.usecase.models import (
    ChannelDeleteInDsDto,
    ChannelDeleteOutDsDto,
    UserSessionDsDto
)

from typing import List, Optional


class ChannelDeleteRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def delete(
        self,
        channel_dto: ChannelDeleteInDsDto
    ) -> List[ChannelDeleteOutDsDto]:
        pass
