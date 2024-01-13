from channel.adapter.controller.user.user_create_controller import UserCreateController
from channel.adapter.gateway.user import UserResetPasswordGateway
from tests.channel.adapter.controller.user.user_create_input_parser_impl import UserCreateInputParserImpl
from tests.channel.adapter.gateway.signup.signup_repository_impl import SignupRepositoryImpl
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.presenter.user.user_create_view_impl import UserCreateViewImpl
from tests.channel.adapter.controller.user.user_create_controller_impl import user_create_controller_impl
from tests.channel.adapter.controller.user.user_update_controller_impl import user_update_controller_impl


def test_success():
    UserResetPasswordGateway(
        user_repository=UserRepositoryImpl(),
        signup_repository=SignupRepositoryImpl(),
    )
