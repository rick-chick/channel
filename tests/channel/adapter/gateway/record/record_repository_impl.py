from datetime import datetime
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
    RecordOutDsDto,
)

from typing import List, Optional


class RecordRepositoryImpl(RecordRepository):

    create_out: RecordCreateOutDsDto

    def list(self, ds_dto: RecordListInDsDto) -> List[RecordListOutDsDto]:
        return []

    def create(self, ds_dto: RecordCreateInDsDto) -> RecordCreateOutDsDto:
        self.create_in = ds_dto
        return self.create_out

    def delete(self, ds_dto: RecordDeleteInDsDto):
        pass

    def exists_by_channel_ids_time(
        self,
        channel_ids: List[int],
        time: datetime
    ) -> bool:
        return False

    def find_latest_by_channel_id(
        self,
        channel_id: int
    ) -> Optional[RecordOutDsDto]:
        return None
