from channel.driver.view.flask.channel.flask_channel_list_view import FlaskChannelListView
from tests.channel.factories import ChannelListOutDtoFactory


def test_success():
    target = FlaskChannelListView()
    target.add_result(ChannelListOutDtoFactory.build())
    assert target.render() is not None


def test_fail():
    target = FlaskChannelListView()
    target.add_exception(Exception())
    assert target.render() is not None
