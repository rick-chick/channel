from channel.adapter.gateway.user_token.user_token_repository import UserTokenRepository
from channel.usecase.models import UserOutDsDto, UserTokenCreateInDsDto, UserTokenCreateOutDsDto, UserTokenDeleteInDsDto

from typing import Optional

from tests.channel.factories import UserTokenCreateOutDsDtoFactory


class UserTokenRepositoryImpl(UserTokenRepository):

    create_out: UserTokenCreateOutDsDto = UserTokenCreateOutDsDtoFactory.build()

    def create(
        self,
        ds_dto: UserTokenCreateInDsDto
    ) -> UserTokenCreateOutDsDto:
        self.create_in = ds_dto
        return self.create_out

    def exists_by_user_id_and_token(
        self,
        user_id: str,
        token: str
    ) -> bool:
        return False

    def delete(
        self,
        user_token_ds_dto: UserTokenDeleteInDsDto
    ):
        pass
