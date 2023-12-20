from abc import ABC, abstractmethod
from typing import Optional

from channel.usecase.models import DeviceSessionDsDto


class DeviceAuthenticateRepository(ABC):

    @abstractmethod
    def find_device_id_by_api_key(
        self,
        api_key: str
    ) -> Optional[int]:
        pass

    @abstractmethod
    def save_device_session(
        self,
        device_session_ds_dto: DeviceSessionDsDto
    ):
        pass
