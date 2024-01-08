from abc import abstractmethod
from channel.usecase.models import ChannelDeleteOutDto
from channel.adapter.presenter.renderer import Renderer


class ChannelDeleteView(Renderer):

    @abstractmethod
    def add_result(self, channel_delete_out_dto: ChannelDeleteOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
