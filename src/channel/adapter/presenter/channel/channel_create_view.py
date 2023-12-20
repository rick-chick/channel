from abc import abstractmethod
from channel.usecase.models import ChannelCreateOutDto
from channel.adapter.presenter.renderer import Renderer


class ChannelCreateView(Renderer):

    @abstractmethod
    def add_result(self, channel_create_out_dto: ChannelCreateOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
