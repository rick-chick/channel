from .channel_repository import ChannelRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    ChannelGetOutDsDto,
    ChannelUpdateInDsDto,
    ChannelUpdateOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.repository.channel import ChannelUpdateRepository

from typing import Optional


class ChannelUpdateGateway(ChannelUpdateRepository):

    def __init__(
            self,
            channel_repository: ChannelRepository,
            user_session: UserSession):
        self.channel_repository = channel_repository
        self.user_session = user_session

    def update(
        self,
        channel: ChannelUpdateInDsDto
    ) -> Optional[ChannelUpdateOutDsDto]:
        return self.channel_repository.update(channel)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()

    def find_channel_by_id(
        self,
        id: int
    ) -> Optional[ChannelGetOutDsDto]:
        return self.channel_repository.find_by_id(id)
