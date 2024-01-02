from channel.adapter.gateway.device.device_repository import DeviceRepository
from .channel_repository import ChannelRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    DeviceListInDsDto,
    DeviceListOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.repository.channel import ChannelListRepository

from typing import Optional, List


class ChannelListGateway(ChannelListRepository):

    def __init__(
            self,
            channel_repository: ChannelRepository,
            user_session: UserSession,
            device_repository: DeviceRepository
    ):
        self.channel_repository = channel_repository
        self.user_session = user_session
        self.device_repository = device_repository

    def list(
        self,
        channel_dto: ChannelListInDsDto
    ) -> List[ChannelListOutDsDto]:
        return self.channel_repository.list(channel_dto)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()

    def list_device(
        self,
        device_dto: DeviceListInDsDto
    ) -> List[DeviceListOutDsDto]:
        return self.device_repository.list(device_dto)
