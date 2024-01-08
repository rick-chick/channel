from channel.adapter.controller.channel.channel_delete_controller import ChannelDeleteController
from tests.channel.adapter.controller.channel.channel_delete_input_parser_impl import ChannelDeleteInputParserImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.channel.channel_repository_impl import ChannelRepositoryImpl
from tests.channel.adapter.presenter.channel.channel_delete_view_impl import ChannelDeleteViewImpl
from tests.channel.factories import ChannelDeleteInDtoFactory


def test_success():
    target = ChannelDeleteController(
        user_session=UserSessionImpl(),
        channel_repository=ChannelRepositoryImpl(),
        channel_delete_view=ChannelDeleteViewImpl(),
        channel_delete_input_parser=ChannelDeleteInputParserImpl(),
    )
    target.handle(ChannelDeleteInDtoFactory.build())
