from channel.adapter.gateway.channel.channel_repository import ChannelRepository
from .device_repository import DeviceRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    DeviceListInDsDto,
    DeviceListOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.repository.device import DeviceListRepository

from typing import List, Optional


class DeviceListGateway(DeviceListRepository):

    def __init__(
            self,
            device_repository: DeviceRepository,
            channel_repository: ChannelRepository,
            user_session: UserSession):
        self.device_repository = device_repository
        self.channel_repository = channel_repository
        self.user_session = user_session

    def list(
        self,
        device_dto: DeviceListInDsDto
    ) -> List[DeviceListOutDsDto]:
        return self.device_repository.list(device_dto)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()

    def list_channel(
        self,
        channel_dto: ChannelListInDsDto
    ) -> List[ChannelListOutDsDto]:
        return self.channel_repository.list(channel_dto)
