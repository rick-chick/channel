from .models import UserDataSource
from .sqlalchemy_translator import SqlalchemyUserTranslator

from channel.adapter.gateway.user import UserRepository

from channel.usecase.models import (
    UserCreateInDsDto,
    UserCreateOutDsDto,
    UserUpdateInDsDto,
    UserUpdateOutDsDto,
    UserOutDsDto,
    UserListInDsDto,
    UserListOutDsDto,
    UserDeleteInDsDto,
    UserDeleteOutDsDto
)

from typing import Optional, List
from sqlalchemy.orm import Session


class SqlalchemyUserRepository(UserRepository):

    def __init__(self, session: Session):
        self.session = session

    def find_by_id(self, id: str) -> Optional[UserOutDsDto]:
        user_ds = self.session.query(UserDataSource)\
            .filter_by(id=id)\
            .first()

        if user_ds:
            return UserOutDsDto.model_validate(user_ds)
        return None

    def find_by_email(self, email: str) -> Optional[UserOutDsDto]:
        user_ds = self.session.query(UserDataSource)\
            .filter_by(email=email)\
            .first()

        if user_ds:
            return UserOutDsDto.model_validate(user_ds)
        return None

    def exists_by_id(self, id: int) -> bool:
        return self.session.query(
            self.session.query(UserDataSource)
            .filter_by(id=id).exists()
        ).scalar()

    def exists_by_email(self, email: str) -> bool:
        return self.session.query(
            self.session.query(UserDataSource)
            .filter_by(email=email).exists()
        ).scalar()

    def list(
        self,
        user_ds_dto: UserListInDsDto
    ) -> List[UserListOutDsDto]:
        user_ds = self.session.query(UserDataSource).all()
        if not user_ds:
            return []

        return [
            UserListOutDsDto.model_validate(ds)
            for ds in user_ds
        ]

    def create(
        self,
        ds_dto: UserCreateInDsDto
    ) -> UserCreateOutDsDto:
        user_ds = SqlalchemyUserTranslator.create(ds_dto)
        self.session.add(user_ds)
        self.session.commit()
        return UserCreateOutDsDto.model_validate(user_ds)

    def update(
        self,
        ds_dto: UserUpdateInDsDto
    ) -> Optional[UserUpdateOutDsDto]:
        user_ds = self.session.query(UserDataSource).filter_by(
            id=ds_dto.id).first()
        if not user_ds:
            return None
        user_ds = SqlalchemyUserTranslator.update(ds_dto, user_ds)
        self.session.commit()
        return UserUpdateOutDsDto.model_validate(user_ds)

    def delete(
        self,
        user_ds_dto: UserDeleteInDsDto
    ) -> List[UserDeleteOutDsDto]:
        if user_ds_dto.ids is None:
            return []

        user_ds = self.session.query(UserDataSource).filter(
            UserDataSource.id.in_(user_ds_dto.ids)).all()
        if not user_ds:
            return []

        ret = []
        for ds in user_ds:
            ret.append(UserDeleteOutDsDto.model_validate(ds))
            self.session.delete(ds)

        self.session.commit()
        return ret
