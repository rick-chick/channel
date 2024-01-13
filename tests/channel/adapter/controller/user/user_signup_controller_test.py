from channel.adapter.controller.user.user_signup_controller import UserSignupController
from tests.channel.adapter.controller.user.user_signup_input_parser_impl import UserSignupInputParserImpl
from tests.channel.adapter.gateway.mail.mail_service_impl import MailServiceImpl
from tests.channel.adapter.gateway.signup.signup_repository_impl import SignupRepositoryImpl
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl
from tests.channel.adapter.presenter.user.user_signup_view_impl import UserSignupViewImpl
from tests.channel.factories import UserSignupInDtoFactory


def test_success():
    target = UserSignupController(
        mail_service=MailServiceImpl(),
        signup_repository=SignupRepositoryImpl(),
        user_repository=UserRepositoryImpl(),
        user_signup_view=UserSignupViewImpl(),
        user_signup_input_parser=UserSignupInputParserImpl(),
        password_reset_url='http://test.com'
    )
    target.handle(UserSignupInDtoFactory.build())
