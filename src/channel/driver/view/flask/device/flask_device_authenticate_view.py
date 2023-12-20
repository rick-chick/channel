from typing import Any
from channel.adapter.presenter.device.device_authenticate_view import DeviceAuthenticateView
from channel.driver.view.flask.response_builder import ResponseBuilder
from channel.usecase.models import DeviceAuthenticateOutDto


class FlaskDeviceAuthenticateView(DeviceAuthenticateView):

    def __init__(self):
        self.exceptions = []
        self.device: Any = None

    def add_result(self, device_authenticate_out_dto: DeviceAuthenticateOutDto):
        self.device = device_authenticate_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self) -> Any:
        return ResponseBuilder(self.device, self.exceptions).json()
