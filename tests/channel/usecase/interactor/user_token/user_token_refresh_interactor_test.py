from channel.entity.models import User
from channel.usecase.interactor.user_token import UserTokenRefreshInteractor
from channel.usecase.models import (
    UserOutDsDto,
    UserTokenCreateInDsDto,
    UserTokenCreateOutDsDto,
    UserTokenDeleteInDsDto,
    UserTokenRefreshInDto,
    UserTokenRefreshOutDto
)
from channel.usecase.output_port.user_token import UserTokenRefreshOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.user_token import UserTokenRefreshRepository

from tests.channel.factories import (
    UserOutDsDtoFactory,
    UserTokenCreateOutDsDtoFactory,
    UserTokenCreateInDsDtoFactory,
    UserTokenRefreshInDtoFactory,
)

import pytest
from typing import Optional, List
from uuid import uuid4

user = User(
    id=str(uuid4()),
    email="hogehuga@test.com",
)

valid_user_token_in_dto = UserTokenRefreshInDtoFactory.build(
    refresh_token=user.create_jwt(30),
    user_id=user.id
)
valid_user_token_ds_dto = UserTokenCreateOutDsDtoFactory.build()
valid_user_ds_dto = UserOutDsDtoFactory.build(
    id=user.id
)


class UserTokenRefreshOututPortImpl(UserTokenRefreshOututPort):

    def __init__(self):
        self.exceptions = []
        self.user_token: Optional[UserTokenRefreshOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, user_token: UserTokenRefreshOutDto):
        self.user_token = user_token
        return user_token


class UserTokenRefreshRepositoryImpl(UserTokenRefreshRepository):

    create_input: Optional[UserTokenCreateInDsDto] = None
    create_output: UserTokenCreateOutDsDto = valid_user_token_ds_dto
    find_user_by_id_output: UserOutDsDto = valid_user_ds_dto
    exists_user_token_by_user_id_and_token_output: bool = False

    def create(self, user_token_dto: UserTokenCreateInDsDto) -> UserTokenCreateOutDsDto:
        self.create_input = user_token_dto
        return self.create_output

    def find_user_by_id(self, id: str) -> Optional[UserOutDsDto]:
        self.find_user_by_id_input = id
        return self.find_user_by_id_output

    def exists_user_token_by_user_id_and_token(
        self,
        user_id: str,
        token: str,
    ) -> bool:
        self.exists_user_token_by_user_id_and_token_input = [user_id, token]
        return self.exists_user_token_by_user_id_and_token_output

    def delete_user_token(
        self,
        user_token_ds_dto: UserTokenDeleteInDsDto
    ):
        self.delete_user_token_input = user_token_ds_dto


def create_interactor(
        gateway=UserTokenRefreshRepositoryImpl(),
        presenter=UserTokenRefreshOututPortImpl()) -> UserTokenRefreshInteractor:
    return UserTokenRefreshInteractor(gateway, presenter)


def test_refresh_success():

    presenter = UserTokenRefreshOututPortImpl()
    gateway = UserTokenRefreshRepositoryImpl()

    gateway.create_output = valid_user_token_ds_dto

    target = create_interactor(gateway, presenter)

    target.refresh(valid_user_token_in_dto)

    assert presenter.user_token is not None


def test_refresh_fail_when_refresh_token_is_invalid():

    presenter = UserTokenRefreshOututPortImpl()
    gateway = UserTokenRefreshRepositoryImpl()

    target = create_interactor(gateway, presenter)

    user_token_in_dto = valid_user_token_in_dto.model_copy()
    user_token_in_dto.refresh_token = 'hogehuga'

    with pytest.raises(BusinessException):
        target.refresh(user_token_in_dto)


def test_refresh_fail_when_user_id_is_incorrect():

    presenter = UserTokenRefreshOututPortImpl()
    gateway = UserTokenRefreshRepositoryImpl()

    target = create_interactor(gateway, presenter)

    user_token_in_dto = valid_user_token_in_dto.model_copy()
    user_token_in_dto.user_id = str(uuid4())

    with pytest.raises(BusinessException):
        target.refresh(user_token_in_dto)


def test_refresh_fail_when_user_not_found():

    presenter = UserTokenRefreshOututPortImpl()
    gateway = UserTokenRefreshRepositoryImpl()
    gateway.find_user_by_id_output = None

    target = create_interactor(gateway, presenter)

    user_token_in_dto = valid_user_token_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.refresh(user_token_in_dto)


def test_refresh_fail_when_already_refreshed():

    presenter = UserTokenRefreshOututPortImpl()
    gateway = UserTokenRefreshRepositoryImpl()
    gateway.exists_user_token_by_user_id_and_token_output = True

    target = create_interactor(gateway, presenter)

    user_token_in_dto = valid_user_token_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.refresh(user_token_in_dto)
