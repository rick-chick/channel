from channel.usecase.interactor.channel import ChannelDeleteInteractor
from channel.usecase.models import (
    ChannelDeleteInDto,
    ChannelDeleteInDsDto,
    ChannelDeleteOutDsDto,
    ChannelDeleteOutDto,
    UserSessionDsDto
)
from channel.usecase.output_port.channel import ChannelDeleteOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.channel import ChannelDeleteRepository

from tests.channel.factories import (
    ChannelDeleteOutDsDtoFactory,
    ChannelDeleteInDtoFactory,
    UserSessionDsDtoFactory
)

from typing import Optional, List
import pytest

valid_channel_ds_dto = ChannelDeleteOutDsDtoFactory.batch(3)

valid_channel_in_dto = ChannelDeleteInDto(
    ids=[channel.id for channel in valid_channel_ds_dto]
)
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()


class ChannelDeleteOututPortImpl(ChannelDeleteOututPort):

    def __init__(self):
        self.exceptions = []

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(
        self,
        channel_dto: ChannelDeleteOutDto
    ) -> ChannelDeleteOutDto:
        self.channel_dto = channel_dto
        return channel_dto


class ChannelDeleteRepositoryImpl(ChannelDeleteRepository):

    delete_input: Optional[ChannelDeleteInDsDto] = None
    delete_output: List[ChannelDeleteOutDsDto] = valid_channel_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto

    def delete(
        self,
        channel_dto: ChannelDeleteInDsDto
    ) -> List[ChannelDeleteOutDsDto]:
        self.delete_input = channel_dto
        return self.delete_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output


def create_interactor(
        gateway=ChannelDeleteRepositoryImpl(),
        presenter=ChannelDeleteOututPortImpl()) -> ChannelDeleteInteractor:
    return ChannelDeleteInteractor(gateway, presenter)


def test_delete_success():

    presenter = ChannelDeleteOututPortImpl()
    gateway = ChannelDeleteRepositoryImpl()

    gateway.delete_output = valid_channel_ds_dto

    target = create_interactor(gateway, presenter)

    target.delete(valid_channel_in_dto)

    assert presenter.channel_dto is not None
    assert len(presenter.channel_dto.ids) == 3
    assert gateway.delete_input is not None
    assert gateway.delete_input.ids is not None
    assert len(gateway.delete_input.ids) == 3


def test_delete_fail():

    presenter = ChannelDeleteOututPortImpl()
    gateway = ChannelDeleteRepositoryImpl()

    gateway.load_session_user_output = None

    target = create_interactor(gateway, presenter)
    with pytest.raises(BusinessException):
        target.delete(valid_channel_in_dto)
