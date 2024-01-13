from abc import ABC, abstractmethod
from channel.usecase.models import (
    SignupGetOutDsDto,
    UserCreateInDsDto,
    UserCreateOutDsDto,
    UserOutDsDto,
    UserUpdateInDsDto,
    UserUpdateInDto,
    UserUpdateOutDsDto,
    UserUpdateOutDto
)

from typing import Optional


class UserResetPasswordRepository(ABC):

    @abstractmethod
    def find_signup_by_token(
        self,
        token: str
    ) -> Optional[SignupGetOutDsDto]:
        pass

    @abstractmethod
    def find_user_by_email(
        self,
        email: str
    ) -> Optional[UserOutDsDto]:
        pass

    @abstractmethod
    def create_user(
        self,
        user_dto: UserCreateInDsDto
    ) -> UserCreateOutDsDto:
        pass

    @abstractmethod
    def update_user(
        self,
        user_dto: UserUpdateInDsDto
    ) -> Optional[UserUpdateOutDsDto]:
        pass
