from channel.adapter.presenter.channel.channel_create_view import (
    ChannelCreateView
)

from channel.usecase.models import ChannelCreateOutDto
from typing import List


class ChannelCreateViewImpl(ChannelCreateView):
    channel_create_out_dto: ChannelCreateOutDto

    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(
        self,channel_craete_out_dto: ChannelCreateOutDto
    ):
        self.channel_create_out_dto = channel_craete_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.channel_create_out_dto)
