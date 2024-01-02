from channel.driver.view.cli.device.cli_device_list_view import CliDeviceListView
from tests.channel.factories import DeviceListOutDtoFactory


def test_success():
    target = CliDeviceListView()
    target.add_result(DeviceListOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliDeviceListView()
    target.add_exception(Exception())
    target.render()
