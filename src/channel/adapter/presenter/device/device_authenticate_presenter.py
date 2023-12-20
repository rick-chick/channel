from channel.adapter.presenter.device.device_authenticate_view import (
    DeviceAuthenticateView,
)
from channel.usecase.models import DeviceAuthenticateOutDto
from channel.usecase.output_port.device.device_authenticate_output_port import (
    DeviceAuthenticateOututPort,
)


class DeviceAuthenticatePresenter(DeviceAuthenticateOututPort):

    def __init__(
        self,
        record_create_view: DeviceAuthenticateView
    ):
        self.record_create_view = record_create_view

    def prepare_success_view(self, record: DeviceAuthenticateOutDto) -> DeviceAuthenticateOutDto:
        self.record_create_view.add_result(record)
        return record

    def prepare_fail_view(self, exception: Exception):
        self.record_create_view.add_exception(exception)
