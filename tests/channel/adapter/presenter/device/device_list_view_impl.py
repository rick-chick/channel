from channel.adapter.presenter.device.device_list_view import (
    DeviceListView
)

from channel.usecase.models import DeviceListOutDto
from typing import List


class DeviceListViewImpl(DeviceListView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, device_list_out_dto: DeviceListOutDto):
        self.device_list_out_dto = device_list_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.device_list_out_dto)
