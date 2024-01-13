from channel.usecase.interactor.user import UserSignupInteractor
from channel.usecase.models import (
    MailSendInDsDto,
    MailSendOutDsDto,
    SignupCreateInDsDto,
    SignupCreateOutDsDto,
    SignupDeleteInDsDto,
    SignupDeleteOutDsDto,
    UserSignupOutDto
)
from channel.usecase.output_port.user import UserSignupOututPort
from channel.usecase.repository.user import UserSignupRepository

from tests.channel.factories import (
    MailSendOutDsDtoFactory,
    SignupCreateOutDsDtoFactory,
    SignupDeleteOutDsDtoFactory,
    UserSignupInDtoFactory,
)

from typing import Optional

valid_user_in_dto = UserSignupInDtoFactory.build()
valid_send_mail_output = MailSendOutDsDtoFactory.build()
valid_signup_output = SignupCreateOutDsDtoFactory.build()
valid_signup_delete_ds_dto = SignupDeleteOutDsDtoFactory.build()


class UserSignupOututPortImpl(UserSignupOututPort):

    def __init__(self):
        self.exceptions = []
        self.user: Optional[UserSignupOutDto] = None

    def prepare_fail_view(self, exception: Exception):
        self.exceptions.append(exception)

    def prepare_success_view(self, user: UserSignupOutDto):
        self.user = user
        return user


class UserSignupRepositoryImpl(UserSignupRepository):

    signup_output: SignupCreateOutDsDto = valid_signup_output
    send_mail_output: MailSendOutDsDto = valid_send_mail_output
    delete_signup_output: SignupDeleteOutDsDto = valid_signup_delete_ds_dto
    send_mail_exception: Optional[Exception] = None
    exists_user_by_email_output: bool = False

    password_reset_url_output: str = 'http://sample.url'

    def create_signup(
        self,
        signup_dto: SignupCreateInDsDto
    ) -> SignupCreateOutDsDto:
        self.signup_input = signup_dto
        return self.signup_output

    def send_mail(
        self,
        mail_dto: MailSendInDsDto
    ):
        self.send_mail_input = mail_dto
        return self.send_mail_output

    def exists_user_by_email(
        self,
        email: str
    ) -> bool:
        self.exists_user_by_email_input = email
        return self.exists_user_by_email_output

    def password_reset_url(
        self,
        token: str
    ) -> str:
        self.password_reset_url_input = token
        return self.password_reset_url_output

    def delete_signup(
        self,
        signup_dto: SignupDeleteInDsDto
    ) -> SignupDeleteOutDsDto:
        self.delete_signup_input = signup_dto
        return self.delete_signup_output


def create_interactor(
        gateway=UserSignupRepositoryImpl(),
        presenter=UserSignupOututPortImpl()) -> UserSignupInteractor:
    return UserSignupInteractor(gateway, presenter)


def test_signup_success():

    presenter = UserSignupOututPortImpl()
    gateway = UserSignupRepositoryImpl()

    target = create_interactor(gateway, presenter)

    target.signup(valid_user_in_dto)

    assert presenter.user is not None
