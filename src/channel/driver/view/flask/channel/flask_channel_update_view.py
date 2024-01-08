from typing import Any
from channel.adapter.presenter.channel.channel_update_view import ChannelUpdateView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import ChannelUpdateOutDto


class FlaskChannelUpdateView(ChannelUpdateView):

    def __init__(self):
        self.exceptions = []
        self.channel: Any = None

    def add_result(self, channel_update_out_dto: ChannelUpdateOutDto):
        self.channel = channel_update_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.channel, self.exceptions).json()
