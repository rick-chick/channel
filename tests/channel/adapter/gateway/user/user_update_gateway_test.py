from channel.adapter.gateway.user.user_update_gateway import UserUpdateGateway
from tests.channel.adapter.gateway.user.user_repository_impl\
    import UserRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl\
    import UserSessionImpl

UserUpdateGateway(
    user_repository=UserRepositoryImpl(),
    user_session=UserSessionImpl(),
)
