from uuid import uuid4

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from channel.driver.db.sqlalchemy import SqlalchemyUserRepository
from channel.driver.db.sqlalchemy.models import Base, UserDataSource
from tests.channel.factories import UserCreateInDsDtoFactory
from tests.conftest import DATABASE_URL


engine = create_engine(url=DATABASE_URL, echo=True)


user_ds = UserDataSource(
    id=str(uuid4()),
    email="test@hoge.com",
    password_hash=str(uuid4()),
    created_by=str(uuid4()),
    updated_by=str(uuid4()),
)


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    try:
        Base.metadata.create_all(bind=engine)

        session = sessionmaker(engine)()

        datas = []
        datas.append(user_ds)
        session.add_all(datas)
        session.commit()
        session.refresh(user_ds)
        session.close()

        try:
            yield
        except Exception:
            pass

    finally:
        Base.metadata.drop_all(bind=engine)


def test_find_by_id_success():
    session = sessionmaker(engine)()
    target = SqlalchemyUserRepository(session)

    res = target.find_by_id(user_ds.id)
    assert res is not None
    session.rollback()


def test_find_by_id_when_id_is_missing():
    session = sessionmaker(engine)()
    target = SqlalchemyUserRepository(session)
    res = target.find_by_id("")
    assert res is None

    session.rollback()


def test_find_by_id_when_id_is_none():
    session = sessionmaker(engine)()
    target = SqlalchemyUserRepository(session)
    res = target.find_by_id("")
    assert res is None
    session.rollback()


def test_create_success():
    session = sessionmaker(engine)()
    target = SqlalchemyUserRepository(session)
    user_ds_dto = UserCreateInDsDtoFactory.build()
    user_output_ds_dto = target.create(user_ds_dto)

    assert user_output_ds_dto is not None
    assert user_output_ds_dto.id is not None
    session.rollback()
