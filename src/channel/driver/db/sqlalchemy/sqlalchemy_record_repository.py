from typing import List
from sqlalchemy import and_

from sqlalchemy.orm import Session

from channel.adapter.gateway.record import RecordRepository
from channel.usecase.models import (
    RecordCreateInDsDto,
    RecordCreateOutDsDto,
    RecordDeleteInDsDto,
    RecordDeleteOutDsDto,
    RecordListInDsDto,
    RecordListOutDsDto,
)

from .models import RecordDataSource
from .sqlalchemy_translator import SqlalchemyRecordTranslator
from datetime import datetime


class SqlalchemyRecordRepository(RecordRepository):

    def __init__(self, session: Session):
        self.session = session

    def exists_by_channel_ids_time(
        self,
        channel_ids: List[int],
        time: datetime
    ):
        return self.session.query(
            self.session.query(RecordDataSource)
            .filter(and_(
                RecordDataSource.channel_id.in_(channel_ids),
                RecordDataSource.time == time
            )).exists()
        ).scalar()

    def list(
        self,
        ds_dto: RecordListInDsDto
    ) -> List[RecordListOutDsDto]:

        record_ds = self.session.query(RecordDataSource).all()

        if not record_ds:
            return []

        return [
            RecordListOutDsDto.model_validate(ds)
            for ds in record_ds
        ]

    def create(
        self,
        ds_dto: RecordCreateInDsDto
    ) -> RecordCreateOutDsDto:

        record_ds = SqlalchemyRecordTranslator.create(ds_dto)
        self.session.add(record_ds)
        self.session.commit()
        return RecordCreateOutDsDto.model_validate(record_ds)

    def delete(
        self,
        ds_dto: RecordDeleteInDsDto
    ) -> List[RecordDeleteOutDsDto]:
        if ds_dto.ids is None:
            return []

        record_ds = self.session.query(RecordDataSource).filter(
            RecordDataSource.id.in_(ds_dto.ids)).all()
        if not record_ds:
            return []

        ret = []
        for ds in record_ds:
            ret.append(RecordDeleteOutDsDto.model_validate(ds))
            self.session.delete(ds)

        self.session.commit()
        return ret
