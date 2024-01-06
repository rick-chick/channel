import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from channel.driver.db.sqlalchemy import SqlalchemyChannelRepository
from channel.driver.db.sqlalchemy.models import Base, ChannelDataSource
from tests.channel.factories import ChannelCreateInDsDtoFactory, ChannelDeleteInDsDtoFactory, ChannelListInDsDtoFactory
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
    try:
        target = SqlalchemyChannelRepository(session)

        res = target.find_by_id(channel_ds.id)
        assert res is not None
    finally:
        session.rollback()


def test_find_by_id_when_id_is_missing():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyChannelRepository(session)
        res = target.find_by_id(-1)
        assert res is None
    finally:
        session.rollback()


def test_find_by_id_when_id_is_none():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyChannelRepository(session)
        res = target.find_by_id(None)
        assert res is None
    finally:
        session.rollback()


def test_create_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyChannelRepository(session)
        channel_ds_dto = ChannelCreateInDsDtoFactory.build()
        channel_output_ds_dto = target.create(channel_ds_dto)

        assert channel_output_ds_dto is not None
        assert channel_output_ds_dto.id is not None
    finally:
        session.rollback()


def test_list_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyChannelRepository(session)

        # 登録
        channel1 = target.create(ChannelCreateInDsDtoFactory.build(
            device_id=1
        ))
        channel2 = target.create(ChannelCreateInDsDtoFactory.build(
            device_id=3
        ))
        channel3 = target.create(ChannelCreateInDsDtoFactory.build(
            device_id=2
        ))

        ret = target.list(ChannelListInDsDtoFactory.build(
            device_id=None,
            device_ids=[1, 2]
        ))

        assert len(ret) == 2
        assert channel1.id in [ds_dto.id for ds_dto in ret]
        assert channel3.id in [ds_dto.id for ds_dto in ret]

    finally:
        session.rollback()


def test_delete_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyChannelRepository(session)

        # 登録
        channel1 = target.create(ChannelCreateInDsDtoFactory.build(
            device_id=4
        ))
        channel2 = target.create(ChannelCreateInDsDtoFactory.build(
            device_id=6
        ))
        channel3 = target.create(ChannelCreateInDsDtoFactory.build(
            device_id=5
        ))

        ret = target.list(ChannelListInDsDtoFactory.build(
            device_id=None,
            device_ids=[4, 5, 6]
        ))

        assert len(ret) == 3

        ret = target.delete(ChannelDeleteInDsDtoFactory.build(
            ids=None,
            device_ids=[4, 5]
        ))

        assert len(ret) == 2
        assert channel1.id in [ds_dto.id for ds_dto in ret]
        assert channel3.id in [ds_dto.id for ds_dto in ret]

    finally:
        session.rollback()
