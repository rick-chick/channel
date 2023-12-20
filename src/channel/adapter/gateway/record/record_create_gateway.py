from channel.adapter.gateway.device.device_repository import DeviceRepository
from channel.adapter.gateway.device.device_session import DeviceSession
from .record_repository import RecordRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    DeviceSessionDsDto,
    RecordCreateInDsDto,
    RecordCreateOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.repository.record import RecordCreateRepository

from typing import Optional


class RecordCreateGateway(RecordCreateRepository):

    def __init__(
            self,
            record_repository: RecordRepository,
            device_session: DeviceSession,
            user_session: UserSession
        ):
        self.record_repository = record_repository
        self.device_session = device_session
        self.user_session = user_session

    def create(
        self,
        record: RecordCreateInDsDto
    ) -> RecordCreateOutDsDto:
        return self.record_repository.create(record)

    def load_session_device(
        self
    ) -> Optional[DeviceSessionDsDto]:
        return self.device_session.load()

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()
