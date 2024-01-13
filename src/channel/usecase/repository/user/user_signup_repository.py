from abc import ABC, abstractmethod
from channel.usecase.models import (
    MailSendInDsDto,
    MailSendOutDsDto,
    SignupCreateInDsDto,
    SignupCreateOutDsDto,
    SignupDeleteInDsDto,
    SignupDeleteOutDsDto,
)


class UserSignupRepository(ABC):

    @abstractmethod
    def create_signup(
        self,
        signup_dto: SignupCreateInDsDto
    ) -> SignupCreateOutDsDto:
        pass

    @abstractmethod
    def delete_signup(
        self,
        signup_dto: SignupDeleteInDsDto
    ) -> SignupDeleteOutDsDto:
        pass

    @abstractmethod
    def send_mail(
        self,
        mail_dto: MailSendInDsDto
    ) -> MailSendOutDsDto:
        pass

    @abstractmethod
    def exists_user_by_email(
        self,
        email: str
    ) -> bool:
        pass

    @abstractmethod
    def password_reset_url(
        self,
        token: str
    ) -> str:
        pass
