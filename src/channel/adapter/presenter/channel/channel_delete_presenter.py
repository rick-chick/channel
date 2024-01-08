from channel.usecase.output_port.channel import ChannelDeleteOututPort
from channel.usecase.models import ChannelDeleteOutDto
from channel.adapter.presenter.channel.channel_delete_view import ChannelDeleteView


class ChannelDeletePresenter(ChannelDeleteOututPort):

    def __init__(
        self,
        channel_delete_view: ChannelDeleteView
    ):
        self.channel_delete_view = channel_delete_view

    def prepare_success_view(
        self, channel_dto: ChannelDeleteOutDto
    ):
        self.channel_delete_view.add_result(channel_dto)
        return channel_dto

    def prepare_fail_view(self, exception: Exception):
        self.channel_delete_view.add_exception(exception)
