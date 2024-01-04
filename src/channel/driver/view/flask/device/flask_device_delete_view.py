from typing import Any
from channel.adapter.presenter.device.device_delete_view import DeviceDeleteView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import DeviceDeleteOutDto


class FlaskDeviceDeleteView(DeviceDeleteView):

    def __init__(self):
        self.exceptions = []
        self.device: Any = None

    def add_result(self, device_delete_out_dto: DeviceDeleteOutDto):
        self.device = device_delete_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.device, self.exceptions).json()
