from channel.adapter.gateway.user.user_session import UserSession
from channel.adapter.gateway.user.user_repository import UserRepository

from channel.usecase.models import (
    UserSessionDsDto,
    UserOutDsDto

)
from channel.usecase.repository.user_token import (
    UserTokenAuthenticateRepository
)

from typing import Optional


class UserTokenAuthenticateGateway(UserTokenAuthenticateRepository):

    def __init__(
        self,
        user_session: UserSession,
        user_repository: UserRepository
    ):
        self.user_session = user_session
        self.user_repository = user_repository

    def save_user_session(self, user_ds_dto: UserSessionDsDto):
        self.user_session.save(user_ds_dto)

    def find_user_by_id(self, id: str) -> Optional[UserOutDsDto]:
        return self.user_repository.find_by_id(id)
