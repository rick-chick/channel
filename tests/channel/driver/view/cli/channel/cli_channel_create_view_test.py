from channel.driver.view.cli.channel.cli_channel_create_view import CliChannelCreateView
from tests.channel.factories import ChannelCreateOutDtoFactory


def test_success():
    target = CliChannelCreateView()
    target.add_result(ChannelCreateOutDtoFactory.build())
    target.render()


def test_fail():
    target = CliChannelCreateView()
    target.add_exception(Exception())
    target.render()
