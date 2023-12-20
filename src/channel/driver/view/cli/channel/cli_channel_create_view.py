from channel.adapter.presenter.channel.channel_create_view import ChannelCreateView
from channel.usecase.models import ChannelCreateOutDto


class CliChannelCreateView(ChannelCreateView):

    def __init__(self):
        self.exceptions = []

    def add_result(self, channel_create_out_dto: ChannelCreateOutDto):
        self.channel = channel_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.channel)
