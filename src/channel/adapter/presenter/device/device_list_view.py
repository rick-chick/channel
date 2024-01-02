from abc import abstractmethod
from channel.usecase.models import DeviceListOutDto
from channel.adapter.presenter.renderer import Renderer


class DeviceListView(Renderer):

    @abstractmethod
    def add_result(self, device_list_out_dto: DeviceListOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
