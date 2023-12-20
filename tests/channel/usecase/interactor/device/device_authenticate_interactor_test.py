from typing import Optional

import pytest

from channel.usecase.exception import BusinessException
from channel.usecase.interactor.device.device_authenticate_interactor import (
    DeviceAuthenticateInteractor,
)
from channel.usecase.models import DeviceAuthenticateOutDto, DeviceSessionDsDto
from channel.usecase.output_port.device.device_authenticate_output_port import (
    DeviceAuthenticateOututPort,
)
from channel.usecase.repository.device.device_authenticate_repository import (
    DeviceAuthenticateRepository,
)
from tests.channel.factories import (
    DeviceAuthenticateInDtoFactory,
    DeviceOutDsDtoFactory,
)

valid_device_in_dto = DeviceAuthenticateInDtoFactory.build()
valid_device_out_ds_dto = DeviceOutDsDtoFactory.build()


class DeviceAuthenticateOututPortImpl(DeviceAuthenticateOututPort):

    def __init__(self):
        self.exceptions = []
        self.device: Optional[DeviceAuthenticateOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, device: DeviceAuthenticateOutDto) -> DeviceAuthenticateOutDto:
        self.device = device
        return self.device


class DeviceAuthenticateRepositoryImpl(DeviceAuthenticateRepository):

    find_device_id_by_api_key_out: Optional[int] = 0

    def find_device_id_by_api_key(self, api_key: str) -> Optional[int]:
        self.find_device_by_api_key_in = api_key
        return self.find_device_id_by_api_key_out

    def save_device_session(self, device_session_ds_dto: DeviceSessionDsDto):
        self.save_device_session_in = device_session_ds_dto


def create_interactor(
        gateway=DeviceAuthenticateRepositoryImpl(),
        presenter=DeviceAuthenticateOututPortImpl()) -> DeviceAuthenticateInteractor:
    return DeviceAuthenticateInteractor(gateway, presenter)


def test_authenticate_success():

    presenter = DeviceAuthenticateOututPortImpl()
    gateway = DeviceAuthenticateRepositoryImpl()

    target = create_interactor(gateway, presenter)

    target.authenticate(valid_device_in_dto)

    assert presenter.device is not None


def test_authenticate_fail():

    presenter = DeviceAuthenticateOututPortImpl()
    gateway = DeviceAuthenticateRepositoryImpl()
    gateway.find_device_id_by_api_key_out = None

    target = create_interactor(gateway, presenter)

    device_in_dto = valid_device_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.authenticate(device_in_dto)
