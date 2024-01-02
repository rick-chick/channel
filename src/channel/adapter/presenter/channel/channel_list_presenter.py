from channel.usecase.output_port.channel import ChannelListOututPort
from channel.usecase.models import ChannelListOutDto
from channel.adapter.presenter.channel.channel_list_view import ChannelListView


class ChannelListPresenter(ChannelListOututPort):

    def __init__(
        self,
        channel_list_view: ChannelListView
    ):
        self.channel_list_view = channel_list_view

    def prepare_success_view(
        self,
        channel: ChannelListOutDto
    ):
        self.channel_list_view.add_result(channel)
        return channel

    def prepare_fail_view(self, exception: Exception):
        self.channel_list_view.add_exception(exception)
