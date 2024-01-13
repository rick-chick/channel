from typing import Optional

from channel.adapter.gateway.signup.signup_repository import SignupRepository
from channel.usecase.models import (
    SignupCreateInDsDto,
    SignupCreateOutDsDto,
    SignupDeleteInDsDto,
    SignupDeleteOutDsDto,
)
from tests.channel.factories import (
    SignupCreateOutDsDtoFactory,
    SignupDeleteOutDsDtoFactory
)


class SignupRepositoryImpl(SignupRepository):

    create_in: Optional[SignupCreateInDsDto] = None

    def create(
        self,
        signup_dto: SignupCreateInDsDto
    ) -> SignupCreateOutDsDto:
        self.create_in = signup_dto
        return SignupCreateOutDsDtoFactory.build()

    def delete(
        self,
        signup_dto: SignupDeleteInDsDto
    ) -> SignupDeleteOutDsDto:
        self.delete_in = signup_dto
        return SignupDeleteOutDsDtoFactory.build()
