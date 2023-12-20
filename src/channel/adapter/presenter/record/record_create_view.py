from abc import abstractmethod
from channel.usecase.models import RecordCreateOutDto
from channel.adapter.presenter.renderer import Renderer
from typing import Optional


class RecordCreateView(Renderer):

    @abstractmethod
    def add_result(self, record_create_out_dto: RecordCreateOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
