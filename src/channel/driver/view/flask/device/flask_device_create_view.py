from typing import Any
from channel.adapter.presenter.device.device_create_view import DeviceCreateView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import DeviceCreateOutDto


class FlaskDeviceCreateView(DeviceCreateView):

    def __init__(self):
        self.exceptions = []
        self.device: Any = None

    def add_result(self, device_create_out_dto: DeviceCreateOutDto):
        self.device = device_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.device, self.exceptions).json()
