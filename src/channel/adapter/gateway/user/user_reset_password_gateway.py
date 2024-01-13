from typing import Optional

from channel.adapter.gateway.signup.signup_repository import SignupRepository
from channel.usecase.input_port.user.user_create_input_port import UserCreateInputPort
from channel.usecase.input_port.user.user_update_input_port import UserUpdateInputPort
from .user_repository import UserRepository

from channel.usecase.models import (
    SignupGetOutDsDto,
    UserCreateInDsDto,
    UserCreateInDto,
    UserCreateOutDsDto,
    UserCreateOutDto,
    UserOutDsDto,
    UserUpdateInDsDto,
    UserUpdateInDto,
    UserUpdateOutDsDto,
    UserUpdateOutDto,
)
from channel.usecase.repository.user import UserResetPasswordRepository


class UserResetPasswordGateway(UserResetPasswordRepository):

    def __init__(
        self,
        user_repository: UserRepository,
        signup_repository: SignupRepository,
    ):
        self.user_repository = user_repository
        self.signup_repository = signup_repository

    def find_signup_by_token(
        self,
        token: str
    ) -> Optional[SignupGetOutDsDto]:
        return self.signup_repository.find_by_token(token)

    def find_user_by_email(
        self,
        email: str
    ) -> Optional[UserOutDsDto]:
        return self.user_repository.find_by_email(email)

    def create_user(
        self,
        user_dto: UserCreateInDsDto
    ) -> UserCreateOutDsDto:
        return self.user_repository.create(user_dto)

    def update_user(
        self,
        user_dto: UserUpdateInDsDto
    ) -> Optional[UserUpdateOutDsDto]:
        return self.user_repository.update(user_dto)
