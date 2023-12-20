from channel.usecase.interactor.channel import ChannelCreateInteractor
from channel.usecase.models import (
    ChannelCreateInDto,
    ChannelCreateOutDto,
    ChannelCreateInDsDto,
    ChannelCreateOutDsDto,
    UserSessionDsDto
)
from channel.usecase.output_port.channel import ChannelCreateOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.channel import ChannelCreateRepository

from tests.channel.factories import (
    ChannelCreateOutDsDtoFactory,
    ChannelCreateInDtoFactory,
    ChannelCreateOutDtoFactory,
    UserSessionDsDtoFactory,
)

import pytest
from typing import Optional, List

valid_channel_in_dto = ChannelCreateInDtoFactory.build()
valid_channel_ds_dto = ChannelCreateOutDsDtoFactory.build()
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()


class ChannelCreateOututPortImpl(ChannelCreateOututPort):

    def __init__(self):
        self.exceptions = []
        self.channel: Optional[ChannelCreateOutDto] = None

    def prepare_fail_view(self, error: Exception):
        self.exceptions.append(error)

    def prepare_success_view(self, channel: ChannelCreateOutDto):
        self.channel = channel

    def errors(self) -> List[Exception]:
        return self.exceptions

    def has_errors(self):
        return len(self.exceptions) > 0

    def get_channel(self) -> ChannelCreateOutDto:
        if self.channel:
            return self.channel
        raise Exception("invalid_access")


class ChannelCreateRepositoryImpl(ChannelCreateRepository):

    create_input: Optional[ChannelCreateInDsDto] = None
    create_output: Optional[ChannelCreateOutDsDto] = valid_channel_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto

    def create(self, channel: ChannelCreateOutDsDto):
        self.create_input = channel
        return self.create_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output


def create_interactor(
        gateway=ChannelCreateRepositoryImpl(),
        presenter=ChannelCreateOututPortImpl()) -> ChannelCreateInteractor:
    return ChannelCreateInteractor(gateway, presenter)


def test_create_success():

    presenter = ChannelCreateOututPortImpl()
    gateway = ChannelCreateRepositoryImpl()

    gateway.create_output = valid_channel_ds_dto

    target = create_interactor(gateway, presenter)

    target.create(valid_channel_in_dto)

    assert presenter.get_channel() is not None


def test_create_fail():

    presenter = ChannelCreateOututPortImpl()
    gateway = ChannelCreateRepositoryImpl()

    target = create_interactor(gateway, presenter)

    channel_in_dto = valid_channel_in_dto.model_copy()
    channel_in_dto.name = None

    with pytest.raises(BusinessException):
        target.create(channel_in_dto)
