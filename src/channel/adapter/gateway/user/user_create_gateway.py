from channel.adapter.gateway.user.user_repository import UserRepository
from channel.adapter.gateway.user.user_session import UserSession

from channel.usecase.models import (
    UserCreateInDsDto,
    UserCreateOutDsDto,
    UserSessionDsDto
)
from channel.usecase.repository.user import UserCreateRepository

from typing import Optional


class UserCreateGateway(UserCreateRepository):

    def __init__(
            self,
            user_repository: UserRepository,
            user_session: UserSession):
        self.user_repository = user_repository
        self.user_session = user_session

    def create(self, user: UserCreateInDsDto) -> UserCreateOutDsDto:
        return self.user_repository.create(user)

    def exists_user_by_email(self, email: str) -> bool:
        return self.user_repository.exists_by_email(email)

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.user_session.load()
