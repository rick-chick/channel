import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from channel.driver.db.sqlalchemy import SqlalchemyDeviceRepository
from channel.driver.db.sqlalchemy.models import Base, DeviceDataSource
from tests.channel.factories import DeviceCreateInDsDtoFactory, DeviceListInDsDtoFactory
from tests.conftest import DATABASE_URL
from uuid import uuid4

engine = create_engine(url=DATABASE_URL, echo=True)


device_ds_dto = DeviceCreateInDsDtoFactory.build()
device_ds = DeviceDataSource(
    **device_ds_dto.model_dump(exclude={"tags"})
)


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    try:
        Base.metadata.create_all(bind=engine)

        session = sessionmaker(engine)()

        datas = []
        datas.append(device_ds)
        session.add_all(datas)
        session.commit()
        session.refresh(device_ds)
        session.close()

        try:
            yield
        except Exception:
            pass

    finally:
        Base.metadata.drop_all(bind=engine)


def test_find_by_id_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyDeviceRepository(session)

        res = target.find_by_id(device_ds.id)
        assert res is not None
    finally:
        session.rollback()


def test_find_by_id_when_id_is_missing():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyDeviceRepository(session)
        res = target.find_by_id(-1)
        assert res is None
    finally:
        session.rollback()


def test_find_by_id_when_id_is_none():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyDeviceRepository(session)
        res = target.find_by_id(None)
        assert res is None
    finally:
        session.rollback()


def test_create_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyDeviceRepository(session)
        device_ds_dto = DeviceCreateInDsDtoFactory.build()
        device_output_ds_dto = target.create(device_ds_dto)

        assert device_output_ds_dto is not None
        assert device_output_ds_dto.id is not None
    finally:
        session.rollback()


def test_list_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyDeviceRepository(session)
        user_id = str(uuid4())

        # 登録
        device1 = target.create(DeviceCreateInDsDtoFactory.build(
            user_id=user_id
        ))
        device2 = target.create(DeviceCreateInDsDtoFactory.build(
            user_id=user_id
        ))
        target.create(DeviceCreateInDsDtoFactory.build(
            user_id="hoge"
        ))

        device_output_ds_dto = target.list(DeviceListInDsDtoFactory.build(
            user_id=user_id
        ))

        assert device1.id in [ds_dto.id for ds_dto in device_output_ds_dto]
        assert device2.id in [ds_dto.id for ds_dto in device_output_ds_dto]

    finally:
        session.rollback()
