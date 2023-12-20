
from channel.adapter.gateway.user_token import UserTokenAuthenticateGateway
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.user.user_repository_impl import UserRepositoryImpl


def test_success():
    UserTokenAuthenticateGateway(
        user_session=UserSessionImpl(),
        user_repository=UserRepositoryImpl()
    )
