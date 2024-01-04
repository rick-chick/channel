from channel.driver.view.cli.device.cli_device_delete_view import CliDeviceDeleteView
from tests.channel.factories import DeviceDeleteOutDtoFactory


def test_success():
    target = CliDeviceDeleteView()
    target.add_result(DeviceDeleteOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliDeviceDeleteView()
    target.add_exception(Exception())
    target.render()
