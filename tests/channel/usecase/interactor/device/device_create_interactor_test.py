from typing import Optional

import pytest

from channel.usecase.exception import BusinessException
from channel.usecase.interactor.device import DeviceCreateInteractor
from channel.usecase.models import (
    DeviceCreateInDsDto,
    DeviceCreateOutDsDto,
    DeviceCreateOutDto,
    UserSessionDsDto,
)
from channel.usecase.output_port.device import DeviceCreateOututPort
from channel.usecase.repository.device import DeviceCreateRepository
from tests.channel.factories import (
    DeviceCreateInDtoFactory,
    DeviceCreateOutDsDtoFactory,
    UserSessionDsDtoFactory,
)

valid_device_in_dto = DeviceCreateInDtoFactory.build()
valid_device_ds_dto = DeviceCreateOutDsDtoFactory.build()
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()


class DeviceCreateOututPortImpl(DeviceCreateOututPort):

    def __init__(self):
        self.exceptions = []
        self.device: Optional[DeviceCreateOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, device: DeviceCreateOutDto) -> DeviceCreateOutDto:
        self.device = device
        return self.device


class DeviceCreateRepositoryImpl(DeviceCreateRepository):

    create_input: Optional[DeviceCreateInDsDto] = None
    create_output: DeviceCreateOutDsDto = valid_device_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto

    def create(self, device: DeviceCreateInDsDto) -> DeviceCreateOutDsDto:
        self.create_input = device
        return self.create_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output


def create_interactor(
        gateway=DeviceCreateRepositoryImpl(),
        presenter=DeviceCreateOututPortImpl()) -> DeviceCreateInteractor:
    return DeviceCreateInteractor(gateway, presenter)


def test_create_success():

    presenter = DeviceCreateOututPortImpl()
    gateway = DeviceCreateRepositoryImpl()

    gateway.create_output = valid_device_ds_dto

    target = create_interactor(gateway, presenter)

    target.create(valid_device_in_dto)

    assert presenter.device is not None
    assert gateway.create_output.api_key is not None


def test_create_fail_when_user_unauthorized():

    presenter = DeviceCreateOututPortImpl()
    gateway = DeviceCreateRepositoryImpl()
    gateway.load_session_user_output = None

    target = create_interactor(gateway, presenter)

    device_in_dto = valid_device_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.create(device_in_dto)
