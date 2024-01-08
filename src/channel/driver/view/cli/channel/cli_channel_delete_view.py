from typing import Any
from channel.adapter.presenter.channel.channel_delete_view import ChannelDeleteView
from channel.usecase.models import ChannelDeleteOutDto


class CliChannelDeleteView(ChannelDeleteView):

    def __init__(self):
        self.exceptions = []
        self.channel: Any = None

    def add_result(self, channel_delete_out_dto: ChannelDeleteOutDto):
        self.channel = channel_delete_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.channel)
