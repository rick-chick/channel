
from channel.adapter.gateway.user_token import UserTokenRefreshGateway
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl
from tests.channel.adapter.gateway.user_token.user_token_repository_impl import UserTokenRepositoryImpl


def test_success():
    UserTokenRefreshGateway(
        user_token_repository=UserTokenRepositoryImpl(),
        user_repository=UserRepositoryImpl(),
    )
