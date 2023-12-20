from channel.adapter.gateway.channel import ChannelCreateGateway
from tests.channel.adapter.gateway.channel.channel_repository_impl\
    import ChannelRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl\
    import UserSessionImpl

ChannelCreateGateway(
    channel_repository=ChannelRepositoryImpl(),
    user_session=UserSessionImpl(),
)
