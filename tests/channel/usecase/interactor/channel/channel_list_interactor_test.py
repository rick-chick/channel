from channel.usecase.interactor.channel import ChannelListInteractor
from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    ChannelListInDto,
    ChannelListOutDto,
    DeviceListInDsDto,
    DeviceListOutDsDto,
    UserSessionDsDto
)
from channel.usecase.output_port.channel import ChannelListOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.channel import ChannelListRepository

from tests.channel.factories import (
    ChannelListOutDsDtoFactory,
    ChannelListInDtoFactory,
    ChannelListOutDtoFactory,
    DeviceListOutDsDtoFactory,
    UserSessionDsDtoFactory
)

import pytest
from typing import Optional, List

valid_channel_in_dto = ChannelListInDtoFactory.build()
valid_channel_ds_dto = ChannelListOutDsDtoFactory.batch(3)
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()
valid_device_ds_dto = DeviceListOutDsDtoFactory.batch(3)


class ChannelListOututPortImpl(ChannelListOututPort):

    def __init__(self):
        self.exceptions = []
        self.channel: Optional[ChannelListOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, channel: ChannelListOutDto):
        self.channel = channel
        return channel


class ChannelListRepositoryImpl(ChannelListRepository):

    list_input: Optional[ChannelListInDsDto] = None
    list_output: List[ChannelListOutDsDto] = valid_channel_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto
    list_device_out: List[DeviceListOutDsDto] = valid_device_ds_dto

    def list(
        self,
        channel_dto: ChannelListInDsDto
    ):
        self.list_input = channel_dto
        return self.list_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output

    def list_device(
        self,
        device_dto: DeviceListInDsDto
    ) -> List[DeviceListOutDsDto]:
        self.list_device_in = device_dto
        return self.list_device_out


def create_interactor(
        gateway=ChannelListRepositoryImpl(),
        presenter=ChannelListOututPortImpl()) -> ChannelListInteractor:
    return ChannelListInteractor(gateway, presenter)


def test_list_success():

    presenter = ChannelListOututPortImpl()
    gateway = ChannelListRepositoryImpl()

    gateway.list_output = valid_channel_ds_dto

    target = create_interactor(gateway, presenter)

    target.list(valid_channel_in_dto)

    assert presenter.channel is not None


def test_list_fail():

    presenter = ChannelListOututPortImpl()
    gateway = ChannelListRepositoryImpl()
    gateway.load_session_user_output = None

    target = create_interactor(gateway, presenter)

    channel_in_dto = valid_channel_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.list(channel_in_dto)
