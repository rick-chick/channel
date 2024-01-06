from channel.adapter.gateway.user import UserAuthenticateGateway
from tests.channel.adapter.gateway.user_token.user_token_repository_impl import UserTokenRepositoryImpl
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl


def test_success():
    UserAuthenticateGateway(
        user_repository=UserRepositoryImpl(),
        user_session=UserSessionImpl()
    )
