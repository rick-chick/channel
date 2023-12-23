from typing import List, Optional
from channel.adapter.gateway.channel.channel_repository import ChannelRepository

from channel.adapter.gateway.user import UserSession
from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    RecordListInDsDto,
    RecordListOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.repository.record import RecordListRepository

from .record_repository import RecordRepository


class RecordListGateway(RecordListRepository):

    def __init__(
            self,
            record_repository: RecordRepository,
            channel_repository: ChannelRepository,
            user_session: UserSession):
        self.record_repository = record_repository
        self.channel_repository = channel_repository
        self.user_session = user_session

    def list(
        self,
        record_dto: RecordListInDsDto
    ) -> List[RecordListOutDsDto]:
        return self.record_repository.list(record_dto)

    def channel_list(
        self,
        channel_dto: ChannelListInDsDto
    ) -> List[ChannelListOutDsDto]:
        return self.channel_repository.list(channel_dto)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()
