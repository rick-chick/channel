from typing import Optional
from .user_token_repository import UserTokenRepository
from channel.adapter.gateway.user.user_repository import UserRepository

from channel.usecase.models import (
    UserOutDsDto,
    UserTokenCreateInDsDto,
    UserTokenCreateOutDsDto,
    UserTokenDeleteInDsDto,
)
from channel.usecase.repository.user_token import UserTokenRefreshRepository


class UserTokenRefreshGateway(UserTokenRefreshRepository):

    def __init__(
        self,
        user_token_repository: UserTokenRepository,
        user_repository: UserRepository
    ):
        self.user_token_repository = user_token_repository
        self.user_repository = user_repository

    def create(
        self,
        user_token_dto: UserTokenCreateInDsDto
    ) -> UserTokenCreateOutDsDto:
        return self.user_token_repository.create(user_token_dto)

    def find_user_by_id(
        self,
        id: str
    ) -> Optional[UserOutDsDto]:
        return self.user_repository.find_by_id(id)

    def exists_user_token_by_user_id_and_token(
        self,
        user_id: str,
        token: str
    ) -> bool:
        return self.user_token_repository.exists_by_user_id_and_token(
            user_id=user_id,
            token=token
        )

    def delete_user_token(
        self,
        user_token_ds_dto: UserTokenDeleteInDsDto
    ):
        self.user_token_repository.delete(user_token_ds_dto)
