from abc import abstractmethod
from channel.usecase.models import ChannelUpdateOutDto
from channel.adapter.presenter.renderer import Renderer


class ChannelUpdateView(Renderer):

    @abstractmethod
    def add_result(self, channel_update_out_dto: ChannelUpdateOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
