from channel.adapter.gateway.device import DeviceCreateGateway
from tests.channel.adapter.gateway.device.device_repository_impl\
    import DeviceRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl\
    import UserSessionImpl

DeviceCreateGateway(
    device_repository=DeviceRepositoryImpl(),
    user_session=UserSessionImpl(),
)
