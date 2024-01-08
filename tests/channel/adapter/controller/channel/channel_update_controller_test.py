from channel.adapter.controller.channel.channel_update_controller import ChannelUpdateController
from tests.channel.adapter.controller.channel.channel_update_input_parser_impl import ChannelUpdateInputParserImpl
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.gateway.channel.channel_repository_impl import ChannelRepositoryImpl
from tests.channel.adapter.presenter.channel.channel_update_view_impl import ChannelUpdateViewImpl
from tests.channel.factories import ChannelUpdateInDtoFactory


def test_success():
    target = ChannelUpdateController(
        user_session=UserSessionImpl(),
        channel_repository=ChannelRepositoryImpl(),
        channel_update_view=ChannelUpdateViewImpl(),
        channel_update_input_parser=ChannelUpdateInputParserImpl(),
    )
    target.handle(ChannelUpdateInDtoFactory.build())
