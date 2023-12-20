from channel.usecase.models import (
    ChannelGetOutDsDto,
    ChannelCreateInDsDto,
    ChannelCreateOutDsDto,
    ChannelUpdateInDsDto,
    ChannelUpdateOutDsDto,
    ChannelDeleteInDsDto,
    ChannelDeleteOutDsDto,
    ChannelListInDsDto,
    ChannelListOutDsDto,
)

from abc import ABC, abstractmethod
from typing import Optional, List


class ChannelRepository(ABC):

    @abstractmethod
    def exists_by_id(self, id: Optional[int]) -> bool:
        pass

    @abstractmethod
    def find_by_id(self, id: Optional[int]) -> Optional[ChannelGetOutDsDto]:
        pass

    @abstractmethod
    def list(self, ds_dto: ChannelListInDsDto) -> List[ChannelListOutDsDto]:
        pass

    @abstractmethod
    def create(self, ds_dto: ChannelCreateInDsDto) -> ChannelCreateOutDsDto:
        pass

    @abstractmethod
    def update(self, ds_dto: ChannelUpdateInDsDto) -> Optional[ChannelUpdateOutDsDto]:
        pass

    @abstractmethod
    def delete(self, ds_dto: ChannelDeleteInDsDto) -> List[ChannelDeleteOutDsDto]:
        pass
