from channel.usecase.output_port.device import DeviceListOututPort
from channel.usecase.models import DeviceListOutDto
from channel.adapter.presenter.device.device_list_view import DeviceListView


class DeviceListPresenter(DeviceListOututPort):

    def __init__(
        self,
        device_list_view: DeviceListView
    ):
        self.device_list_view = device_list_view

    def prepare_success_view(
        self,
        device: DeviceListOutDto
    ):
        self.device_list_view.add_result(device)
        return device

    def prepare_fail_view(self, exception: Exception):
        self.device_list_view.add_exception(exception)
