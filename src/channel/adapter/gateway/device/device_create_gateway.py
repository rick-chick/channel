from .device_repository import DeviceRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    DeviceCreateInDsDto,
    DeviceCreateOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.repository.device import DeviceCreateRepository

from typing import Optional


class DeviceCreateGateway(DeviceCreateRepository):

    def __init__(
            self,
            device_repository: DeviceRepository,
            user_session: UserSession):
        self.device_repository = device_repository
        self.user_session = user_session

    def create(
        self,
        device: DeviceCreateInDsDto
    ) -> DeviceCreateOutDsDto:
        return self.device_repository.create(device)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()
