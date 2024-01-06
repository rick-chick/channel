from abc import ABC, abstractmethod
from channel.usecase.models import UserOutDsDto, UserTokenCreateInDsDto, UserTokenCreateOutDsDto, UserSessionDsDto, UserTokenDeleteInDsDto

from typing import Optional


class UserTokenRefreshRepository(ABC):

    @abstractmethod
    def create(self, user_token_dto: UserTokenCreateInDsDto) -> UserTokenCreateOutDsDto:
        pass

    @abstractmethod
    def find_user_by_id(self, id: str) -> Optional[UserOutDsDto]:
        pass

    @abstractmethod
    def exists_user_token_by_user_id_and_token(
        self,
        user_id: str,
        token: str
    ) -> bool:
        pass

    @abstractmethod
    def delete_user_token(
        self,
        user_token_ds_dto: UserTokenDeleteInDsDto
    ):
        pass
