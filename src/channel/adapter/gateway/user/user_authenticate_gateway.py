from typing import Optional
from channel.adapter.gateway.user_token.user_token_repository import UserTokenRepository

from channel.usecase.models import UserTokenCreateInDsDto, UserTokenCreateOutDsDto, UserOutDsDto, UserSessionDsDto
from channel.usecase.repository.user import UserAuthenticateRepository
from channel.adapter.gateway.user.user_session import UserSession

from .user_repository import UserRepository


class UserAuthenticateGateway(UserAuthenticateRepository):

    def __init__(
        self,
        user_repository: UserRepository,
        user_session: UserSession
    ):
        self.user_repository = user_repository
        self.user_session = user_session

    def find_user_by_email(
        self,
        email: str
    ) -> Optional[UserOutDsDto]:
        return self.user_repository.find_by_email(email)

    def save_user_session(
        self,
        session_ds_dto: UserSessionDsDto
    ):
        self.user_session.save(session_ds_dto)
