from channel.adapter.gateway.device.device_session import (
    DeviceSession
)
from channel.usecase.models import (
    DeviceSessionDsDto,
)

from typing import Optional


class DeviceSessionImpl(DeviceSession):

    load_out: Optional[DeviceSessionDsDto]

    def save(self, device_session_ds_dto: DeviceSessionDsDto):
        self.save_in = device_session_ds_dto

    def load(self) -> Optional[DeviceSessionDsDto]:
        return self.load_out

