from typing import List

from channel.adapter.presenter.device import DeviceCreateView
from channel.usecase.models import DeviceCreateOutDto


class DeviceCreateViewImpl(DeviceCreateView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, device_create_out_dto: DeviceCreateOutDto):
        self.device_create_out_dto = device_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        print(self.device_create_out_dto)
