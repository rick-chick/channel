import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from channel.driver.db.sqlalchemy import SqlalchemyChannelRepository
from channel.driver.db.sqlalchemy.models import Base, ChannelDataSource
from tests.channel.factories import ChannelCreateInDsDtoFactory
from tests.conftest import DATABASE_URL

engine = create_engine(url=DATABASE_URL, echo=True)

channelds_dto = ChannelCreateInDsDtoFactory.build()
channel_ds = ChannelDataSource(
    **channelds_dto.model_dump(exclude={'tags'})
)


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    try:
        Base.metadata.create_all(bind=engine)

        session = sessionmaker(engine)()

        datas = []
        datas.append(channel_ds)
        session.add_all(datas)
        session.commit()
        session.refresh(channel_ds)
        session.close()

        try:
            yield
        except Exception:
            pass

    finally:
        Base.metadata.drop_all(bind=engine)


def test_find_by_id_success():
    session = sessionmaker(engine)()
    target = SqlalchemyChannelRepository(session)

    res = target.find_by_id(channel_ds.id)
    assert res is not None
    session.rollback()


def test_find_by_id_when_id_is_missing():
    session = sessionmaker(engine)()
    target = SqlalchemyChannelRepository(session)
    res = target.find_by_id(-1)
    assert res is None
    session.rollback()


def test_find_by_id_when_id_is_none():
    session = sessionmaker(engine)()
    target = SqlalchemyChannelRepository(session)
    res = target.find_by_id(None)
    assert res is None
    session.rollback()


def test_create_success():
    session = sessionmaker(engine)()
    target = SqlalchemyChannelRepository(session)
    channel_ds_dto = ChannelCreateInDsDtoFactory.build()
    channel_output_ds_dto = target.create(channel_ds_dto)

    assert channel_output_ds_dto is not None
    assert channel_output_ds_dto.id is not None
    session.rollback()
