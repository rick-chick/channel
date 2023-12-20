from abc import ABC, abstractmethod
from typing import Optional

from channel.usecase.models import UserOutDsDto, UserSessionDsDto


class UserAuthenticateRepository(ABC):

    @abstractmethod
    def find_user_by_email(self, email: str) -> Optional[UserOutDsDto]:
        pass


    @abstractmethod
    def save_user_session(
        self,
        session_ds_dto: UserSessionDsDto
    ):
        pass
