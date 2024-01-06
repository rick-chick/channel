from .models import UserTokenDataSource
from .sqlalchemy_translator import SqlalchemyUserTokenTranslator

from channel.adapter.gateway.user_token import UserTokenRepository

from channel.usecase.models import (
    UserTokenCreateInDsDto,
    UserTokenCreateOutDsDto,
    UserTokenDeleteInDsDto,
    UserTokenDeleteOutDsDto
)

from typing import Optional, List
from sqlalchemy.orm import Session
from datetime import datetime


class SqlalchemyUserTokenRepository(UserTokenRepository):

    def __init__(self, session: Session):
        self.session = session

    def exists_by_user_id_and_token(
        self,
        user_id: str,
        token: str
    ) -> bool:
        if id is None:
            return False

        return self.session.query(
            self.session.query(
                UserTokenDataSource
            )
            .filter(
                UserTokenDataSource.user_id.__eq__(user_id),
                UserTokenDataSource.token == token,
            ).exists()
        ).scalar()

    def create(
        self,
        ds_dto: UserTokenCreateInDsDto
    ) -> UserTokenCreateOutDsDto:

        user_token_ds = SqlalchemyUserTokenTranslator.create(
            ds_dto)
        self.session.add(user_token_ds)
        return UserTokenCreateOutDsDto.model_validate(user_token_ds)

    def delete(
        self,
        user_token_ds_dto: UserTokenDeleteInDsDto
    ):
        user_token_ds = self.session.query(
            UserTokenDataSource
        ).filter(
            UserTokenDataSource.user_id == user_token_ds_dto.user_id,
            UserTokenDataSource.created_at.__le__(
                user_token_ds_dto.date_before)
        ).delete()
