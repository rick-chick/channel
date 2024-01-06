from channel.adapter.controller.user_token.user_token_refresh_controller import UserTokenRefreshController
from channel.usecase.exception import UnauthenticateException
from tests.channel.adapter.controller.user_token.user_token_refresh_input_parser_impl import UserTokenRefreshInputParserImpl
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl
from tests.channel.adapter.gateway.user_token.user_token_repository_impl import UserTokenRepositoryImpl
from tests.channel.adapter.presenter.user_token.user_token_refresh_view_impl import UserTokenRefreshViewImpl
from tests.channel.factories import UserTokenRefreshInDtoFactory
import pytest


def test_success():
    target = UserTokenRefreshController(
        user_repository=UserRepositoryImpl(),
        user_token_repository=UserTokenRepositoryImpl(),
        user_token_refresh_view=UserTokenRefreshViewImpl(),
        user_token_refresh_input_parser=UserTokenRefreshInputParserImpl(),
    )
    with pytest.raises(UnauthenticateException):
        target.handle(UserTokenRefreshInDtoFactory.build())
