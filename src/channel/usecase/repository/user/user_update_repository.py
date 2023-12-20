from abc import ABC, abstractmethod
from channel.usecase.models import (
    UserUpdateInDsDto,
    UserUpdateOutDsDto,
    UserSessionDsDto
)

from typing import Optional

class UserUpdateRepository(ABC):

    @abstractmethod
    def load_session_user(self) -> Optional[UserSessionDsDto]:
        pass

    @abstractmethod
    def update(
        self,
        user_dto: UserUpdateInDsDto
    ) -> UserUpdateOutDsDto:
        pass

    @abstractmethod
    def exists_user_by_id(self, id: Optional[int]) -> bool:
        pass
