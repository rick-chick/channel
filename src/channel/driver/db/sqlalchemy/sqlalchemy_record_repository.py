from typing import List

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


class SqlalchemyRecordRepository(RecordRepository):

    def __init__(self, session: Session):
        self.session = session

    def list(
        self,
        record_ds_dto: RecordListInDsDto
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
        record_ds_dto: RecordDeleteInDsDto
    ) -> List[RecordDeleteOutDsDto]:
        if record_ds_dto.ids is None:
            return []

        record_ds = self.session.query(RecordDataSource).filter(
            RecordDataSource.id.in_(record_ds_dto.ids)).all()
        if not record_ds:
            return []

        ret = []
        for ds in record_ds:
            ret.append(RecordDeleteOutDsDto.model_validate(ds))
            self.session.delete(ds)

        self.session.commit()
        return ret
