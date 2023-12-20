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


class ChannelRepositoryImpl(ChannelRepository):

    create_out: ChannelCreateOutDsDto

    def exists_by_id(self, id: Optional[int]) -> bool:
        pass

    def exists_by_code(self, code: str, except_id: Optional[int]) -> bool:
        pass

    def find_by_id(self, id: Optional[int]) -> Optional[ChannelGetOutDsDto]:
        pass

    def list(self, ds_dto: ChannelListInDsDto) -> List[ChannelListOutDsDto]:
        pass

    def create(self, ds_dto: ChannelCreateInDsDto) -> ChannelCreateOutDsDto:
        self.create_in = ds_dto
        return self.create_out

    def update(self, ds_dto: ChannelUpdateInDsDto) -> ChannelUpdateOutDsDto:
        pass

    def delete(self, ds_dto: ChannelDeleteInDsDto) -> List[ChannelDeleteOutDsDto]:
        pass
