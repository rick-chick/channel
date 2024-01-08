from channel.usecase.output_port.channel import ChannelUpdateOututPort
from channel.usecase.models import ChannelUpdateOutDto
from channel.adapter.presenter.channel.channel_update_view import ChannelUpdateView


class ChannelUpdatePresenter(ChannelUpdateOututPort):

    def __init__(
        self,
        channel_update_view: ChannelUpdateView
    ):
        self.channel_update_view = channel_update_view

    def prepare_success_view(
        self, channel: ChannelUpdateOutDto
    ) -> ChannelUpdateOutDto:
        self.channel_update_view.add_result(channel)
        return channel

    def prepare_fail_view(
        self,
        exception: Exception
    ):
        self.channel_update_view.add_exception(exception)
