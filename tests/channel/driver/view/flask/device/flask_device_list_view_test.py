from channel.driver.view.flask.device.flask_device_list_view import FlaskDeviceListView
from tests.channel.factories import DeviceListOutDtoFactory


def test_success():
    target = FlaskDeviceListView()
    target.add_result(DeviceListOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskDeviceListView()
    target.add_exception(Exception())
    assert target.render() is not None
