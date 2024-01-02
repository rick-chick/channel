from channel.usecase.interactor.device import DeviceListInteractor
from channel.usecase.models import (
    DeviceListInDsDto,
    DeviceListOutDsDto,
    DeviceListInDto,
    DeviceListOutDto,
    UserSessionDsDto
)
from channel.usecase.output_port.device import DeviceListOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.device import DeviceListRepository

from tests.channel.factories import (
    DeviceListOutDsDtoFactory,
    DeviceListInDtoFactory,
    DeviceListOutDtoFactory,
    UserSessionDsDtoFactory
)

import pytest
from typing import Optional, List

valid_device_in_dto = DeviceListInDtoFactory.build()
valid_device_ds_dto = DeviceListOutDsDtoFactory.batch(3)
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()


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

    def list(
        self,
        device_dto: DeviceListInDsDto
    ) -> List[DeviceListOutDsDto]:
        self.list_input = device_dto
        return self.list_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output


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


def test_list_fail():

    presenter = DeviceListOututPortImpl()
    gateway = DeviceListRepositoryImpl()
    gateway.load_session_user_output = None

    target = create_interactor(gateway, presenter)

    device_in_dto = valid_device_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.list(device_in_dto)
