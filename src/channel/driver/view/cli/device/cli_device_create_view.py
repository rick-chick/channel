from channel.adapter.presenter.device.device_create_view import DeviceCreateView
from channel.usecase.models import DeviceCreateOutDto


class CliDeviceCreateView(DeviceCreateView):

    def __init__(self):
        self.exceptions = []

    def add_result(self, device_create_out_dto: DeviceCreateOutDto):
        self.device = device_create_out_dto

    def add_exception(self, exception: Exception):
        self.exceptions.append(exception)

    def render(self):
        if len(self.exceptions) > 0:
            for e in self.exceptions:
                print(e)
            return
        print(self.device)
