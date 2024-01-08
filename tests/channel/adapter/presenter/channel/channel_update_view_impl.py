from channel.adapter.presenter.channel.channel_update_view import (
    ChannelUpdateView
)

from channel.usecase.models import ChannelUpdateOutDto
from typing import List


class ChannelUpdateViewImpl(ChannelUpdateView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, channel_update_out_dto: ChannelUpdateOutDto):
        self.channel_update_out_dto = channel_update_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.channel_update_out_dto)
