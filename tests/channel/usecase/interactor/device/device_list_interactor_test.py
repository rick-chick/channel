from channel.usecase.interactor.device import DeviceListInteractor
from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    DeviceListInDsDto,
    DeviceListOutDsDto,
    DeviceListInDto,
    DeviceListOutDto,
    RecordOutDsDto,
    UserSessionDsDto
)
from channel.usecase.output_port.device import DeviceListOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.device import DeviceListRepository

from tests.channel.factories import (
    ChannelListOutDsDtoFactory,
    DeviceListOutDsDtoFactory,
    DeviceListInDtoFactory,
    DeviceListOutDtoFactory,
    RecordOutDsDtoFactory,
    UserSessionDsDtoFactory
)

import pytest
from typing import Optional, List

valid_device_in_dto = DeviceListInDtoFactory.build()
valid_device_ds_dto = DeviceListOutDsDtoFactory.batch(3)
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()
valid_channel_ds_dto = ChannelListOutDsDtoFactory.batch(
    3,
    device_id=valid_device_ds_dto[0].id
)
valid_find_latest_record_by_channel_id = RecordOutDsDtoFactory.build()


class DeviceListOututPortImpl(DeviceListOututPort):

    def __init__(self):
        self.exceptions = []
        self.device: Optional[DeviceListOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, device: DeviceListOutDto):
        self.device = device
        return device


class DeviceListRepositoryImpl(DeviceListRepository):

    list_input: Optional[DeviceListInDsDto] = None
    list_output: List[DeviceListOutDsDto] = valid_device_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto
    list_channel_out: List[ChannelListOutDsDto] = valid_channel_ds_dto
    find_latest_record_by_channel_id_output: Optional[
        RecordOutDsDto] = valid_find_latest_record_by_channel_id
    find_latest_record_by_channel_id_input = []

    def list(
        self,
        device_dto: DeviceListInDsDto
    ) -> List[DeviceListOutDsDto]:
        self.list_input = device_dto
        return self.list_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output

    def list_channel(
        self,
        channel_dto: ChannelListInDsDto
    ) -> List[ChannelListOutDsDto]:
        self.list_channel_in = channel_dto
        return self.list_channel_out

    def find_latest_record_by_channel_id(
        self,
        channel_id: int
    ) -> Optional[RecordOutDsDto]:
        self.find_latest_record_by_channel_id_input.append(channel_id)
        return self.find_latest_record_by_channel_id_output


def create_interactor(
        gateway=DeviceListRepositoryImpl(),
        presenter=DeviceListOututPortImpl()) -> DeviceListInteractor:
    return DeviceListInteractor(gateway, presenter)


def test_list_success():

    presenter = DeviceListOututPortImpl()
    gateway = DeviceListRepositoryImpl()

    gateway.list_output = valid_device_ds_dto

    target = create_interactor(gateway, presenter)

    target.list(valid_device_in_dto)

    assert presenter.device is not None
    assert len(presenter.device.values) > 0
    assert len(presenter.device.values[0].channels) > 0
    assert presenter.device.values[0].channels[0].record == valid_find_latest_record_by_channel_id.value
    assert presenter.device.values[0].latest_time == valid_find_latest_record_by_channel_id.time
    assert gateway.find_latest_record_by_channel_id_input[0] in [
        dto.id for dto in valid_channel_ds_dto
    ]
    assert presenter.device.values[0].channels[0].unit == valid_channel_ds_dto[0].unit


def test_list_fail():

    presenter = DeviceListOututPortImpl()
    gateway = DeviceListRepositoryImpl()
    gateway.load_session_user_output = None

    target = create_interactor(gateway, presenter)

    device_in_dto = valid_device_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.list(device_in_dto)
