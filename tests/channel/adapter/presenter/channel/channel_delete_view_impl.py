from channel.adapter.presenter.channel.channel_delete_view import (
    ChannelDeleteView
)

from channel.usecase.models import ChannelDeleteOutDto
from typing import List


class ChannelDeleteViewImpl(ChannelDeleteView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, channel_delete_out_dto: ChannelDeleteOutDto):
        self.channel_delete_out_dto = channel_delete_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.channel_delete_out_dto)
