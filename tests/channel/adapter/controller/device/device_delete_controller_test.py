from channel.adapter.controller.device.device_delete_controller import DeviceDeleteController
from tests.channel.adapter.controller.device.device_delete_input_parser_impl import DeviceDeleteInputParserImpl
from tests.channel.adapter.gateway.channel.channel_repository_impl import ChannelRepositoryImpl
from tests.channel.adapter.gateway.record.record_repository_impl import RecordRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.device.device_repository_impl import DeviceRepositoryImpl
from tests.channel.adapter.presenter.device.device_delete_view_impl import DeviceDeleteViewImpl
from tests.channel.factories import DeviceDeleteInDtoFactory


def test_success():
    target = DeviceDeleteController(
        device_delete_input_parser=DeviceDeleteInputParserImpl(),
        user_session=UserSessionImpl(),
        device_repository=DeviceRepositoryImpl(),
        channel_repository=ChannelRepositoryImpl(),
        record_repository=RecordRepositoryImpl(),
        device_delete_view=DeviceDeleteViewImpl(),
    )
    target.handle(DeviceDeleteInDtoFactory.build())
