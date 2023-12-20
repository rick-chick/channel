from typing import Optional
from channel.adapter.gateway.device.device_session import DeviceSession
from channel.usecase.models import DeviceSessionDsDto
from channel.usecase.repository.device.device_authenticate_repository import DeviceAuthenticateRepository

from .device_repository import DeviceRepository


class DeviceAuthenticateGateway(DeviceAuthenticateRepository):

    def __init__(
            self,
            device_repository: DeviceRepository,
            device_session: DeviceSession,
    ):
        self.device_repository = device_repository
        self.device_session = device_session

    def find_device_id_by_api_key(
        self, api_key: str
    ) -> Optional[int]:
        return self.device_repository.find_id_by_api_key(api_key)

    def save_device_session(
        self,
        device_session_ds_dto: DeviceSessionDsDto
    ):
        return self.device_session.save(device_session_ds_dto)
