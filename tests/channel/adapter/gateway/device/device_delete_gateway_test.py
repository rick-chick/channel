from channel.adapter.gateway.device import DeviceDeleteGateway
from tests.channel.adapter.gateway.channel.channel_repository_impl import ChannelRepositoryImpl

from tests.channel.adapter.gateway.device.device_repository_impl\
    import DeviceRepositoryImpl
from tests.channel.adapter.gateway.record.record_repository_impl import RecordRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl\
    import UserSessionImpl


def test_success():
    DeviceDeleteGateway(
        device_repository=DeviceRepositoryImpl(),
        channel_repository=ChannelRepositoryImpl(),
        record_repository=RecordRepositoryImpl(),
        user_session=UserSessionImpl(),
    )
