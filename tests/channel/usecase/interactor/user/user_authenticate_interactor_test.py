from typing import List, Optional

from passlib.context import CryptContext
import pytest

from channel.usecase.exception import BusinessException
from channel.usecase.interactor.user import UserAuthenticateInteractor
from channel.usecase.models import (
    UserAuthenticateOutDto,
    UserOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.output_port.user import UserAuthenticateOututPort
from channel.usecase.repository.user import UserAuthenticateRepository
from tests.channel.factories import UserAuthenticateInDtoFactory, UserOutDsDtoFactory
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


valid_user_in_dto = UserAuthenticateInDtoFactory.build()
valid_user_ds_dto = UserOutDsDtoFactory.build(
    password_hash=pwd_context.hash(valid_user_in_dto.password)
)


class UserAuthenticateOututPortImpl(UserAuthenticateOututPort):

    def __init__(self):
        self.exceptions = []
        self.user: Optional[UserAuthenticateOutDto] = None

    def prepare_fail_view(self, error: Exception):
        self.exceptions.append(error)

    def prepare_success_view(self, user: UserAuthenticateOutDto):
        self.user = user
        return user


class UserAuthenticateRepositoryImpl(UserAuthenticateRepository):

    find_user_by_email_input: Optional[str] = None
    find_user_by_email_output: UserOutDsDto = valid_user_ds_dto

    save_user_session_in: UserSessionDsDto

    def find_user_by_email(self, email: str) -> Optional[UserOutDsDto]:
        self.find_user_by_email_input = email
        return self.find_user_by_email_output

    def save_user_session(self, session_ds_dto: UserSessionDsDto):
        self.save_user_session_in = session_ds_dto


def create_interactor(
        gateway=UserAuthenticateRepositoryImpl(),
        presenter=UserAuthenticateOututPortImpl()) -> UserAuthenticateInteractor:
    return UserAuthenticateInteractor(gateway, presenter)


def test_authenticate_success():

    presenter = UserAuthenticateOututPortImpl()
    gateway = UserAuthenticateRepositoryImpl()

    target = create_interactor(gateway, presenter)

    target.authenticate(valid_user_in_dto)

    assert gateway.save_user_session_in.email == valid_user_ds_dto.email


def test_authenticate_fail():

    presenter = UserAuthenticateOututPortImpl()
    gateway = UserAuthenticateRepositoryImpl()

    target = create_interactor(gateway, presenter)

    user_in_dto = valid_user_in_dto.model_copy()
    user_in_dto.password = 'invalid'

    with pytest.raises(BusinessException):
        target.authenticate(user_in_dto)
