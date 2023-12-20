from channel.usecase.interactor.user_token import UserTokenAuthenticateInteractor
from channel.usecase.models import (
    UserTokenAuthenticateInDto,
    UserTokenAuthenticateOutDto,
    UserOutDsDto,
    UserSessionDsDto
)
from channel.usecase.output_port.user_token import UserTokenAuthenticateOututPort
from channel.usecase.exception import (
    BusinessException,
    UnauthenticateException,
)
from channel.usecase.repository.user_token import UserTokenAuthenticateRepository
from channel.entity.models import User

from tests.channel.factories import (
    UserTokenAuthenticateOutDtoFactory,
    UserTokenAuthenticateInDtoFactory,
    UserOutDsDtoFactory,
)


import pytest
from typing import Optional, List

user = User(**UserOutDsDtoFactory.build().model_dump())
token = user.create_jwt()

valid_user_token_in_dto = UserTokenAuthenticateInDtoFactory.build(
    token=token
)
valid_user_out_ds_dto = UserOutDsDtoFactory.build(
    id=user.id
)


class UserTokenAuthenticateOututPortImpl(UserTokenAuthenticateOututPort):

    def __init__(self):
        self.exceptions = []
        self.user_token: Optional[UserTokenAuthenticateOutDto] = None

    def prepare_fail_view(self, error: Exception):
        self.exceptions.append(error)

    def prepare_success_view(self, user_token: UserTokenAuthenticateOutDto):
        self.user_token = user_token

    def errors(self) -> List[Exception]:
        return self.exceptions

    def has_errors(self):
        return len(self.exceptions) > 0

    def get_user_token(self) -> UserTokenAuthenticateOutDto:
        if self.user_token:
            return self.user_token
        raise Exception("invalid_access")


class UserTokenAuthenticateRepositoryImpl(UserTokenAuthenticateRepository):

    find_user_by_id_in: Optional[str] = None
    find_user_by_id_out: Optional[UserOutDsDto] = valid_user_out_ds_dto
    save_user_session_in: Optional[UserSessionDsDto] = None

    def find_user_by_id(self, id: Optional[str]) -> Optional[UserOutDsDto]:
        self.find_user_by_id_in = id
        return self.find_user_by_id_out

    def save_user_session(self, uer_out_ds_dto: UserSessionDsDto):
        self.save_user_session_in = uer_out_ds_dto


def create_interactor(
        gateway=UserTokenAuthenticateRepositoryImpl(),
        presenter=UserTokenAuthenticateOututPortImpl()
) -> UserTokenAuthenticateInteractor:
    return UserTokenAuthenticateInteractor(gateway, presenter)


def test_authenticate_success():

    presenter = UserTokenAuthenticateOututPortImpl()
    gateway = UserTokenAuthenticateRepositoryImpl()

    target = create_interactor(gateway, presenter)

    target.authenticate(valid_user_token_in_dto)

    assert presenter.get_user_token() is not None
    assert gateway.find_user_by_id_in == user.id
    assert gateway.save_user_session_in.email == valid_user_out_ds_dto.email


def test_authenticate_fail_when_token_is_invalid():

    presenter = UserTokenAuthenticateOututPortImpl()
    gateway = UserTokenAuthenticateRepositoryImpl()

    target = create_interactor(gateway, presenter)

    user_token_in_dto = valid_user_token_in_dto.model_copy()
    user_token_in_dto.token = 'invalid_token'

    with pytest.raises(UnauthenticateException):
        target.authenticate(user_token_in_dto)


def test_authenticate_fail_when_user_id_is_not_found():

    presenter = UserTokenAuthenticateOututPortImpl()
    gateway = UserTokenAuthenticateRepositoryImpl()
    gateway.find_user_by_id_out = None

    target = create_interactor(gateway, presenter)

    user_token_in_dto = valid_user_token_in_dto.model_copy()

    with pytest.raises(UnauthenticateException):
        target.authenticate(user_token_in_dto)
