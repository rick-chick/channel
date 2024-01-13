from datetime import datetime
from channel.adapter.controller.user.user_reset_password_controller import UserResetPasswordController
from tests.channel.adapter.controller.user.user_reset_password_input_parser_impl import UserResetPasswordInputParserImpl
from tests.channel.adapter.gateway.signup.signup_repository_impl import SignupRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl
from tests.channel.adapter.presenter.user.user_reset_password_view_impl import UserResetPasswordViewImpl
from tests.channel.factories import (
    SignupGetOutDsDtoFactory,
    UserResetPasswordInDtoFactory
)


def test_success():
    target = UserResetPasswordController(
        user_repository=UserRepositoryImpl(),
        signup_repository=SignupRepositoryImpl(),
        user_reset_password_view=UserResetPasswordViewImpl(),
        user_reset_password_input_parser=UserResetPasswordInputParserImpl(),
    )
    target.handle(UserResetPasswordInDtoFactory.build())
