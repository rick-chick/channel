from datetime import datetime, timedelta
from sqlalchemy import create_engine

from channel.driver.db.sqlalchemy.models import (
    Base, UserTokenDataSource)
from channel.driver.db.sqlalchemy.sqlalchemy_user_token_repository import SqlalchemyUserTokenRepository

from channel.usecase.models import UserTokenCreateInDsDto, UserTokenDeleteInDsDto

from sqlalchemy.orm import sessionmaker
import pytest
from uuid import uuid4

from tests.conftest import DATABASE_URL
from tests.channel.factories import (
    UserTokenCreateInDsDtoFactory
)

engine = create_engine(url=DATABASE_URL, echo=True)

user_tokends_dto = UserTokenCreateInDsDtoFactory.build()
user_token_ds = UserTokenDataSource(
    **user_tokends_dto.model_dump()
)


@pytest.fixture(scope="module", autouse=True)
def scope_module():
    try:
        Base.metadata.create_all(bind=engine)

        session = sessionmaker(engine)()

        datas = []
        datas.append(user_token_ds)
        session.add_all(datas)
        session.commit()
        session.refresh(user_token_ds)
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
        target = SqlalchemyUserTokenRepository(session)
        user_token_ds_dto = UserTokenCreateInDsDtoFactory.build()
        user_token_output_ds_dto = target.create(user_token_ds_dto)

        assert user_token_output_ds_dto is not None
        assert user_token_output_ds_dto.user_id is not None

    finally:
        session.rollback()


def test_exists_by_user_id_and_token_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyUserTokenRepository(session)

        # まず登録する
        user_token_ds_dto = UserTokenCreateInDsDtoFactory.build()
        target.create(user_token_ds_dto)

        ret = target.exists_by_user_id_and_token(
            user_id=user_token_ds_dto.user_id,
            token=user_token_ds_dto.token,
        )

        assert ret

        ret = target.exists_by_user_id_and_token(
            user_id='hoge',
            token=user_token_ds_dto.token,
        )

        assert not ret

        ret = target.exists_by_user_id_and_token(
            user_id=user_token_ds_dto.user_id,
            token='huga',
        )

        assert not ret

    finally:
        session.rollback()


def test_delete_success():
    session = sessionmaker(engine)()
    try:
        target = SqlalchemyUserTokenRepository(session)

        # まず登録する
        user_token_ds_dto = UserTokenCreateInDsDtoFactory.build()
        target.create(user_token_ds_dto)

        # 存在している
        ret = target.exists_by_user_id_and_token(
            user_id=user_token_ds_dto.user_id,
            token=user_token_ds_dto.token,
        )
        assert ret

        # 削除する(過去すぎて消せない)
        ret = target.delete(
            UserTokenDeleteInDsDto(
                user_id=user_token_ds.user_id,
                date_before=datetime.now() - timedelta(days=10)
            )
        )
        # 存在している
        ret = target.exists_by_user_id_and_token(
            user_id=user_token_ds_dto.user_id,
            token=user_token_ds_dto.token,
        )
        assert ret

        # 削除する(ユーザIDが違って消せない)
        ret = target.delete(
            UserTokenDeleteInDsDto(
                user_id='hoge',
                date_before=datetime.now() + timedelta(days=10)
            )
        )
        # 存在している
        ret = target.exists_by_user_id_and_token(
            user_id=user_token_ds_dto.user_id,
            token=user_token_ds_dto.token,
        )
        assert ret

        # 削除する
        ret = target.delete(
            UserTokenDeleteInDsDto(
                user_id=user_token_ds_dto.user_id,
                date_before=datetime.now() + timedelta(days=10)
            )
        )
        # 存在ないこと
        ret = target.exists_by_user_id_and_token(
            user_id=user_token_ds_dto.user_id,
            token=user_token_ds_dto.token,
        )
        assert not ret
    finally:
        session.rollback()
