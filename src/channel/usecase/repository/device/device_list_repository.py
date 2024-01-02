from abc import ABC, abstractmethod
from channel.usecase.models import (
    DeviceListInDsDto,
    DeviceListOutDsDto,
    UserSessionDsDto
)

from typing import List, Optional


class DeviceListRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def list(
        self,
        device_dto: DeviceListInDsDto
    ) -> List[DeviceListOutDsDto]:
        pass
