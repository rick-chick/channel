from channel.adapter.gateway.record import RecordCreateGateway
from tests.channel.adapter.gateway.device.device_session_impl import DeviceSessionImpl
from tests.channel.adapter.gateway.record.record_repository_impl\
    import RecordRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl\
    import UserSessionImpl
from tests.channel.factories import DeviceSessionDsDtoFactory


def test_success():
    device_session = DeviceSessionImpl()
    device_session.load_out = DeviceSessionDsDtoFactory.build()
    gateway = RecordCreateGateway(
        record_repository=RecordRepositoryImpl(),
        device_session=device_session,
        user_session=UserSessionImpl(),
    )
    gateway.load_session_device()
