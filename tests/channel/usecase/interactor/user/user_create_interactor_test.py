from channel.usecase.interactor.user import UserCreateInteractor
from channel.usecase.models import (
    UserCreateOutDto,
    UserCreateInDsDto,
    UserCreateOutDsDto,
    UserSessionDsDto,
)
from channel.usecase.output_port.user import UserCreateOututPort
from channel.usecase.exception import (
    BusinessException,
    UserExistsException,
    UnauthorizedException
)
from channel.usecase.repository.user import UserCreateRepository

from tests.channel.factories import (
    UserCreateOutDsDtoFactory,
    UserCreateInDtoFactory,
    UserCreateOutDtoFactory,
    UserSessionDsDtoFactory,
)

import pytest
from typing import Optional, List

valid_user_in_dto = UserCreateInDtoFactory.build()
valid_user_ds_dto = UserCreateOutDsDtoFactory.build()
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()


class UserCreateOututPortImpl(UserCreateOututPort):

    def __init__(self):
        self.exceptions = []
        self.user: Optional[UserCreateOutDto] = None

    def prepare_fail_view(self, error: Exception):
        self.exceptions.append(error)

    def prepare_success_view(self, user: UserCreateOutDto):
        self.user = user

    def errors(self) -> List[Exception]:
        return self.exceptions

    def has_errors(self):
        return len(self.exceptions) > 0

    def get_user(self) -> UserCreateOutDto:
        if self.user:
            return self.user
        raise Exception("invalid_access")


class UserCreateRepositoryImpl(UserCreateRepository):

    create_input: Optional[UserCreateInDsDto] = None
    create_output: Optional[UserCreateOutDsDto] = valid_user_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto
    exists_user_by_email_input: Optional[str] = None
    exists_user_by_email_output: bool = False

    def create(self, user: UserCreateOutDsDto):
        self.create_input = user
        return self.create_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output

    def exists_user_by_email(self, email: str) -> bool:
        self.exists_user_by_email_input = email
        return self.exists_user_by_email_output


def create_interactor(
    gateway=UserCreateRepositoryImpl(),
    presenter=UserCreateOututPortImpl()
) -> UserCreateInteractor:
    return UserCreateInteractor(gateway, presenter)


def test_create_success():

    presenter = UserCreateOututPortImpl()
    gateway = UserCreateRepositoryImpl()

    gateway.create_output = valid_user_ds_dto

    target = create_interactor(gateway, presenter)

    target.create(valid_user_in_dto)

    assert presenter.get_user() is not None


def test_create_fail():

    presenter = UserCreateOututPortImpl()
    gateway = UserCreateRepositoryImpl()

    target = create_interactor(gateway, presenter)

    user_in_dto = valid_user_in_dto.model_copy()
    user_in_dto.email = None

    with pytest.raises(BusinessException):
        target.create(user_in_dto)


def test_create_fail_when_duplicate_email():

    presenter = UserCreateOututPortImpl()
    gateway = UserCreateRepositoryImpl()
    gateway.exists_user_by_email_output = True

    target = create_interactor(gateway, presenter)

    user_in_dto = valid_user_in_dto.model_copy()

    with pytest.raises(UserExistsException):
        target.create(user_in_dto)


def test_create_fail_when_user_unauthorized():

    presenter = UserCreateOututPortImpl()
    gateway = UserCreateRepositoryImpl()
    gateway.load_session_user_output = None

    target = create_interactor(gateway, presenter)

    user_in_dto = valid_user_in_dto.model_copy()

    with pytest.raises(UnauthorizedException):
        target.create(user_in_dto)
