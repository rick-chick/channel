from typing import Optional
from channel.usecase.models import (
    SignupCreateInDsDto,
    SignupCreateOutDsDto,
    SignupDeleteInDsDto,
    SignupDeleteOutDsDto,
    SignupGetOutDsDto,
)

from abc import ABC, abstractmethod


class SignupRepository(ABC):

    @abstractmethod
    def create(
        self,
        signup_dto: SignupCreateInDsDto
    ) -> SignupCreateOutDsDto:
        pass

    @abstractmethod
    def delete(
        self,
        signup_dto: SignupDeleteInDsDto
    ) -> SignupDeleteOutDsDto:
        pass

    @abstractmethod
    def find_by_token(
        self,
        token: str
    ) -> Optional[SignupGetOutDsDto]:
        pass
