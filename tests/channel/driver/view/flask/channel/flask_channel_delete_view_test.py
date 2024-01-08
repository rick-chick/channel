from channel.driver.view.flask.channel.flask_channel_delete_view import FlaskChannelDeleteView
from tests.channel.factories import ChannelDeleteOutDtoFactory


def test_success():
    target = FlaskChannelDeleteView()
    target.add_result(ChannelDeleteOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskChannelDeleteView()
    target.add_exception(Exception())
    assert target.render() is not None
