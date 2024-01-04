from channel.usecase.output_port.device import DeviceDeleteOututPort
from channel.usecase.models import DeviceDeleteOutDto
from channel.adapter.presenter.device.device_delete_view import DeviceDeleteView


class DeviceDeletePresenter(DeviceDeleteOututPort):

    def __init__(
        self,
        device_delete_view: DeviceDeleteView
    ):
        self.device_delete_view = device_delete_view

    def prepare_success_view(
        self, device_dto: DeviceDeleteOutDto
    ):
        self.device_delete_view.add_result(device_dto)
        return device_dto

    def prepare_fail_view(self, exception: Exception):
        self.device_delete_view.add_exception(exception)
