from typing import List, Optional
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
    RecordOutDsDto,
)

from .models import RecordDataSource
from .sqlalchemy_translator import SqlalchemyRecordTranslator
from datetime import datetime


class SqlalchemyRecordRepository(RecordRepository):

    def __init__(self, session: Session):
        self.session = session

    def find_latest_by_channel_id(
        self,
        channel_id: int
    ) -> Optional[RecordOutDsDto]:
        result = self.session.query(
            RecordDataSource
        ).filter(
            RecordDataSource.channel_id == channel_id
        ).order_by(
            RecordDataSource.time.desc()
        ).limit(
            1
        ).first()

        if not result:
            return None
        return RecordOutDsDto.model_validate(result)

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

        filters = []

        if ds_dto.channel_ids:
            filters.append(RecordDataSource.channel_id.in_(ds_dto.channel_ids))

        if ds_dto.date_from:
            filters.append(RecordDataSource.time.__ge__(ds_dto.date_from))

        if ds_dto.date_to:
            filters.append(RecordDataSource.time.__le__(ds_dto.date_to))

        record_ds = self.session.query(
            RecordDataSource
        ).filter(
            and_(*filters)
        ).order_by(
            RecordDataSource.time
        ).all()

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
    ):

        filters = []
        if ds_dto.channel_ids:
            filters.append(
                RecordDataSource.channel_id.in_(ds_dto.channel_ids)
            )

        if len(filters) == 0:
            return

        self.session.query(
            RecordDataSource
        ).filter(
            and_(*filters)
        ).delete()

        self.session.commit()
