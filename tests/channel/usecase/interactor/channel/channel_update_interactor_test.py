from channel.usecase.interactor.channel import ChannelUpdateInteractor
from channel.usecase.models import (
    ChannelGetOutDsDto,
    ChannelUpdateInDsDto,
    ChannelUpdateOutDsDto,
    ChannelUpdateInDto,
    ChannelUpdateOutDto,
    UserSessionDsDto
)
from channel.usecase.output_port.channel import ChannelUpdateOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.channel import ChannelUpdateRepository

from tests.channel.factories import (
    ChannelGetOutDsDtoFactory,
    ChannelUpdateOutDsDtoFactory,
    ChannelUpdateInDtoFactory,
    ChannelUpdateOutDtoFactory,
    UserSessionDsDtoFactory
)

import pytest
from typing import Optional, List

valid_channel_in_dto = ChannelUpdateInDtoFactory.build()
valid_channel_ds_dto = ChannelUpdateOutDsDtoFactory.build()
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()
valid_channel_get_ds_dto = ChannelGetOutDsDtoFactory.build()


class ChannelUpdateOututPortImpl(ChannelUpdateOututPort):

    def __init__(self):
        self.exceptions = []
        self.channel: Optional[ChannelUpdateOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, channel: ChannelUpdateOutDto):
        self.channel = channel
        return channel


class ChannelUpdateRepositoryImpl(ChannelUpdateRepository):

    update_output: Optional[ChannelUpdateOutDsDto] = valid_channel_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto
    find_channel_by_id_output: Optional[ChannelGetOutDsDto] = valid_channel_get_ds_dto

    def update(
        self,
        channel: ChannelUpdateInDsDto
    ) -> Optional[ChannelUpdateOutDsDto]:
        self.update_input = channel
        return self.update_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output

    def find_channel_by_id(
        self,
        id: int
    ) -> Optional[ChannelGetOutDsDto]:
        self.find_channel_by_id_input = id
        return self.find_channel_by_id_output


def create_interactor(
        gateway=ChannelUpdateRepositoryImpl(),
        presenter=ChannelUpdateOututPortImpl()) -> ChannelUpdateInteractor:
    return ChannelUpdateInteractor(gateway, presenter)


def test_update_success():

    presenter = ChannelUpdateOututPortImpl()
    gateway = ChannelUpdateRepositoryImpl()

    gateway.update_output = valid_channel_ds_dto

    target = create_interactor(gateway, presenter)

    target.update(valid_channel_in_dto)

    assert presenter.channel is not None

    if valid_channel_in_dto.name:
        assert valid_channel_in_dto.name == gateway.update_input.name
    else:
        assert valid_channel_get_ds_dto.name == gateway.update_input.name
    if valid_channel_in_dto.unit:
        assert valid_channel_in_dto.unit == gateway.update_input.unit
    else:
        assert valid_channel_get_ds_dto.unit == gateway.update_input.unit


def test_update_fail():

    presenter = ChannelUpdateOututPortImpl()
    gateway = ChannelUpdateRepositoryImpl()
    gateway.load_session_user_output = None

    target = create_interactor(gateway, presenter)

    channel_in_dto = valid_channel_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.update(channel_in_dto)
