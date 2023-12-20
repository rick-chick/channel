from .user_repository import UserRepository
from channel.adapter.gateway.user import UserSession

from channel.usecase.models import (
    UserUpdateInDsDto,
    UserUpdateOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.repository.user.user_update_repository import UserUpdateRepository

from typing import Optional


class UserUpdateGateway(UserUpdateRepository):

    def __init__(
            self,
            user_repository: UserRepository,
            user_session: UserSession):
        self.user_repository = user_repository
        self.user_session = user_session

    def update(
        self,
        user_dto: UserUpdateInDsDto
    ) -> UserUpdateOutDsDto:
        return self.user_repository.update(user_dto)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()

    def exists_user_by_id(
        self,
        id: int
    ) -> bool:
        return self.user_repository.exists_by_id(id)
