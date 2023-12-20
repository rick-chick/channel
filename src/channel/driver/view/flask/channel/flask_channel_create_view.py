from typing import Any
from channel.adapter.presenter.channel.channel_create_view import ChannelCreateView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import ChannelCreateOutDto


class FlaskChannelCreateView(ChannelCreateView):

    def __init__(self):
        self.exceptions = []
        self.channel: Any = None

    def add_result(self, channel_create_out_dto: ChannelCreateOutDto):
        self.channel = channel_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.channel, self.exceptions).json()
