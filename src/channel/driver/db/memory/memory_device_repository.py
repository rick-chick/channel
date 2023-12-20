from channel.usecase.models import (
    DeviceSessionDsDto
)
from channel.adapter.gateway.device.device_session import (
    DeviceSession
)

from typing import Dict, Any, Optional


class MemoryDeviceRepository(DeviceSession):

    def __init__(self, memory: Dict[str, Any]):
        self.memory = memory

    def load(self) -> Optional[DeviceSessionDsDto]:
        if not 'device' in self.memory:
            return None
        return self.memory['device']

    def save(self, device_session_ds_dto: DeviceSessionDsDto):
        if self.memory:
            self.memory['device'] = device_session_ds_dto
