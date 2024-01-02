from channel.adapter.gateway.channel import ChannelListGateway
from tests.channel.adapter.gateway.channel.channel_repository_impl\
    import ChannelRepositoryImpl
from tests.channel.adapter.gateway.device.device_repository_impl import DeviceRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl\
    import UserSessionImpl


def test_success():
    ChannelListGateway(
        channel_repository=ChannelRepositoryImpl(),
        device_repository=DeviceRepositoryImpl(),
        user_session=UserSessionImpl(),
    )
