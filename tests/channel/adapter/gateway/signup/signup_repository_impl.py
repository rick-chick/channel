from typing import Optional

from channel.adapter.gateway.signup.signup_repository import SignupRepository
from channel.usecase.models import (
    SignupCreateInDsDto,
    SignupCreateOutDsDto,
    SignupDeleteInDsDto,
    SignupDeleteOutDsDto,
    SignupGetOutDsDto,
)
from tests.channel.factories import (
    SignupCreateOutDsDtoFactory,
    SignupDeleteOutDsDtoFactory,
    SignupGetOutDsDtoFactory
)


class SignupRepositoryImpl(SignupRepository):

    create_in: Optional[SignupCreateInDsDto] = None
    find_by_token_out = SignupGetOutDsDtoFactory.build()

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

    def find_by_token(
        self,
        token: str
    ) -> Optional[SignupGetOutDsDto]:
        self.find_by_token_in = token
        return self.find_by_token_out
