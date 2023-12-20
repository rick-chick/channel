from abc import abstractmethod
from channel.usecase.models import DeviceAuthenticateOutDto
from channel.adapter.presenter.renderer import Renderer


class DeviceAuthenticateView(Renderer):

    @abstractmethod
    def add_result(self, device_authenticate_out_dto: DeviceAuthenticateOutDto):
        pass

    @abstractmethod
    def add_exception(self, exception: Exception):
        pass

    @abstractmethod
    def render(self):
        pass
