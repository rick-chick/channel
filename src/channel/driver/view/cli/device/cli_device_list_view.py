from typing import Any
from channel.adapter.presenter.device.device_list_view import DeviceListView
from channel.usecase.models import DeviceListOutDto


class CliDeviceListView(DeviceListView):

    def __init__(self):
        self.exceptions = []
        self.device: Any = None

    def add_result(self, device_list_out_dto: DeviceListOutDto):
        self.device = device_list_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.device)
