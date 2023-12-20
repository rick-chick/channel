from channel.adapter.presenter.device.device_authenticate_view import DeviceAuthenticateView
from channel.usecase.models import DeviceAuthenticateOutDto


class CliDeviceAuthenticateView(DeviceAuthenticateView):

    def __init__(self):
        self.exceptions = []

    def add_result(self, device_authenticate_out_dto: DeviceAuthenticateOutDto):
        self.device = device_authenticate_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.device)
