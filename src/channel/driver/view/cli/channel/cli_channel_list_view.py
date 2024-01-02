from typing import Any
from channel.adapter.presenter.channel.channel_list_view import ChannelListView
from channel.usecase.models import ChannelListOutDto


class CliChannelListView(ChannelListView):

    def __init__(self):
        self.exceptions = []
        self.channel: Any = None

    def add_result(self, channel_list_out_dto: ChannelListOutDto):
        self.channel = channel_list_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.channel)
