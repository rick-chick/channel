from channel.adapter.controller.device.device_list_controller import DeviceListController
from tests.channel.adapter.controller.device.device_list_input_parser_impl import DeviceListInputParserImpl
from tests.channel.adapter.gateway.channel.channel_repository_impl import ChannelRepositoryImpl
from tests.channel.adapter.gateway.record.record_repository_impl import RecordRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.device.device_repository_impl import DeviceRepositoryImpl
from tests.channel.adapter.presenter.device.device_list_view_impl import DeviceListViewImpl
from tests.channel.factories import DeviceListInDtoFactory


def test_success():
    target = DeviceListController(
        device_list_input_parser=DeviceListInputParserImpl(),
        channel_repository=ChannelRepositoryImpl(),
        record_repository=RecordRepositoryImpl(),
        user_session=UserSessionImpl(),
        device_repository=DeviceRepositoryImpl(),
        device_list_view=DeviceListViewImpl()
    )
    target.handle(DeviceListInDtoFactory.build())
