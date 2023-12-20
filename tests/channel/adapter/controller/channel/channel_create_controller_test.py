from channel.adapter.controller.channel.channel_create_controller import (
    ChannelCreateController,
)
from tests.channel.adapter.controller.channel.channel_create_input_parser_impl import (
    ChannelCreateInputParserImpl,
)
from tests.channel.adapter.gateway.channel.channel_repository_impl import (
    ChannelRepositoryImpl,
)
from tests.channel.adapter.gateway.user.user_session_impl import UserSessionImpl
from tests.channel.adapter.presenter.channel.channel_create_view_impl import (
    ChannelCreateViewImpl,
)
from tests.channel.factories import ChannelCreateOutDsDtoFactory 


def test_success():

    repository = ChannelRepositoryImpl()
    repository.create_out = ChannelCreateOutDsDtoFactory.build()
    controller = ChannelCreateController(
            user_session= UserSessionImpl(),
            channel_repository= repository,
            channel_view= ChannelCreateViewImpl(),
            parser= ChannelCreateInputParserImpl(),
    )

    controller.handle(None)
