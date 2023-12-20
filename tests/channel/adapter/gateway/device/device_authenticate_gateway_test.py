from channel.adapter.gateway.device import DeviceAuthenticateGateway
from tests.channel.adapter.gateway.device.device_repository_impl import (
    DeviceRepositoryImpl,
)
from tests.channel.adapter.gateway.device.device_session_impl import DeviceSessionImpl


def test_success():
    DeviceAuthenticateGateway(
        device_repository=DeviceRepositoryImpl(),
        device_session=DeviceSessionImpl()
    )
