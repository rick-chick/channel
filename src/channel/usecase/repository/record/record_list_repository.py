from abc import ABC, abstractmethod
from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    RecordListInDsDto,
    RecordListOutDsDto,
    UserSessionDsDto
)

from typing import List, Optional

class RecordListRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def list(
        self,
        record_dto: RecordListInDsDto
    ) -> List[RecordListOutDsDto]:
        pass


    @abstractmethod
    def channel_list(
        self,
        channel_dto: ChannelListInDsDto
    ) -> List[ChannelListOutDsDto]:
        pass
