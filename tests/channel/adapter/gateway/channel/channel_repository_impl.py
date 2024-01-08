from channel.adapter.gateway.channel.channel_repository import (
    ChannelRepository
)
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

from typing import Optional, List

from tests.channel.factories import ChannelGetOutDsDtoFactory, ChannelUpdateOutDsDtoFactory


class ChannelRepositoryImpl(ChannelRepository):

    create_out: ChannelCreateOutDsDto
    list_out: List[ChannelListOutDsDto] = []

    def exists_by_id(self, id: Optional[int]) -> bool:
        return False

    def exists_by_code(self, code: str, except_id: Optional[int]) -> bool:
        return False

    def find_by_id(self, id: Optional[int]) -> Optional[ChannelGetOutDsDto]:
        return ChannelGetOutDsDtoFactory.build()

    def list(self, ds_dto: ChannelListInDsDto) -> List[ChannelListOutDsDto]:
        self.ds_dto_in = ds_dto
        return self.list_out

    def create(self, ds_dto: ChannelCreateInDsDto) -> ChannelCreateOutDsDto:
        self.create_in = ds_dto
        return self.create_out

    def update(
        self,
        ds_dto: ChannelUpdateInDsDto
    ) -> Optional[ChannelUpdateOutDsDto]:
        return ChannelUpdateOutDsDtoFactory.build()

    def delete(self, ds_dto: ChannelDeleteInDsDto) -> List[ChannelDeleteOutDsDto]:
        return []
