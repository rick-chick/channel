from abc import abstractmethod
from channel.usecase.models import DeviceDeleteOutDto
from channel.adapter.presenter.renderer import Renderer


class DeviceDeleteView(Renderer):

    @abstractmethod
    def add_result(self, device_delete_out_dto: DeviceDeleteOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
