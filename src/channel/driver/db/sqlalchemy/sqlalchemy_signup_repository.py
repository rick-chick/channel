from operator import and_
from channel.driver.db.sqlalchemy.models import SignupDataSource
from .sqlalchemy_translator import SqlalchemySignupTranslator

from channel.adapter.gateway.user import SignupRepository

from channel.usecase.models import (
    SignupCreateInDsDto,
    SignupCreateOutDsDto,
    SignupDeleteInDsDto,
    SignupDeleteOutDsDto,
)

from sqlalchemy.orm import Session


class SqlalchemySignupRepository(SignupRepository):

    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        signup_dto: SignupCreateInDsDto
    ) -> SignupCreateOutDsDto:
        user_ds = SqlalchemySignupTranslator.create(signup_dto)
        self.session.add(user_ds)
        self.session.flush()
        return SignupCreateOutDsDto.model_validate(user_ds)

    def delete(
        self,
        signup_dto: SignupDeleteInDsDto
    ) -> SignupDeleteOutDsDto:

        filters = []

        if signup_dto.email:
            filters.append(
                SignupDataSource.email == signup_dto.email
            )

        if len(filters) == 0:
            return SignupDeleteOutDsDto(
                emails=[]
            )

        if len(filters) == 1:
            filters.append(1 == 1)

        delete_signups = self.session.query(
            SignupDataSource
        ).filter(
            and_(*filters)
        ).all()

        emails = []
        for ds in delete_signups:
            emails.append(ds.email)
            self.session.delete(ds)

        self.session.commit()
        return SignupDeleteOutDsDto(
            emails=emails
        )
