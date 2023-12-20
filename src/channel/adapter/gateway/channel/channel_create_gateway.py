from .channel_repository import ChannelRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    ChannelCreateInDsDto,
    ChannelCreateOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.repository.channel import ChannelCreateRepository

from typing import Optional


class ChannelCreateGateway(ChannelCreateRepository):

    def __init__(
            self,
            channel_repository: ChannelRepository,
            user_session: UserSession):
        self.channel_repository = channel_repository
        self.user_session = user_session

    def create(
        self,
        channel: ChannelCreateInDsDto
    ) -> ChannelCreateOutDsDto:
        return self.channel_repository.create(channel)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()
