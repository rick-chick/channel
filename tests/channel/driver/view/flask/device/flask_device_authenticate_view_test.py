from channel.driver.view.flask.device.flask_device_authenticate_view import FlaskDeviceAuthenticateView
from tests.channel.factories import DeviceAuthenticateOutDtoFactory


def test_success():
    target = FlaskDeviceAuthenticateView()
    target.add_result(DeviceAuthenticateOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskDeviceAuthenticateView()
    target.add_exception(Exception())
    assert target.render() is not None
