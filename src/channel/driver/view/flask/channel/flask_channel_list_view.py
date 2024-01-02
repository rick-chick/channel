from typing import Any
from channel.adapter.presenter.channel.channel_list_view import ChannelListView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import ChannelListOutDto


class FlaskChannelListView(ChannelListView):

    def __init__(self):
        self.exceptions = []
        self.channel: Any = None

    def add_result(self, channel_list_out_dto: ChannelListOutDto):
        self.channel = channel_list_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.channel, self.exceptions).json()
