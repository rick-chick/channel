from channel.adapter.presenter.channel.channel_update_view import ChannelUpdateView
from channel.usecase.models import ChannelUpdateOutDto


class CliChannelUpdateView(ChannelUpdateView):

    def __init__(self):
        self.exceptions = []

    def add_result(self, channel_update_out_dto: ChannelUpdateOutDto):
        self.channel = channel_update_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.channel)
