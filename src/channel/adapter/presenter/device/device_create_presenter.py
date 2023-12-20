from channel.usecase.output_port.device import DeviceCreateOututPort
from channel.adapter.presenter.device.device_create_view import DeviceCreateView
from channel.usecase.models import DeviceCreateOutDto


class DeviceCreatePresenter(DeviceCreateOututPort):

    def __init__(
        self,
        device_create_view: DeviceCreateView
    ):
        self.view = device_create_view

    def prepare_success_view(self, device: DeviceCreateOutDto) -> DeviceCreateOutDto:
        self.view.add_result(device)
        return device

    def prepare_fail_view(self, exception: Exception):
        self.view.add_exception(exception)
