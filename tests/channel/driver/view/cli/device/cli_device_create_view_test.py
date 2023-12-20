from channel.driver.view.cli.device.cli_device_create_view import CliDeviceCreateView
from tests.channel.factories import DeviceCreateOutDtoFactory


def test_success():
    target = CliDeviceCreateView()
    target.add_result(DeviceCreateOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliDeviceCreateView()
    target.add_exception(Exception())
    target.render()
