from sqlalchemy import and_
from channel.adapter.gateway.device.device_repository import DeviceRepository
from .models import DeviceDataSource
from .sqlalchemy_translator import SqlalchemyDeviceTranslator

from channel.usecase.models import (
    DeviceCreateInDsDto,
    DeviceCreateOutDsDto,
    DeviceUpdateInDsDto,
    DeviceUpdateOutDsDto,
    DeviceOutDsDto,
    DeviceListInDsDto,
    DeviceListOutDsDto,
    DeviceDeleteInDsDto,
    DeviceDeleteOutDsDto
)

from typing import Optional, List
from sqlalchemy.orm import Session


class SqlalchemyDeviceRepository(DeviceRepository):

    def __init__(self, session: Session):
        self.session = session

    def find_by_id(self, id: Optional[int]) -> Optional[DeviceOutDsDto]:
        if id is None:
            return None

        device_ds = self.session.query(DeviceDataSource)\
            .filter_by(id=id)\
            .first()

        if device_ds:
            return DeviceOutDsDto.model_validate(device_ds)
        return None

    def find_id_by_api_key(self, api_key: str) -> Optional[int]:
        device_ds = self.session.query(DeviceDataSource)\
            .filter_by(api_key=api_key)\
            .first()

        if device_ds:
            return device_ds.id
        return None

    def exists_by_id(self, id: Optional[int]) -> bool:
        if id is None:
            return False

        return self.session.query(self.session.query(DeviceDataSource)
                                  .filter_by(id=id).exists()).scalar()

    def list(
        self,
        ds_dto: DeviceListInDsDto
    ) -> List[DeviceListOutDsDto]:

        # where句
        where = and_(
            DeviceDataSource.user_id == ds_dto.user_id
        )

        # 検索
        device_ds = self.session.query(
            DeviceDataSource
        ).filter(
            where
        ).all()

        if not device_ds:
            return []

        return [
            DeviceListOutDsDto.model_validate(ds)
            for ds in device_ds
        ]

    def create(
        self,
        ds_dto: DeviceCreateInDsDto
    ) -> DeviceCreateOutDsDto:

        device_ds = SqlalchemyDeviceTranslator.create(ds_dto)
        self.session.add(device_ds)
        self.session.commit()
        return DeviceCreateOutDsDto.model_validate(device_ds)

    def update(
        self,
        ds_dto: DeviceUpdateInDsDto
    ) -> Optional[DeviceUpdateOutDsDto]:

        device_ds = self.session.query(DeviceDataSource).filter_by(
            id=ds_dto.id).first()
        if device_ds is None:
            return None
        device_ds = SqlalchemyDeviceTranslator.update(
            device_ds, ds_dto)
        self.session.commit()
        return DeviceUpdateOutDsDto.model_validate(device_ds)

    def delete(
        self,
        device_ds_dto: DeviceDeleteInDsDto
    ) -> List[DeviceDeleteOutDsDto]:
        if device_ds_dto.ids is None:
            return []

        device_ds = self.session.query(DeviceDataSource).filter(
            DeviceDataSource.id.in_(device_ds_dto.ids)).all()
        if not device_ds:
            return []

        ret = []
        for ds in device_ds:
            ret.append(DeviceDeleteOutDsDto.model_validate(ds))
            self.session.delete(ds)

        self.session.commit()
        return ret
