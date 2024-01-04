from datetime import datetime
from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from channel.driver.db.sqlalchemy import SqlalchemyRecordRepository
from channel.driver.db.sqlalchemy.models import Base, RecordDataSource
from channel.usecase.models import RecordCreateInDsDto
from tests.channel.factories import RecordCreateInDsDtoFactory, RecordDeleteInDsDtoFactory, RecordListInDsDtoFactory
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


def test_list_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyRecordRepository(session)

        # あらかじめデータを登録する
        target.create(RecordCreateInDsDtoFactory.build(
            channel_id=1,
            time=datetime(2023, 12, 23)
        ))
        target.create(RecordCreateInDsDtoFactory.build(
            channel_id=1,
            time=datetime(2023, 12, 24)
        ))
        target.create(RecordCreateInDsDtoFactory.build(
            channel_id=1,
            time=datetime(2023, 12, 25)
        ))
        target.create(RecordCreateInDsDtoFactory.build(
            channel_id=2,
            time=datetime(2023, 12, 26)
        ))

        ret = target.list(RecordListInDsDtoFactory.build(
            channel_ids=[1],
            date_from=datetime(2023, 12, 24),
            date_to=datetime(2023, 12, 26)
        ))

        assert len(ret) == 2
        assert ret[0].time == datetime(2023, 12, 24)
        assert ret[1].time == datetime(2023, 12, 25)

        ret = target.list(RecordListInDsDtoFactory.build(
            channel_ids=[1],
            date_from=datetime(2023, 12, 24),
            date_to=datetime(2023, 12, 24)
        ))

        assert len(ret) == 1
        assert ret[0].time == datetime(2023, 12, 24)

        ret = target.list(RecordListInDsDtoFactory.build(
            channel_ids=[1],
            date_from=datetime(2023, 12, 25),
            date_to=datetime(2023, 12, 26)
        ))

        assert len(ret) == 1
        assert ret[0].time == datetime(2023, 12, 25)

        ret = target.list(RecordListInDsDtoFactory.build(
            channel_ids=[1, 2],
            date_from=datetime(2023, 12, 24),
            date_to=datetime(2023, 12, 26)
        ))

        assert len(ret) == 3
    finally:
        session.rollback()


def test_delete_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyRecordRepository(session)

        # あらかじめデータを登録する
        target.create(RecordCreateInDsDtoFactory.build(
            channel_id=5,
            time=datetime(2023, 12, 23)
        ))
        target.create(RecordCreateInDsDtoFactory.build(
            channel_id=5,
            time=datetime(2023, 12, 24)
        ))
        target.create(RecordCreateInDsDtoFactory.build(
            channel_id=6,
            time=datetime(2023, 12, 25)
        ))
        target.create(RecordCreateInDsDtoFactory.build(
            channel_id=7,
            time=datetime(2023, 12, 26)
        ))

        ret = target.list(RecordListInDsDtoFactory.build(
            channel_ids=[5, 6, 7],
        ))

        assert len(ret) == 4

        target.delete(RecordDeleteInDsDtoFactory.build(
            channel_ids=[5, 6],
        ))

        ret = target.list(RecordListInDsDtoFactory.build(
            channel_ids=[5, 6, 7],
        ))

        assert len(ret) == 1
        assert ret[0].channel_id == 7

    finally:
        session.rollback()
