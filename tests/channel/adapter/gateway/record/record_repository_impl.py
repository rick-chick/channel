from channel.adapter.gateway.record.record_repository import (
    RecordRepository
)
from channel.usecase.models import (
    RecordCreateInDsDto,
    RecordCreateOutDsDto,
    RecordDeleteInDsDto,
    RecordDeleteOutDsDto,
    RecordListInDsDto,
    RecordListOutDsDto,
)

from typing import Optional, List


class RecordRepositoryImpl(RecordRepository):

    create_out: RecordCreateOutDsDto

    def list(self, ds_dto: RecordListInDsDto) -> List[RecordListOutDsDto]:
        pass

    def create(self, ds_dto: RecordCreateInDsDto) -> RecordCreateOutDsDto:
        self.create_in = ds_dto
        return self.create_out

    def delete(self, ds_dto: RecordDeleteInDsDto) -> List[RecordDeleteOutDsDto]:
        pass
