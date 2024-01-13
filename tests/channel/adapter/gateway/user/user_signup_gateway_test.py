
from channel.adapter.gateway.user import UserSignupGateway
from tests.channel.adapter.gateway.mail.mail_service_impl import MailServiceImpl
from tests.channel.adapter.gateway.signup.signup_repository_impl import SignupRepositoryImpl
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl


def test_success():
    UserSignupGateway(
        mail_service=MailServiceImpl(),
        signup_repository=SignupRepositoryImpl(),
        user_repository=UserRepositoryImpl(),
        password_reset_url='http://reset.password.com',
    )
