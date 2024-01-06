from abc import ABC, abstractmethod

from channel.usecase.models import UserTokenCreateInDsDto, UserTokenCreateOutDsDto, UserTokenDeleteInDsDto


class UserTokenRepository(ABC):

    @abstractmethod
    def create(
        self,
        ds_dto: UserTokenCreateInDsDto
    ) -> UserTokenCreateOutDsDto:
        pass

    @abstractmethod
    def exists_by_user_id_and_token(
        self,
        user_id: str,
        token: str
    ) -> bool:
        pass

    @abstractmethod
    def delete(
        self,
        user_token_ds_dto: UserTokenDeleteInDsDto
    ):
        pass
