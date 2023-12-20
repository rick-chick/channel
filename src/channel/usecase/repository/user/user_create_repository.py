from abc import ABC, abstractmethod
from channel.usecase.models import (
    UserSessionDsDto,
    UserCreateInDsDto,
    UserCreateOutDsDto,
)

from typing import Optional


class UserCreateRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def create(self, user: UserCreateInDsDto) -> UserCreateOutDsDto:
        pass

    @abstractmethod
    def exists_user_by_email(self, email: str) -> bool:
        pass
