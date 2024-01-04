from channel.driver.view.flask.device.flask_device_delete_view import FlaskDeviceDeleteView
from tests.channel.factories import DeviceDeleteOutDtoFactory


def test_success():
    target = FlaskDeviceDeleteView()
    target.add_result(DeviceDeleteOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskDeviceDeleteView()
    target.add_exception(Exception())
    assert target.render() is not None
