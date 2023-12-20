from channel.driver.view.cli.device.cli_device_authenticate_view import CliDeviceAuthenticateView
from tests.channel.factories import DeviceAuthenticateOutDtoFactory


def test_success():
    target = CliDeviceAuthenticateView()
    target.add_result(DeviceAuthenticateOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliDeviceAuthenticateView()
    target.add_exception(Exception())
    target.render()
