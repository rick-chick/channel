from typing import Any
from channel.adapter.presenter.device.device_list_view import DeviceListView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import DeviceListOutDto


class FlaskDeviceListView(DeviceListView):

    def __init__(self):
        self.exceptions = []
        self.device: Any = None

    def add_result(self, device_list_out_dto: DeviceListOutDto):
        self.device = device_list_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.device, self.exceptions).json()
