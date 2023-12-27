from datetime import datetime, timezone, tzinfo
from channel.usecase.interactor.record import RecordListInteractor
from channel.usecase.models import (
    ChannelListInDsDto,
    ChannelListOutDsDto,
    RecordListInDsDto,
    RecordListOutDsDto,
    RecordListOutDto,
    UserSessionDsDto
)
from channel.usecase.output_port.record import RecordListOututPort
from channel.usecase.exception import BusinessException
from channel.usecase.repository.record import RecordListRepository

from tests.channel.factories import (
    ChannelListOutDsDtoFactory,
    RecordListOutDsDtoFactory,
    RecordListInDtoFactory,
    UserSessionDsDtoFactory
)

import pytest
from typing import Optional, List

valid_record_in_dto = RecordListInDtoFactory.build()
valid_record_ds_dto = RecordListOutDsDtoFactory.batch(3)
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()
valid_channel_ds_dto = ChannelListOutDsDtoFactory.batch(3)


class RecordListOututPortImpl(RecordListOututPort):

    def __init__(self):
        self.exceptions = []
        self.record: Optional[RecordListOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, record: RecordListOutDto):
        self.record = record
        return record


class RecordListRepositoryImpl(RecordListRepository):

    list_input: Optional[RecordListInDsDto] = None
    list_output: List[RecordListOutDsDto] = valid_record_ds_dto
    load_session_user_output: Optional[UserSessionDsDto] = valid_session_user_ds_dto
    channel_list_output: List[ChannelListOutDsDto] = valid_channel_ds_dto

    def list(
        self,
        record_dto: RecordListInDsDto
    ) -> List[RecordListOutDsDto]:
        self.list_input = record_dto
        return self.list_output

    def channel_list(
        self,
        channel_dto: ChannelListInDsDto
    ) -> List[ChannelListOutDsDto]:
        self.channel_list_input = channel_dto
        return self.channel_list_output

    def load_session_user(self) -> Optional[UserSessionDsDto]:
        return self.load_session_user_output


def create_interactor(
        gateway=RecordListRepositoryImpl(),
        presenter=RecordListOututPortImpl()) -> RecordListInteractor:
    return RecordListInteractor(gateway, presenter)


def test_list_success():

    presenter = RecordListOututPortImpl()
    gateway = RecordListRepositoryImpl()

    gateway.list_output = valid_record_ds_dto

    target = create_interactor(gateway, presenter)

    target.list(valid_record_in_dto)

    assert presenter.record is not None


def test_list_fail_if_user_not_authenticated():

    presenter = RecordListOututPortImpl()
    gateway = RecordListRepositoryImpl()
    gateway.load_session_user_output = None

    target = create_interactor(gateway, presenter)

    record_in_dto = valid_record_in_dto.model_copy()

    with pytest.raises(BusinessException):
        target.list(record_in_dto)


def test_list_aggregate_success():
    presenter = RecordListOututPortImpl()
    gateway = RecordListRepositoryImpl()

    target = create_interactor(gateway, presenter)

    record_in_dto = valid_record_in_dto.model_copy()
    record_in_dto.date_from = datetime(2000, 1, 1, 0, 0, 0, 0, timezone.utc)
    record_in_dto.date_to = datetime(2000, 1, 2, 0, 0, 0, 0, timezone.utc)
    record_in_dto.span = 30

    gateway.channel_list_output = [
        ChannelListOutDsDtoFactory.build(
            id=1,
            name='hoge',
        )
    ]

    gateway.list_output = [
        RecordListOutDsDtoFactory.build(
            time=datetime(2000, 1, 1, 0, 0, 30, 0, timezone.utc),
            channel_id=1,
            value=2
        ),
        RecordListOutDsDtoFactory.build(
            time=datetime(2000, 1, 1, 0, 29, 59, 0, timezone.utc),
            channel_id=1,
            value=4
        ),
        RecordListOutDsDtoFactory.build(
            time=datetime(2000, 1, 1, 0, 30, 0, 0, timezone.utc),
            channel_id=1,
            value=2
        ),
    ]

    ret = target.list(record_in_dto)
    assert ret.labels[0] == datetime(2000, 1, 1, 0, 0, 0, 0, timezone.utc)
    assert ret.labels[1] == datetime(2000, 1, 1, 0, 30, 0, 0, timezone.utc)
    assert len(ret.datasets) == 1
    assert ret.datasets[0].label == 'hoge'
    assert ret.datasets[0].data[0] == 3
    assert ret.datasets[0].data[1] == 2


def test_list_aggregate_success_when_first_spna_has_no_item():
    presenter = RecordListOututPortImpl()
    gateway = RecordListRepositoryImpl()

    target = create_interactor(gateway, presenter)

    record_in_dto = valid_record_in_dto.model_copy()
    record_in_dto.date_from = datetime(2000, 1, 1, 0, 0, 0, 0, timezone.utc)
    record_in_dto.date_to = datetime(2000, 1, 2, 0, 0, 0, 0, timezone.utc)
    record_in_dto.span = 30

    gateway.channel_list_output = [
        ChannelListOutDsDtoFactory.build(
            id=1,
            name='hoge',
        )
    ]

    gateway.list_output = [
        RecordListOutDsDtoFactory.build(
            time=datetime(2000, 1, 1, 1, 0, 30, 0, timezone.utc),
            channel_id=1,
            value=2
        ),
        RecordListOutDsDtoFactory.build(
            time=datetime(2000, 1, 1, 1, 29, 59, 0, timezone.utc),
            channel_id=1,
            value=4
        ),
        RecordListOutDsDtoFactory.build(
            time=datetime(2000, 1, 1, 1, 30, 00, 0, timezone.utc),
            channel_id=1,
            value=2
        ),
    ]

    ret = target.list(record_in_dto)
    assert ret.labels[0] == datetime(2000, 1, 1, 0, 0, 0, 0, timezone.utc)
    assert ret.labels[1] == datetime(2000, 1, 1, 0, 30, 0, 0, timezone.utc)
    assert len(ret.datasets) == 1
    assert len(ret.labels) == len(ret.datasets[0].data)
    assert ret.datasets[0].label == 'hoge'
    assert ret.datasets[0].data[2] == 3
    assert ret.datasets[0].data[3] == 2


def test_list_aggregate_success_when_range_is_60():
    presenter = RecordListOututPortImpl()
    gateway = RecordListRepositoryImpl()

    target = create_interactor(gateway, presenter)

    record_in_dto = valid_record_in_dto.model_copy()
    record_in_dto.date_from = datetime(2000, 1, 1, 0, 0, 0, 0, timezone.utc)
    record_in_dto.date_to = datetime(2000, 1, 2, 0, 0, 0, 0, timezone.utc)
    record_in_dto.span = 60

    gateway.channel_list_output = [
        ChannelListOutDsDtoFactory.build(
            id=1,
            name='hoge',
        )
    ]

    gateway.list_output = [
        RecordListOutDsDtoFactory.build(
            time=datetime(2000, 1, 1, 0, 0, 30, 0, timezone.utc),
            channel_id=1,
            value=2
        ),
        RecordListOutDsDtoFactory.build(
            time=datetime(2000, 1, 1, 0, 29, 59, 0, timezone.utc),
            channel_id=1,
            value=4
        ),
        RecordListOutDsDtoFactory.build(
            time=datetime(2000, 1, 1, 0, 30, 00, 0, timezone.utc),
            channel_id=1,
            value=2
        ),
    ]

    ret = target.list(record_in_dto)
    assert ret.labels[0] == datetime(2000, 1, 1, 0, 0, 0, 0, timezone.utc)
    assert ret.labels[1] == datetime(2000, 1, 1, 1, 0, 0, 0, timezone.utc)
    assert len(ret.labels) == len(ret.datasets[0].data)
    assert len(ret.datasets) == 1
    assert ret.datasets[0].label == 'hoge'
    assert ret.datasets[0].data[0] == 8/3
    assert ret.datasets[0].data[1] == 0
