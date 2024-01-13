from datetime import datetime, timedelta
from channel.entity.models import User
from channel.usecase.interactor.user import UserResetPasswordInteractor
from channel.usecase.models import (
    SignupGetOutDsDto,
    UserCreateInDsDto,
    UserCreateOutDsDto,
    UserOutDsDto,
    UserResetPasswordOutDsDto,
    UserResetPasswordInDsDto,
    UserResetPasswordInDto,
    UserResetPasswordOutDto,
    UserUpdateInDsDto,
    UserUpdateInDsDto,
    UserUpdateOutDsDto,
    UserUpdateOutDsDto
)
from channel.usecase.output_port.user import UserResetPasswordOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.user import UserResetPasswordRepository

from tests.channel.factories import (
    SignupGetOutDsDtoFactory,
    UserCreateOutDsDtoFactory,
    UserCreateOutDtoFactory,
    UserOutDsDtoFactory,
    UserResetPasswordOutDsDtoFactory,
    UserResetPasswordInDtoFactory,
    UserUpdateOutDsDtoFactory,
    UserUpdateOutDtoFactory,
)

import pytest
from typing import Optional, List

valid_user_in_dto = UserResetPasswordInDtoFactory.build()
valid_user_ds_dto = UserOutDsDtoFactory.build()
valid_user_create_ds_dto = UserCreateOutDsDtoFactory.build()
valid_user_update_ds_dto = UserUpdateOutDsDtoFactory.build()
valid_signup_ds_dto = SignupGetOutDsDtoFactory.build(
    created_at=datetime.now()
)


class UserResetPasswordOututPortImpl(UserResetPasswordOututPort):

    def __init__(self):
        self.exceptions = []
        self.user: Optional[UserResetPasswordOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, user: UserResetPasswordOutDto):
        self.user = user
        return user


class UserResetPasswordRepositoryImpl(UserResetPasswordRepository):
    create_user_output: UserCreateOutDsDto = valid_user_create_ds_dto
    create_user_input: Optional[UserCreateInDsDto] = None
    update_user_output: UserUpdateOutDsDto = valid_user_update_ds_dto
    update_user_input: Optional[UserUpdateInDsDto] = None

    find_signup_by_token_output: Optional[SignupGetOutDsDto] = valid_signup_ds_dto
    find_user_by_email_output: Optional[UserOutDsDto] = valid_user_ds_dto

    def create_user(
        self,
        user_dto: UserCreateInDsDto
    ) -> UserCreateOutDsDto:
        self.create_user_input = user_dto
        return self.create_user_output

    def update_user(
        self,
        user_dto: UserUpdateInDsDto
    ) -> UserUpdateOutDsDto:
        self.update_user_input = user_dto
        return self.update_user_output

    def find_signup_by_token(
        self,
        token: str
    ) -> Optional[SignupGetOutDsDto]:
        self.find_signup_by_token_input = token
        return self.find_signup_by_token_output

    def find_user_by_email(
        self,
        email: str
    ) -> Optional[UserOutDsDto]:
        self.find_user_by_email_input = email
        return self.find_user_by_email_output


def create_interactor(
        gateway=UserResetPasswordRepositoryImpl(),
        presenter=UserResetPasswordOututPortImpl()
) -> UserResetPasswordInteractor:
    return UserResetPasswordInteractor(gateway, presenter)


def test_reset_password_success_when_update():

    presenter = UserResetPasswordOututPortImpl()
    gateway = UserResetPasswordRepositoryImpl()

    target = create_interactor(gateway, presenter)

    target.reset_password(valid_user_in_dto)

    assert presenter.user is not None
    assert not gateway.create_user_input
    assert gateway.update_user_input

    user_for_assert = User(
        id="",
        email="",
        password_hash=gateway.update_user_input.password_hash,
        password=valid_user_in_dto.password
    )
    assert user_for_assert.is_authenticated()


def test_reset_password_success_when_user_create():

    presenter = UserResetPasswordOututPortImpl()
    gateway = UserResetPasswordRepositoryImpl()
    gateway.find_user_by_email_output = None

    target = create_interactor(gateway, presenter)

    target.reset_password(valid_user_in_dto)

    assert presenter.user is not None
    assert gateway.create_user_input
    assert gateway.create_user_input.email == valid_signup_ds_dto.email
    assert not gateway.update_user_input

    user_for_assert = User(
        id="",
        email="",
        password_hash=gateway.create_user_input.password_hash,
        password=valid_user_in_dto.password
    )
    assert user_for_assert.is_authenticated()


def test_reset_password_fail_when_signup_token_missing():

    presenter = UserResetPasswordOututPortImpl()
    gateway = UserResetPasswordRepositoryImpl()
    gateway.find_signup_by_token_output = None

    target = create_interactor(gateway, presenter)

    user_in_dto = valid_user_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.reset_password(user_in_dto)


def test_reset_password_fail_when_signup_token_is_timeout():

    presenter = UserResetPasswordOututPortImpl()
    gateway = UserResetPasswordRepositoryImpl()
    signup = valid_signup_ds_dto.model_copy()
    signup.created_at = datetime.now() - timedelta(minutes=11)
    gateway.find_signup_by_token_output = signup

    target = create_interactor(gateway, presenter)

    user_in_dto = valid_user_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.reset_password(user_in_dto)
