from channel.usecase.models import (
    UserSessionDsDto
)

from abc import ABC, abstractmethod
from typing import Optional


class UserSession(ABC):

    @abstractmethod
    def load(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def save(self, user_session_ds_dto: UserSessionDsDto):
        pass
