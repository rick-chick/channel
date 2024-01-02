from channel.adapter.controller.channel.channel_list_controller import ChannelListController
from tests.channel.adapter.controller.channel.channel_list_input_parser_impl import ChannelListInputParserImpl
from tests.channel.adapter.gateway.device.device_repository_impl import DeviceRepositoryImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.channel.channel_repository_impl import ChannelRepositoryImpl
from tests.channel.adapter.presenter.channel.channel_list_view_impl import ChannelListViewImpl
from tests.channel.factories import ChannelListInDtoFactory


def test_success():
    target = ChannelListController(
        channel_list_input_parser=ChannelListInputParserImpl(),
        device_repository=DeviceRepositoryImpl(),
        user_session=UserSessionImpl(),
        channel_repository=ChannelRepositoryImpl(),
        channel_list_view=ChannelListViewImpl()
    )
    target.handle(ChannelListInDtoFactory.build())
