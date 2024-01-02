from channel.adapter.presenter.channel.channel_list_view import (
    ChannelListView
)

from channel.usecase.models import ChannelListOutDto
from typing import List


class ChannelListViewImpl(ChannelListView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, channel_list_out_dto: ChannelListOutDto):
        self.channel_list_out_dto = channel_list_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.channel_list_out_dto)
