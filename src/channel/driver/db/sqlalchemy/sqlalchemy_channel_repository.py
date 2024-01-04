from sqlalchemy import and_
from typing import List, Optional

from sqlalchemy.orm import Session

from channel.adapter.gateway.channel import ChannelRepository
from channel.usecase.models import (
    ChannelCreateInDsDto,
    ChannelCreateOutDsDto,
    ChannelDeleteInDsDto,
    ChannelDeleteOutDsDto,
    ChannelGetOutDsDto,
    ChannelListInDsDto,
    ChannelListOutDsDto,
    ChannelUpdateInDsDto,
    ChannelUpdateOutDsDto,
)

from .models import ChannelDataSource
from .sqlalchemy_translator import SqlalchemyChannelTranslator


class SqlalchemyChannelRepository(ChannelRepository):

    def __init__(self, session: Session):
        self.session = session

    def find_by_id(self, id: Optional[int]) -> Optional[ChannelGetOutDsDto]:
        if id is None:
            return None

        channel_ds = self.session.query(ChannelDataSource)\
            .filter_by(id=id)\
            .first()

        if channel_ds:
            return ChannelGetOutDsDto.model_validate(channel_ds)
        return None

    def exists_by_id(self, id: Optional[int]) -> bool:
        if id is None:
            return False

        return self.session.query(self.session.query(ChannelDataSource)
                                  .filter_by(id=id).exists()).scalar()

    def list(
        self,
        ds_dto: ChannelListInDsDto
    ) -> List[ChannelListOutDsDto]:
        filters = []

        # where 句
        if ds_dto.device_id:
            filters.append(
                ChannelDataSource.device_id == ds_dto.device_id
            )
        if ds_dto.device_ids:
            filters.append(
                ChannelDataSource.device_id.in_(ds_dto.device_ids)
            )

        # 検索
        channel_ds = self.session.query(
            ChannelDataSource
        ).filter(
            and_(*filters)
        ).all()

        if not channel_ds:
            return []

        return [
            ChannelListOutDsDto.model_validate(ds)
            for ds in channel_ds
        ]

    def create(
        self,
        ds_dto: ChannelCreateInDsDto
    ) -> ChannelCreateOutDsDto:

        channel_ds = SqlalchemyChannelTranslator.create(ds_dto)
        self.session.add(channel_ds)
        self.session.commit()
        return ChannelCreateOutDsDto.model_validate(channel_ds)

    def update(
        self,
        ds_dto: ChannelUpdateInDsDto
    ) -> Optional[ChannelUpdateOutDsDto]:

        channel_ds = self.session.query(ChannelDataSource).filter_by(
            id=ds_dto.id).first()
        if channel_ds is None:
            return None
        channel_ds = SqlalchemyChannelTranslator.update(
            channel_ds, ds_dto)
        self.session.commit()
        return ChannelUpdateOutDsDto.model_validate(channel_ds)

    def delete(
        self,
        ds_dto: ChannelDeleteInDsDto
    ) -> List[ChannelDeleteOutDsDto]:
        filters = []
        if ds_dto.ids:
            filters.append(ChannelDataSource.id.in_(ds_dto.ids))

        if ds_dto.device_ids:
            filters.append(ChannelDataSource.device_id.in_(ds_dto.device_ids))

        channel_ds = self.session.query(
            ChannelDataSource
        ).filter(
            and_(*filters)
        ).all()

        ret = []
        for ds in channel_ds:
            ret.append(ChannelDeleteOutDsDto.model_validate(ds))
            self.session.delete(ds)

        self.session.commit()
        return ret
