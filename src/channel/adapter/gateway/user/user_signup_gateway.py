from channel.adapter.gateway.mail.mail_service import MailService
from channel.adapter.gateway.signup.signup_repository import SignupRepository
from channel.adapter.gateway.user.user_repository import UserRepository

from channel.usecase.models import (
    MailSendInDsDto,
    MailSendOutDsDto,
    SignupCreateInDsDto,
    SignupCreateOutDsDto,
    SignupDeleteInDsDto,
    SignupDeleteOutDsDto,
)
from channel.usecase.repository.user import UserSignupRepository


class UserSignupGateway(UserSignupRepository):

    def __init__(
        self,
        signup_repository: SignupRepository,
        mail_service: MailService,
        user_repository: UserRepository,
        password_reset_url: str
    ):
        self.signup_repository = signup_repository
        self.mail_service = mail_service
        self.user_repository = user_repository
        self.url = password_reset_url

    def create_signup(
        self,
        signup_dto: SignupCreateInDsDto
    ) -> SignupCreateOutDsDto:
        return self.signup_repository.create(signup_dto)

    def delete_signup(
        self,
        signup_dto: SignupDeleteInDsDto
    ) -> SignupDeleteOutDsDto:
        return self.signup_repository.delete(signup_dto)

    def send_mail(
        self,
        mail_dto: MailSendInDsDto
    ) -> MailSendOutDsDto:
        return self.mail_service.send(mail_dto)

    def exists_user_by_email(
        self,
        email: str
    ) -> bool:
        return self.user_repository.exists_by_email(email)

    def password_reset_url(
        self,
        token: str
    ) -> str:
        return f"{self.url}?token={token}"
