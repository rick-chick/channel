from abc import abstractmethod
from channel.usecase.models import DeviceCreateOutDto
from channel.adapter.presenter.renderer import Renderer


class DeviceCreateView(Renderer):

    @abstractmethod
    def add_result(self, device_create_out_dto: DeviceCreateOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
