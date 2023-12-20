from sqlalchemy import create_engine

from channel.driver.db.sqlalchemy.models import (
    Base, RecordDataSource)
from channel.driver.db.sqlalchemy import SqlalchemyRecordRepository

from channel.usecase.models import RecordCreateInDsDto

from sqlalchemy.orm import sessionmaker
import pytest
from uuid import uuid4

from tests.conftest import DATABASE_URL
from tests.channel.factories import (
    RecordCreateInDsDtoFactory
)

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
    target = SqlalchemyRecordRepository(session)
    record_ds_dto = RecordCreateInDsDtoFactory.build()
    record_output_ds_dto = target.create(record_ds_dto)

    assert record_output_ds_dto is not None
    session.rollback()
