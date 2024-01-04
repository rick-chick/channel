from channel.adapter.gateway.channel.channel_repository import ChannelRepository
from channel.adapter.gateway.record.record_repository import RecordRepository
from .device_repository import DeviceRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    ChannelDeleteInDsDto,
    ChannelDeleteOutDsDto,
    DeviceDeleteOutDsDto,
    DeviceDeleteInDsDto,
    RecordDeleteInDsDto,
    RecordDeleteOutDsDto,
    UserSessionDsDto
)
from channel.usecase.repository.device import DeviceDeleteRepository

from typing import List, Optional


class DeviceDeleteGateway(DeviceDeleteRepository):

    def __init__(
        self,
        device_repository: DeviceRepository,
        channel_repository: ChannelRepository,
        record_repository: RecordRepository,
        user_session: UserSession,
    ):
        self.device_repository = device_repository
        self.channel_repository = channel_repository
        self.record_repository = record_repository
        self.user_session = user_session

    def delete(
        self,
        device_dto: DeviceDeleteInDsDto
    ) -> List[DeviceDeleteOutDsDto]:
        return self.device_repository.delete(device_dto)

    def delete_channel(
        self,
        channel_dto: ChannelDeleteInDsDto
    ) -> List[ChannelDeleteOutDsDto]:
        return self.channel_repository.delete(channel_dto)

    def delete_record(
        self,
        record_dto: RecordDeleteInDsDto
    ) -> List[RecordDeleteOutDsDto]:
        return self.record_repository.delete(record_dto)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()
