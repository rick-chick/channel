from channel.driver.view.flask.channel.flask_channel_update_view import FlaskChannelUpdateView
from tests.channel.factories import ChannelUpdateOutDtoFactory


def test_success():
    target = FlaskChannelUpdateView()
    target.add_result(ChannelUpdateOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskChannelUpdateView()
    target.add_exception(Exception())
    assert target.render() is not None
