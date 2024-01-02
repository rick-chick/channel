from abc import abstractmethod
from channel.usecase.models import ChannelListOutDto
from channel.adapter.presenter.renderer import Renderer


class ChannelListView(Renderer):

    @abstractmethod
    def add_result(self, channel_list_out_dto: ChannelListOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
