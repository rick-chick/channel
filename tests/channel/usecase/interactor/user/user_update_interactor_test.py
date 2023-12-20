from channel.usecase.interactor.user.user_update_interactor import UserUpdateInteractor
from channel.usecase.models import (
    UserUpdateInDsDto,
    UserUpdateOutDsDto,
    UserUpdateOutDto,
    UserSessionDsDto
)
from channel.usecase.output_port.user import UserUpdateOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.user.user_update_repository import UserUpdateRepository

from tests.channel.factories import (
    UserUpdateInDtoFactory,
    UserUpdateOutDsDtoFactory,
    UserSessionDsDtoFactory
)

import pytest
from typing import Optional

valid_user_in_dto = UserUpdateInDtoFactory.build()
valid_user_ds_dto = UserUpdateOutDsDtoFactory.build()
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()

class UserUpdateOututPortImpl(UserUpdateOututPort):

    def __init__(self):
        self.exceptions = []
        self.user: Optional[UserUpdateOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, user: UserUpdateOutDto):
        self.user = user
        return user



class UserUpdateRepositoryImpl(UserUpdateRepository):

    update_in: Optional[UserUpdateInDsDto] = None
    update_out: Optional[UserUpdateOutDsDto] = valid_user_ds_dto 
    load_session_user_out: Optional[UserSessionDsDto] = valid_session_user_ds_dto


    exists_user_by_id_in: Optional[int] = None
    exists_user_by_id_out: bool = True


    def update(self, user: UserUpdateInDsDto):
        self.update_in = user
        return self.update_out

    def exists_user_by_id(self, id: Optional[int]) -> bool:
        self.exists_user_by_id_in = id
        return self.exists_user_by_id_out

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_out


def create_interactor(
        gateway=UserUpdateRepositoryImpl(),
        presenter=UserUpdateOututPortImpl()) -> UserUpdateInteractor:
    return UserUpdateInteractor(gateway, presenter)


def test_update_success():

    presenter = UserUpdateOututPortImpl()
    gateway = UserUpdateRepositoryImpl()

    gateway.update_out = valid_user_ds_dto

    target = create_interactor(gateway, presenter)

    target.update(valid_user_in_dto)

    assert presenter.user is not None 
    assert gateway.update_in is not None
    assert gateway.update_in.password_hash is not None


def test_update_success_when_password_is_blank_password_hash_is_blank():

    presenter = UserUpdateOututPortImpl()
    gateway = UserUpdateRepositoryImpl()

    gateway.update_out = valid_user_ds_dto

    # パスワードをブランクとする
    target = create_interactor(gateway, presenter)
    user_in_dto = valid_user_in_dto.model_copy()
    user_in_dto.password = None

    target.update(user_in_dto)

    assert gateway.update_in is not None
    assert gateway.update_in.password_hash is None


def test_update_fail():

    presenter = UserUpdateOututPortImpl()
    gateway = UserUpdateRepositoryImpl()
    gateway.load_session_user_out = None

    target = create_interactor(gateway, presenter)

    user_in_dto = valid_user_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.update(user_in_dto)
