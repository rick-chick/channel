from abc import ABC, abstractmethod
from channel.usecase.models import (
    DriverDsDto,
    UserSessionDsDto,
)

from typing import Optional


class DriverCreateRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def create(self, driver: DriverDsDto) -> DriverDsDto:
        pass
