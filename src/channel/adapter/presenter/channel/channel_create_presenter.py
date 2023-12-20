from channel.usecase.output_port.channel import ChannelCreateOututPort
from channel.usecase.models import ChannelCreateOutDto
from channel.adapter.presenter.channel.channel_create_view import ChannelCreateView


class ChannelCreatePresenter(ChannelCreateOututPort):

    def __init__(
        self,
        channe_create_view :ChannelCreateView
    ):
        self.channe_create_view = channe_create_view

    def prepare_success_view(
        self,
        channel: ChannelCreateOutDto
    ) -> ChannelCreateOutDto:
        self.channe_create_view.add_result(channel)
        return channel

    def prepare_fail_view(self, exception: Exception):
        self.channe_create_view.add_exception(exception)
