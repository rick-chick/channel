from typing import Any
from channel.adapter.presenter.channel.channel_delete_view import ChannelDeleteView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import ChannelDeleteOutDto


class FlaskChannelDeleteView(ChannelDeleteView):

    def __init__(self):
        self.exceptions = []
        self.channel: Any = None

    def add_result(self, channel_delete_out_dto: ChannelDeleteOutDto):
        self.channel = channel_delete_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.channel, self.exceptions).json()
