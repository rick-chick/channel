from channel.usecase.interactor.device import DeviceDeleteInteractor
from channel.usecase.models import (
    ChannelDeleteInDsDto,
    ChannelDeleteOutDsDto,
    ChannelListInDsDto,
    ChannelListOutDsDto,
    DeviceDeleteInDto,
    DeviceDeleteInDsDto,
    DeviceDeleteOutDsDto,
    DeviceDeleteOutDto,
    RecordDeleteInDsDto,
    RecordDeleteOutDsDto,
    UserSessionDsDto
)
from channel.usecase.output_port.device import DeviceDeleteOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.device import DeviceDeleteRepository

from tests.channel.factories import (
    ChannelDeleteOutDsDtoFactory,
    DeviceDeleteOutDsDtoFactory,
    DeviceDeleteInDtoFactory,
    RecordDeleteOutDsDtoFactory,
    UserSessionDsDtoFactory
)

from typing import Optional, List
import pytest

valid_session_user_ds_dto = UserSessionDsDtoFactory.build()
valid_device_ds_dto = DeviceDeleteOutDsDtoFactory.batch(3)
valid_channel_ds_dto = ChannelDeleteOutDsDtoFactory.batch(3)
valid_record_ds_dto = RecordDeleteOutDsDtoFactory.batch(3)

valid_device_in_dto = DeviceDeleteInDto(
    ids=[device.id for device in valid_device_ds_dto]
)


class DeviceDeleteOututPortImpl(DeviceDeleteOututPort):

    def __init__(self):
        self.exceptions = []
        self.device_dto: Optional[DeviceDeleteOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, device_dto: DeviceDeleteOutDto) -> DeviceDeleteOutDto:
        self.device_dto = device_dto
        return device_dto


class DeviceDeleteRepositoryImpl(DeviceDeleteRepository):

    delete_input: Optional[DeviceDeleteInDsDto] = None
    delete_output: List[DeviceDeleteOutDsDto] = valid_device_ds_dto
    delete_channel_output: List[ChannelDeleteOutDsDto] = valid_channel_ds_dto
    delete_record_output: List[RecordDeleteOutDsDto] = valid_record_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto

    def delete(
        self,
        device_dto: DeviceDeleteInDsDto
    ) -> List[DeviceDeleteOutDsDto]:
        self.delete_input = device_dto
        return self.delete_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output

    def delete_channel(
        self,
        channel_dto: ChannelDeleteInDsDto
    ) -> List[ChannelDeleteOutDsDto]:
        self.delete_channel_input = channel_dto
        return self.delete_channel_output

    def delete_record(
        self,
        record_dto: RecordDeleteInDsDto
    ) -> List[RecordDeleteOutDsDto]:
        self.delete_record_input = record_dto
        return self.delete_record_output


def create_interactor(
        gateway=DeviceDeleteRepositoryImpl(),
        presenter=DeviceDeleteOututPortImpl()) -> DeviceDeleteInteractor:
    return DeviceDeleteInteractor(gateway, presenter)


def test_delete_success():

    presenter = DeviceDeleteOututPortImpl()
    gateway = DeviceDeleteRepositoryImpl()

    gateway.delete_output = valid_device_ds_dto

    target = create_interactor(gateway, presenter)

    target.delete(valid_device_in_dto)

    assert presenter.device_dto is not None
    assert len(presenter.device_dto.ids) == 3
    assert gateway.delete_input
    assert gateway.delete_input.user_id == valid_session_user_ds_dto.id

    assert gateway.delete_channel_input
    assert gateway.delete_channel_input.device_ids == valid_device_in_dto.ids

    assert gateway.delete_record_input
    assert gateway.delete_record_input.channel_ids == [
        dto.id for dto in valid_channel_ds_dto
    ]


def test_delete_fail():

    presenter = DeviceDeleteOututPortImpl()
    gateway = DeviceDeleteRepositoryImpl()

    gateway.load_session_user_output = None

    target = create_interactor(gateway, presenter)
    with pytest.raises(BusinessException):
        target.delete(valid_device_in_dto)


def test_delete_warrn_when_there_is_undeleted():

    presenter = DeviceDeleteOututPortImpl()
    gateway = DeviceDeleteRepositoryImpl()

    gateway.delete_output = valid_device_ds_dto[1:]

    target = create_interactor(gateway, presenter)

    ret = target.delete(valid_device_in_dto)

    assert len(ret.ids) == 2
    assert valid_device_ds_dto[0].id not in ret.ids
    assert valid_device_ds_dto[0].id in ret.undeleted_ids
