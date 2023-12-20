from channel.usecase.models import (
    RecordCreateInDsDto,
    RecordCreateOutDsDto,
    RecordDeleteInDsDto,
    RecordDeleteOutDsDto,
    RecordListInDsDto,
    RecordListOutDsDto,
)

from abc import ABC, abstractmethod
from typing import List


class RecordRepository(ABC):

    @abstractmethod
    def list(self, ds_dto: RecordListInDsDto) -> List[RecordListOutDsDto]:
        pass

    @abstractmethod
    def create(self, ds_dto: RecordCreateInDsDto) -> RecordCreateOutDsDto:
        pass

    @abstractmethod
    def delete(self, ds_dto: RecordDeleteInDsDto) -> List[RecordDeleteOutDsDto]:
        pass
