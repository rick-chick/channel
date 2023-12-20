from channel.adapter.presenter.device.device_authenticate_view import (
    DeviceAuthenticateView
)

from channel.usecase.models import DeviceAuthenticateOutDto
from typing import List


class DeviceAuthenticateViewImpl(DeviceAuthenticateView):
    def __init__(self):
        self.exceptions: List[Exception] = []

    def add_result(self, device_authenticate_out_dto: DeviceAuthenticateOutDto):
        self.device_authenticate_out_dto = device_authenticate_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> DeviceAuthenticateOutDto:
        print(self.device_authenticate_out_dto)
