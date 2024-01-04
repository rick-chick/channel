from channel.adapter.presenter.device.device_delete_view import (
    DeviceDeleteView
)

from channel.usecase.models import DeviceDeleteOutDto
from typing import List


class DeviceDeleteViewImpl(DeviceDeleteView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, device_delete_out_dto: DeviceDeleteOutDto):
        self.device_delete_out_dto = device_delete_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.device_delete_out_dto)
