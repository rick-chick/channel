from datetime import datetime
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from channel.driver.db.sqlalchemy import SqlalchemyRecordRepository
from channel.driver.db.sqlalchemy.models import Base, RecordDataSource
from channel.usecase.models import RecordCreateInDsDto
from tests.channel.factories import RecordCreateInDsDtoFactory
from tests.conftest import DATABASE_URL

engine = create_engine(url=DATABASE_URL, echo=True)

recordds_dto = RecordCreateInDsDtoFactory.build()
record_ds = RecordDataSource(
    **recordds_dto.model_dump()
)


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    try:
        Base.metadata.create_all(bind=engine)

        session = sessionmaker(engine)()

        datas = []
        datas.append(record_ds)
        session.add_all(datas)
        session.commit()
        session.refresh(record_ds)
        session.close()

        try:
            yield
        except Exception:
            pass

    finally:
        Base.metadata.drop_all(bind=engine)


def test_create_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyRecordRepository(session)
        record_ds_dto = RecordCreateInDsDtoFactory.build()
        record_output_ds_dto = target.create(record_ds_dto)

        assert record_output_ds_dto is not None
    finally:
        session.rollback()


def test_exists_by_device_id_time_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyRecordRepository(session)

        record_ds_dto = RecordCreateInDsDtoFactory.build()
        record_output_ds_dto = target.create(record_ds_dto)

        record_ds_dto = RecordCreateInDsDtoFactory.build()
        record_output_ds_dto = target.create(record_ds_dto)

        ret = target.exists_by_channel_ids_time(
            [record_ds_dto.channel_id],
            record_output_ds_dto.time
        )

        assert ret
    finally:
        session.rollback()

def test_exists_by_device_id_time_fail():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyRecordRepository(session)

        record_ds_dto = RecordCreateInDsDtoFactory.build()
        target.create(record_ds_dto)

        record_ds_dto = RecordCreateInDsDtoFactory.build()
        target.create(record_ds_dto)

        ret = target.exists_by_channel_ids_time(
            [record_ds_dto.channel_id],
            datetime.now()
        )

        assert not ret

        ret = target.exists_by_channel_ids_time(
            [-1],
            record_ds_dto.time
        )

        assert not ret
    finally:
        session.rollback()
