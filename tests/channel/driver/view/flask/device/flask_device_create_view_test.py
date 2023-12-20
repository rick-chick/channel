from channel.driver.view.flask.device.flask_device_create_view import FlaskDeviceCreateView
from tests.channel.factories import DeviceCreateOutDtoFactory


def test_success():
    target = FlaskDeviceCreateView()
    target.add_result(DeviceCreateOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskDeviceCreateView()
    target.add_exception(Exception())
    assert target.render() is not None
