import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from channel.driver.db.sqlalchemy import SqlalchemyDeviceRepository
from channel.driver.db.sqlalchemy.models import Base, DeviceDataSource
from tests.channel.factories import DeviceCreateInDsDtoFactory
from tests.conftest import DATABASE_URL

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
    target = SqlalchemyDeviceRepository(session)

    res = target.find_by_id(device_ds.id)
    assert res is not None
    session.rollback()


def test_find_by_id_when_id_is_missing():
    session = sessionmaker(engine)()
    target = SqlalchemyDeviceRepository(session)
    res = target.find_by_id(-1)
    assert res is None
    session.rollback()


def test_find_by_id_when_id_is_none():
    session = sessionmaker(engine)()
    target = SqlalchemyDeviceRepository(session)
    res = target.find_by_id(None)
    assert res is None
    session.rollback()


def test_create_success():
    session = sessionmaker(engine)()
    target = SqlalchemyDeviceRepository(session)
    device_ds_dto = DeviceCreateInDsDtoFactory.build()
    device_output_ds_dto = target.create(device_ds_dto)

    assert device_output_ds_dto is not None
    assert device_output_ds_dto.id is not None
    session.rollback()
