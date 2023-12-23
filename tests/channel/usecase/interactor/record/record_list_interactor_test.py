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
    ChanneListOutDsDtoFactory,
    RecordListOutDsDtoFactory,
    RecordListInDtoFactory,
    UserSessionDsDtoFactory
)

import pytest
from typing import Optional, List

valid_record_in_dto = RecordListInDtoFactory.build()
valid_record_ds_dto = RecordListOutDsDtoFactory.batch(3)
valid_session_user_ds_dto = UserSessionDsDtoFactory.build()
valid_channel_ds_dto = ChanneListOutDsDtoFactory.batch(3)

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
