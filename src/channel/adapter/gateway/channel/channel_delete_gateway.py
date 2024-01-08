from .channel_repository import ChannelRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    ChannelDeleteOutDsDto,
    ChannelDeleteInDsDto,
    UserSessionDsDto
)
from channel.usecase.repository.channel import ChannelDeleteRepository

from typing import List, Optional


class ChannelDeleteGateway(ChannelDeleteRepository):

    def __init__(
            self,
            channel_repository: ChannelRepository,
            user_session: UserSession):
        self.channel_repository = channel_repository
        self.user_session = user_session

    def delete(self, channel_dto: ChannelDeleteInDsDto) -> List[ChannelDeleteOutDsDto]:
        return self.channel_repository.delete(channel_dto)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()
