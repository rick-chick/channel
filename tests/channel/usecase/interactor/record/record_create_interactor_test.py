from channel.usecase.interactor.record import RecordCreateInteractor
from channel.usecase.models import (
    DeviceSessionDsDto,
    RecordCreateInDsDto,
    RecordCreateOutDsDto,
    RecordCreateOutDto,
    UserSessionDsDto,
)
from channel.usecase.output_port.record import RecordCreateOututPort
from channel.usecase.exception import (
    BusinessException,
    UnauthorizedException,
    RecordExistsException
)
from channel.usecase.repository.record import RecordCreateRepository

from tests.channel.factories import (
    DeviceSessionDsDtoFactory,
    RecordCreateOutDsDtoFactory,
    RecordCreateInDtoFactory,
    UserSessionDsDtoFactory
)

import pytest
from typing import Optional
from datetime import datetime

valid_record_in_dto = RecordCreateInDtoFactory.build()
valid_record_ds_dto = RecordCreateOutDsDtoFactory.build()
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()
valid_session_device_ds_dto = DeviceSessionDsDtoFactory.build()

class RecordCreateOututPortImpl(RecordCreateOututPort):

    def __init__(self):
        self.exceptions = []
        self.record: Optional[RecordCreateOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, record: RecordCreateOutDto) -> RecordCreateOutDto:
        self.record = record
        return self.record

class RecordCreateRepositoryImpl(RecordCreateRepository):

    create_input: Optional[RecordCreateInDsDto] = None
    create_output: RecordCreateOutDsDto = valid_record_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto
    find_device_id_by_api_key_input: Optional[str] = None
    load_session_device_out: Optional[DeviceSessionDsDto] = valid_session_device_ds_dto
    exists_record_by_channel_ids_time_out: bool = False

    def create(self, record: RecordCreateInDsDto) -> RecordCreateOutDsDto:
        self.create_input = record
        return self.create_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output

    def load_session_device(self) -> Optional[DeviceSessionDsDto]:
        return self.load_session_device_out

    def exists_record_by_channel_ids_time(
        self,
        device_id: int,
        time: datetime
    ) -> bool:
        self.exists_record_by_channel_ids_time_in = (device_id, time)
        return self.exists_record_by_channel_ids_time_out

def create_interactor(
        gateway=RecordCreateRepositoryImpl(),
        presenter=RecordCreateOututPortImpl()) -> RecordCreateInteractor:
    return RecordCreateInteractor(gateway, presenter)


def test_create_success():

    presenter = RecordCreateOututPortImpl()
    gateway = RecordCreateRepositoryImpl()

    gateway.create_output = valid_record_ds_dto

    target = create_interactor(gateway, presenter)

    target.create(valid_record_in_dto)

    assert presenter.record is not None


def test_create_fail_if_device_id_was_none():

    presenter = RecordCreateOututPortImpl()
    gateway = RecordCreateRepositoryImpl()
    gateway.load_session_device_out = None

    target = create_interactor(gateway, presenter)

    record_in_dto = valid_record_in_dto.model_copy()

    with pytest.raises(UnauthorizedException):
        target.create(record_in_dto)


def test_create_fail_if_duplicate_record():

    presenter = RecordCreateOututPortImpl()
    gateway = RecordCreateRepositoryImpl()
    gateway.exists_record_by_channel_ids_time_out = True

    target = create_interactor(gateway, presenter)

    record_in_dto = valid_record_in_dto.model_copy()

    with pytest.raises(RecordExistsException):
        target.create(record_in_dto)
