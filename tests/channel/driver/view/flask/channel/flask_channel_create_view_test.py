from channel.driver.view.flask.channel.flask_channel_create_view import FlaskChannelCreateView
from tests.channel.factories import ChannelCreateOutDtoFactory


def test_success():
    target = FlaskChannelCreateView()
    target.add_result(ChannelCreateOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskChannelCreateView()
    target.add_exception(Exception())
    assert target.render() is not None
