from channel.adapter.gateway.channel.channel_repository import ChannelRepository
from channel.adapter.gateway.record.record_repository import RecordRepository
from .device_repository import DeviceRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    DeviceListInDsDto,
    DeviceListOutDsDto,
    RecordOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.repository.device import DeviceListRepository

from typing import List, Optional


class DeviceListGateway(DeviceListRepository):

    def __init__(
            self,
            device_repository: DeviceRepository,
            channel_repository: ChannelRepository,
            record_repository: RecordRepository,
            user_session: UserSession):
        self.device_repository = device_repository
        self.channel_repository = channel_repository
        self.record_repository = record_repository
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

    def find_latest_record_by_channel_id(
        self,
        channel_id: int
    ) -> Optional[RecordOutDsDto]:
        return self.record_repository.find_latest_by_channel_id(channel_id)
