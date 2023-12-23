from abc import abstractmethod
from channel.usecase.models import RecordListOutDto
from channel.adapter.presenter.renderer import Renderer


class RecordListView(Renderer):

    @abstractmethod
    def add_result(self, record_list_out_dto: RecordListOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
