from datetime import datetime
from channel.usecase.models import (
    RecordCreateInDsDto,
    RecordCreateOutDsDto,
    RecordDeleteInDsDto,
    RecordDeleteOutDsDto,
    RecordListInDsDto,
    RecordListOutDsDto,
    RecordOutDsDto,
)

from abc import ABC, abstractmethod
from typing import List, Optional


class RecordRepository(ABC):

    @abstractmethod
    def list(self, ds_dto: RecordListInDsDto) -> List[RecordListOutDsDto]:
        pass

    @abstractmethod
    def create(self, ds_dto: RecordCreateInDsDto) -> RecordCreateOutDsDto:
        pass

    @abstractmethod
    def delete(self, ds_dto: RecordDeleteInDsDto):
        pass

    @abstractmethod
    def exists_by_channel_ids_time(
        self,
        channel_ids: List[int],
        time: datetime
    ) -> bool:
        pass

    @abstractmethod
    def find_latest_by_channel_id(
        self,
        channel_id: int
    ) -> Optional[RecordOutDsDto]:
        pass
