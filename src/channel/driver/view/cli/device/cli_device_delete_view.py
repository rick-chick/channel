from typing import Any
from channel.adapter.presenter.device.device_delete_view import DeviceDeleteView
from channel.usecase.models import DeviceDeleteOutDto


class CliDeviceDeleteView(DeviceDeleteView):

    def __init__(self):
        self.exceptions = []
        self.device: Any = None

    def add_result(self, device_delete_out_dto: DeviceDeleteOutDto):
        self.device = device_delete_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.device)
